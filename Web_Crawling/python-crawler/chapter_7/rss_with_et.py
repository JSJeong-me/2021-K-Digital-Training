"""xml.etree.ElementTree로 RSS 만들기"""
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 사용자 정의 네임 스페이스(http://my-service.com/xmlns/book은 단순한 예입니다)
NAMESPACES = {'book': 'http://my-service.com/xmlns/book'}

def create_rss():
    """RSS 만들기"""
    for ns_name, ns_uri in NAMESPACES.items():
        ET.register_namespace(ns_name, ns_uri) # 네임 스페이스 등록

    # <rss> 요소 만들기
    elm_rss = ET.Element(
        "rss",
        attrib={
            'version': "2.0",
            'xmlns:book': NAMESPACES['book']
        },
    )

    # <channel> 요소 만들기
    elm_channel = ET.SubElement(elm_rss, 'channel')

    # channel 요소의 서브 요소를 한 번에 추가하기
    channel_sources = {
        'title': "위키북스의 도서 목록",
        'link': "http://example.com",
        'description': "설명을 입력했다고 가정합니다.",
    }
    children_of_channel = []
    for tag, text in channel_sources.items():
        child_elm_of_channel = ET.Element(tag)
        child_elm_of_channel.text = text
        children_of_channel.append(child_elm_of_channel)

    # 한 번에 추가하기
    elm_channel.extend(children_of_channel)

    # <item> 요소 추가하기: 하나씩 서브 요소 추가해보기
    elm_item = ET.SubElement(elm_channel, 'item')

    # <item><title> 요소 추가하기
    elm_item_title = ET.SubElement(elm_item, 'title')
    elm_item_title.text = "파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발"

    # <item><link> 요소 추가하기
    elm_item_link = ET.SubElement(elm_item, 'link')
    elm_item_link.text = "http://example.com"

    # <item><description> 요소 추가하기
    elm_item_description = ET.SubElement(elm_item, 'description')
    elm_item_description.text \
        = ( '<a href="http://example.com">이스케이프 처리 확인 전용 링크</a>'
            "설명을 입력했다고 가정합니다.")

    # <item><book:publisher> 요소 추가하기
    elm_item_publisher = ET.SubElement(elm_item, 'book:publisher', id="1")
    elm_item_publisher.text = "위키북스"

    # XML 문자열로 변환하기
    xml = ET.tostring(elm_rss, 'utf-8')

    # 앞에 <?xml version="1.0"?>를 추가하고 보기 좋게 가공하기
    with minidom.parseString(xml) as dom:
        return dom.toprettyxml(indent="  ")

if __name__ == '__main__':
    rss_str = create_rss()
    print(rss_str)
