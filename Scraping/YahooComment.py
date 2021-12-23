import time
from urllib import request
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
#from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

#プロキシ設定
PROXY = "{proxy.anan-nct.ac.jp}:{8080}"

# ブラウザをバックグラウンド実行
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--proxy-server=http://%s' % PROXY)
# ブラウザ起動
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# 対象要素のテキスト取得


def getItem(element, name, name2):
    result = ""
    elem = element.find_elements_by_class_name(name)
    if len(elem) > 0:
        if name2 == "":
            result = elem[0].text.strip()
        else:
            result = elem[0].find_element_by_class_name(name2).text.strip()
    return result

# 認証者コメント出力(保留)


def print_authorComment(comment):
    comment_boxes = driver.find_elements_by_css_selector(
        'li[id^="authorcomment-"]')
    for comment_box in comment_boxes:
        # コメント取得
        elem_comment = comment_box.find_element_by_class_name("comment")
        comment += elem_comment.text.strip().rstrip('...もっと見る')
        comment += comment_box.find_element_by_class_name(
            "hideAthrCmtText").get_attribute("textContent")
    return comment

# 一般者コメント出力


def print_generalComment(comment):
    comment = ""
    comment_boxes = driver.find_elements_by_css_selector('li[id^="comment-"]')
    for comment_box in comment_boxes:
        # コメント取得
        comment += getItem(comment_box, "cmtBody", "") + "\n"
        # 返信数
        reply = int(getItem(comment_box, "reply", "num") or "0")
        if reply == 0:
            continue
        # 返信出力
        comment = print_reply(comment_box, reply, comment)
    return comment

# 返信コメント出力


def print_reply(element, reply, comment):
    # 「返信」 リンクを click
    rep_links = element.find_elements_by_css_selector('a.btnView.expandBtn')
    for rep_link in rep_links:
        rep_link.click()
        time.sleep(2)

    # 「もっと見る」 リンクを click
    response_boxes = element.find_elements_by_class_name("response")
    for i in range(int(reply/10)):
        if len(response_boxes) > 0 and (reply % 10) > 0:
            rep_links = response_boxes[0].find_elements_by_css_selector(
                'a.moreReplyCommentList')
            for rep_link in rep_links:
                rep_link.click()
                time.sleep(2)

    # 返信コメント 取り出し
    replys = response_boxes[0].find_elements_by_css_selector(
        'li[id^="reply-"]')
    cno = 1
    for reply in replys:
        cmtBodies = reply.find_elements_by_css_selector(
            'div.action article p span.cmtBody')
        if len(cmtBodies) == 0:
            continue
        # コメント取得
        comment += cmtBodies[0].text.strip()
        cno += 1
    return comment


comment = ""
YahooUrl = ""
genre = ["domestic", "world", "business", "entertainment",
         "sports", "it-science", "life", "local"]

# メインループ
with open("../../data/yahooComment.txt", "w", encoding="utf-8", newline="")as f:
    for i in range(0, 7):
        YahooUrl = "https://news.yahoo.co.jp/ranking/comment/" + genre[i]
        YahooRes = request.urlopen(YahooUrl)
        YahooSoup = BeautifulSoup(YahooRes, "html.parser")
        articles = [tag.get('href')
                    for tag in YahooSoup(class_="newsFeed_item_link")]
        for rank in range(0, 39):
            print(str((rank + 1 + 40 * i)) + " atricle")
            articleUrl = articles[rank]
            page = 1
            maxPage = 2
            while page < maxPage:
                driver.get(
                    articleUrl + "/comments?order=recommended&page=" + str(page))
                time.sleep(2)
                iframe = driver.find_element_by_class_name(
                    "news-comment-plguin-iframe")
                driver.switch_to.frame(iframe)

                if page == 1:
                    # コメント数を取得
                    maxComment = int(driver.find_element_by_css_selector(
                        ".counter > span").text.strip("/""件"))
                    maxPage = int(maxComment / 10) + 1
                    if maxComment % 10 != 0:
                        maxPage += 1
                    # 認証者コメント(保留)
                    # comment = print_authorComment(comment)
                # 一般者コメント
                comment = print_generalComment(comment)
                f.writelines(comment)
                page += 1
    driver.quit()
