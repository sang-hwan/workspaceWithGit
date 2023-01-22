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
from parsed_data.models import newsData

def news_data():
    result = []
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    url = 'http://feeds.bbci.co.uk/news/rss.xml'
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
        '#item > ul > li > a'
    )

    for i in range(10):
        ## title
        url = url_list[i].get('href')
        driver.get(url)
        
        ## 대기 시간 5초
        driver.implicitly_wait(5)
        
        ## 팝업창 종료
        main = driver.window_handles
        for e in main:
            if e != main[0]:
                driver.switch_to.window(e)
                driver.close()
        driver.switch_to.window(main[0])
                
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select(
            '#main-heading'
        )
        if 'sport' in url:
            title = soup.select(
                'article > header > h1'
            )
        title_obj = ""
        for t in title:
            title_obj += t.text
        ## published_datetime
        date = soup.select(
            '#main-content > div > div > div > article > header > div:nth-child(2) > ul > div > li > div > span > span > time'
        )
        if 'sport' in url:
            date = soup.select(
                'article > header > p > span:nth-child(1) > span > time > span:nth-child(1)'
            )
        date_obj = ""
        for d in date:
            date_obj += d.text
        ## body
        body = soup.select(
            '#main-content > div > div > div > article > div'
        )
        if 'sport' in url:
            body = soup.select(
                'article > div'
            )
        body_obj = ""
        for b in body:
            body_obj += b.text
        
        item_obj = {
            'url': url_list[i].get('href'),
            'title': title_obj,
            'published_datetime': date_obj,
            'body': body_obj
        }
        
        result.append(item_obj)
    
    return result

# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    result = news_data()
    result.reverse()
    n_objects = newsData.objects.order_by('-publishedDate')
    n_titles = []
    for n in n_objects:
        n_titles.append(n.title)
    for r in result:
        if r['title'] not in n_titles:
            newsData(
                url = r['url'],
                title = r['title'],
                publishedDate = r['published_datetime'],
                body = r['body']
            ).save()
        else:
            continue