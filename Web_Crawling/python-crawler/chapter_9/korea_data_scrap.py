"""특정 지역의 미세먼지 정보를 크롤링합니다."""
import urllib
import requests
from bs4 import BeautifulSoup
import json

# URL 관련 정보를 선언합니다.
service_key = "자신의 서비스키를 입력해주세요"
end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=" + service_key
default_options = {
    "numOfRows": 1,
    "pageNo": 1,
    "dataTerm": "Daily",
    "ver": 1.3
}

def get_dust_info(region):
    """특정 지역의 미세먼지 수치 추출하기"""

    # URL을 생성합니다.
    default_options["stationName"] = region
    params = urllib.parse.urlencode(default_options)
    url = end_point + "&" + params

    # 요청합니다.
    r = requests.get(url)
    xml = r.text

    # 필요한 정보를 스크레이핑합니다.
    soup = BeautifulSoup(xml, 'html.parser')
    pm_10 = soup.select('item > pm10Value')[0].text
    pm_25 = soup.select('item > pm25Value')[0].text
    
    return {
        "region": region,
        "pm_10": pm_10,
        "pm_25": pm_25,
    }

if __name__ == '__main__':
    output_a = get_dust_info("강서구")
    print(json.dumps(output_a, ensure_ascii=False))
    output_a = get_dust_info("강남구")
    print(json.dumps(output_a, ensure_ascii=False))
