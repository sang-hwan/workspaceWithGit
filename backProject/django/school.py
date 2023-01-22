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
from parsed_data.models import schoolData

def school_data():
    result = []
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    url = 'https://school.iamservice.net/organization/1674/group/2001892'
    # url = 'https://school.iamservice.net/organization/19710/group/2091428'

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
        '#fe-contents > div > div.inner_cont > a'
    )
    ## title
    title_list = soup.select(
        '#fe-contents > div > div.inner_cont > h4'
    )
    ## published_datetime
    date_list = soup.select(
        '#fe-contents > div > div.bx_etc > p > span:nth-child(2)'
    )

    for i in range(10):
        ## body
        url = url_list[i].get('href')
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select(
            '#articleBody > p'
        )
        body_obj = ""
        for p in body:
            body_obj += p.text
        ## file
        file_list = soup.select(
            '#__content > div.files > div > a'
        )
        file_obj = ""
        if file_list:
            for f in file_list:
                file_obj += ","
                file_obj += f.text
            file_obj = file_obj.replace('\n', '')
            file_obj = file_obj.replace('\t', '')
        
        item_obj = {
            'url': url_list[i].get('href'),
            'title': title_list[i].text,
            'published_datetime': date_list[i].text,
            'body': body_obj,
            'file': file_obj
        }
        
        result.append(item_obj)

    return result

# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    result = school_data()
    result.reverse()
    s_objects = schoolData.objects.order_by('-publishedDate')
    s_titles = []
    for s in s_objects:
        s_titles.append(s.title)
    for r in result:
        if r['title'] not in s_titles:
            schoolData(
                url = r['url'],
                title = r['title'],
                publishedDate = r['published_datetime'],
                body = r['body'],
                file = r['file']
            ).save()
        else:
            continue