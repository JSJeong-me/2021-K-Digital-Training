"""Celery를 사용하는 예제"""
import random
import time
from os import path
from urllib import parse
import requests
from celery import Celery
from pydub import AudioSegment
from my_logging import get_my_logger

logger = get_my_logger(__name__)

# 크롤링 요청 간격 리스트 정의
RANDOM_SLEEP_TIMES = [x * 0.1 for x in range(10, 40, 5)]

# 아티스트 이름
ARTIST_NAME = "Maurice RAVEL "

# 앨범 타이틀
ALBUM_NAME = "The Piano Music of Maurice Ravel from archive.org"

# 크롤링 대상 URL 리스트
MUSIC_URLS = [
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/01PavanePourUneInfanteDfuntePourPianoMr19.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/02JeuxDeauPourPianoMr30.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/03SonatinePourPianoMr40-Modr.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/04MouvementDeMenuet.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/05Anim.mp3',
]

# Reids의 0번째 DB를 사용하는 예
app = Celery('crawler_with_celery_sample', broker='redis://localhost:6379/0')
app.conf.update(
    # Redis에 태스크 또는 실행 결과를 저장할 때의 형식을 JSON으로 지정
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Asia/Seoul',
    enable_utc=True,  # Celery 태스크 내부의 시간을 UTC로 다룸
    # 1개의 워커는 동시에 1개의 프로세스만 실행하게 함
    worker_max_tasks_per_child=1,
    # Redis에 저장되는 태스크의 실행 결과는 60초가 지나면 제거(파기)함
    result_expires=60,
    # 워커가 표준 출력으로 출력한 내용을 명령어 실행 터미널에 출력하지 않음
    worker_redirect_stdouts=False,
    # 태스크 실행 시간이 180초를 넘으면 자동으로 종료함
    task_soft_time_limit=180,

    # 어떤 태스크를 어떤 워커로 라우팅할지 설정함
    task_routes={
        'crawler_with_celery_sample.download': {
            'queue': 'download',
            'routing_key': 'download',
        },
        'crawler_with_celery_sample.cut_mp3': {
            'queue': 'media',
            'routing_key': 'media',
        },
    },
)

# 재시도는 최대 2회까지, 재시도할 때는 10초 간격을 둠
@app.task(bind=True, max_retries=2, default_retry_delay=10)
def download(self, url, timeout=180):
    """파일 내려받기"""
    try:
        # mp3 파일 이름을 URL을 기반으로 추출
        parsed_url = parse.urlparse(url)
        file_name = path.basename(parsed_url.path)

        # 요청 간격을 랜덤하게 선택
        sleep_time = random.choice(RANDOM_SLEEP_TIMES)

        # 내려받기 시작을 로그에 출력
        logger.info("[download start] sleep: {time} {file_name}".format(time=sleep_time, file_name=file_name))

        # 요청 대기
        time.sleep(sleep_time)

        # 음악 파일 내려받기
        r = requests.get(url, timeout=timeout)
        with open(file_name, 'wb') as fw:
            fw.write(r.content)

        # 내려받기 종료를 로그에 출력
        logger.info("[download finished] {file_name}".format(file_name=file_name))
        cut_mp3.delay(file_name)  # cut_mp3 함수 실행을 태스크로 큐에 넣음

    except requests.exceptions.RequestException as e:
        # 예외가 발생하면 로그를 출력하고 재시도
        logger.error("[download error - retry] file: {file_name}, e: {e}".format( file_name=file_name, e=e))
        raise self.retry(exc=e, url=url)

@app.task
def cut_mp3(file_name):
    """앞의 2초를 추출해서 저장하기"""
    logger.info("[cut_mp3 start] {file_name}".format(file_name=file_name))
    # 내려받은 파일을 pydub 데이터 형식으로 변환해서 읽어 들임
    music = AudioSegment.from_mp3(file_name)

    # mp3 파일의 앞 2초만 잘라내기
    head_time = 2 * 1000  # milliseconds
    head_part = music[:head_time]  # 잘라냄
    root_name, ext = path.splitext(file_name)  # 파일 이름을 확장자와 이외의 부분으로 분할

    # 저장
    # 원래 파일과 구별할 수 있게 확장자 이름 앞에 _head를 붙임
    file_handler = head_part.export(
        root_name + "_head" + ext,
        format="mp3",
        tags={
            'title': root_name,
            'artist': ARTIST_NAME,
            'album': ALBUM_NAME,
        }
    )
    # 주의: 파일 핸들러 닫기를 잊으면 안 됩니다.
    file_handler.close()
    logger.info("[cut_mp3 finished] {file_name}".format(file_name=file_name))

if __name__ == '__main__':
    logger.info("[main start]")
    # 크롤링 대상 URL 별로 download() 함수를 태스크로 큐에 넣음
    # 큐에 들어간 태스크는 워커에 의해서 자동 실행됨
    for music_url in MUSIC_URLS:
        download.delay(music_url)
    logger.info("[main finished]")
