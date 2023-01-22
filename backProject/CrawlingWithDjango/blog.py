from bs4 import BeautifulSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# python manage.py shell을 실행하는 것과 비슷한 방법
import django
django.setup()
# schoolData model
from parsed_data.models import blogData

def blog_data():
    result = []
       
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    url = 'https://blog.naver.com/PostList.nhn?blogId=sntjdska123&from=postList&categoryNo=51'
    # url = 'https://blog.naver.com/PostList.nhn?blogId=hellopolicy&from=postList&categoryNo=168'

    driver.get(url)
    ## 대기 2초
    # time.sleep(2)
    ## 페이지의 elements 모두 가져오기
    html = driver.page_source

    ## BeautifulSoup으로 html소스를 python객체로 변환
    ## (html, parser)
    soup = BeautifulSoup(html, 'html.parser')

    ## url
    url_list = soup.select(
        '#PostThumbnailAlbumViewArea > ul > li > a'
    )
    ## title
    title_list = soup.select(
        '#PostThumbnailAlbumViewArea > ul > li > a > div.area_text > strong'
    )
    ## published_datetime
    date_list = soup.select(
        '#PostThumbnailAlbumViewArea > ul > li > a > div.area_text > span.date'
    )

    for i in range(10):
        url = "https://blog.naver.com" + url_list[i].get('href')
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find_all('b')
        body_obj = ""
        for b in body:
            body_obj += b.get_text()
            
        item_obj = {
            'url': "https://blog.naver.com" + url_list[i].get('href'),
            'title': title_list[i].text,
            'published_datetime': date_list[i].text,
            'body': body_obj
        }
        
        result.append(item_obj)
    
    return result

# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    result = blog_data()
    result.reverse()
    b_objects = blogData.objects.order_by('-publishedDate')
    b_titles = []
    for b in b_objects:
        b_titles.append(b.title)
    for r in result:
        if r['title'] not in b_titles:
            blogData(
                url = r['url'],
                title = r['title'],
                publishedDate = r['published_datetime'],
                body = r['body']
            ).save()
        else:
            continue