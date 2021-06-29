"""음악 파일을 병렬로 내려받는 예제"""
import concurrent.futures
import random
import time
from collections import namedtuple
from os import path
from urllib import parse
import requests
from my_logging import get_my_logger

logger = get_my_logger(__name__)

# 음악 파일의 이름과 데이터를 저장하기 위한 이름이 있는 튜플 정의
Music = namedtuple('music', 'file_name, file_content')

# 크롤링 요청별 간격 리스트 정의
RANDOM_SLEEP_TIMES = [x * 0.1 for x in range(10, 40, 5)]

# 크롤링 대상 URL 리스트
MUSIC_URLS = [
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/01PavanePourUneInfanteDfuntePourPianoMr19.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/02JeuxDeauPourPianoMr30.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/03SonatinePourPianoMr40-Modr.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/04MouvementDeMenuet.mp3',
    'https://archive.org/download/ThePianoMusicOfMauriceRavel/05Anim.mp3',
]

def download(url, timeout=180):
    # mp3 파일 이름 추출
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

    # 내려받기 종료를 로그에 출력
    logger.info("[download finished] {file_name}".format(file_name=file_name))

    # 이름 있는 튜플에 파일 이름과 mp3 데이터를 넣어 반환
    return Music(file_name=file_name, file_content=r.content)

if __name__ == '__main__':
    # 동시에 2개의 처리를 하기 위한 executor 생성하기
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        logger.info("[main start]")

        # executor.submit()으로 download() 함수를 병행 실행
        # download() 함수의 매개 변수로 music_url 전달
        # 병행 실행 처리의 결과는 futures 변수에 넣어둠
        futures = [executor.submit(download, music_url) for music_url in MUSIC_URLS]

        # download() 함수의 처리가 완료되면 반복문에서 반복해 결과 출력하기
        for future in concurrent.futures.as_completed(futures):
            # download() 함수의 실행 결과는 result() 메서드로 확인할 수 있음
            music = future.result()
            
            # music.filename에는 mp3 파일의 파일 이름이 들어있음
            # 이를 사용해 music.file_conten에 저장된 데이터를 파일로 저장함
            with open(music.file_name, 'wb') as fw:
                fw.write(music.file_content)
        logger.info("[main finished]")
