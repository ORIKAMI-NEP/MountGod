import re;
import time
from urllib import request
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup

YahooUrl = 'https://news.yahoo.co.jp/ranking/comment'
YahooRes = request.urlopen(YahooUrl)
YahooSoup = BeautifulSoup(YahooRes, "html.parser")
articles = [tag.get('href') for tag in YahooSoup(class_='newsFeed_item_link')]

with open('../../data/yahooComment.txt', 'w', encoding="utf-8", newline='\n')as f:
    for rank in range(0, 39):
        articleUrl = articles[rank]
        commentNum = 0
        maxComment = 1
        page = 1
        while(commentNum < maxComment):
            print(str(rank + 1) + 'article:' + str(page) +  'page...start\n')
            pageUrl = articleUrl + '/comments?page=' + str(page) + '&t=t&order=recommended'
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.get(pageUrl)
            time.sleep(2)
            html = driver.page_source
            pageSoup = BeautifulSoup(html, 'html.parser')
            commentUrl = pageSoup.find(class_='news-comment-plguin-iframe').get('src')
            driver.quit()

            commentRes = request.urlopen(commentUrl)
            commentSoup = BeautifulSoup(commentRes, "html.parser")

            if(page == 1):
                maxComment = int(commentSoup.select('.counter > span')[0].text.strip("/""件"))

            comment = ""
            for tag in commentSoup(class_='cmtBody'):
                comment += tag.text + '\n'
                commentNum += 1
            print(str(rank + 1) + 'article:' + str(page) + "page...finish")
            page += 1
            f.writelines(comment)
