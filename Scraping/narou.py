from os import truncate
import time
import re
from urllib import request
from bs4 import BeautifulSoup

import requests
import pandas as pd
import json
import time as tm
import datetime
import gzip
from tqdm import tqdm
tqdm.pandas()
import xlsxwriter
import sqlite3

ncode = ""

info_url1 = "https://yomou.syosetu.com/rank/list/type/total_total/"
info_res1 = request.urlopen(info_url1)
soup1 = BeautifulSoup(info_res1, "html.parser")

#リクエストの秒数間隔(1以上を推奨)
interval = 1
### なろう小説API・なろう１８禁小説API を設定 ####
now_day = datetime.datetime.now()
now_day = now_day.strftime("%Y_%m_%d")

filename = 'Narou_All_OUTPUT_%s.xlsx'%now_day
sql_filename = 'Narou_All_OUTPUT_%s.sqlite3'%now_day
api_url="https://api.syosetu.com/novelapi/api/"    
# データをSqlite3形式でも保存する
is_save_sqlite = False
#####　以上設定、以下関数　##############

with open("novel.txt", "w", encoding="utf-8", newline="\n") as f:
  df = pd.DataFrame()
    
  payload = {'out': 'json','gzip':5,'of':'n','lim':1}
  res = requests.get(api_url, params=payload).content
  r =  gzip.decompress(res).decode("utf-8") 
  allcount = json.loads(r)[0]["allcount"]
  print('対象作品数  ',allcount)
  
  # all_queue_cnt = (allcount // 500) + 10
  all_queue_cnt = (10)
  
  #現在時刻を取得
  nowtime = datetime.datetime.now().timestamp()
  lastup = int(nowtime)
                   
  for i in tqdm(range(all_queue_cnt)):
    payload = {'out': 'json', 'order':'hyoka', 'gzip':5,'opt':'weekly','lim':500,'lastup':"1073779200-"+str(lastup)}
    
    # なろうAPIにリクエスト
    cnt=0
    while cnt < 5:
      try:
        res = requests.get(api_url, params=payload, timeout=30).content
        break
      except:
        print("Connection Error")
        cnt = cnt + 1
        tm.sleep(120) #接続エラーの場合、120秒後に再リクエストする
      
    r =  gzip.decompress(res).decode("utf-8")   
    # ncode = json.loads(r)[1]["ncode"]
    # print(ncode)

    # pandasのデータフレームに追加する処理
    df_temp = pd.read_json(r)
    df_temp = df_temp.drop(0)
    df = pd.concat([df, df_temp])
    
    last_general_lastup = df.iloc[-1]["general_lastup"]
    lastup = datetime.datetime.strptime(last_general_lastup, "%Y-%m-%d %H:%M:%S").timestamp()
    lastup = int(lastup)
    #取得間隔を空ける
    tm.sleep(interval)

  print('取得成功数:', len(df))
  # for i in range(1, len(df)):
  #   ncode = df.iloc[i]["ncode"]
  #   print(i, ":", ncode)
 
  for i in tqdm(range(1, len(df))):
    ncode = df.iloc[i]["ncode"]
    # print(i, ":", ncode)

    info_url = "https://ncode.syosetu.com/novelview/infotop/ncode/{}/".format(ncode)
  
    info_res = request.urlopen(info_url)
    soup = BeautifulSoup(info_res, "html.parser")
    pre_info = soup.select_one("#pre_info").text
    pre_info = re.sub(r",", "",pre_info)
    # print(pre_info)
    num_parts = int(re.search(r"全([0-9]+)部分", pre_info).group(1))
    
    for part in range(1, num_parts+1):
      deff = 14
      # 作品本文ページのURL
      url = "https://ncode.syosetu.com/{}/{:d}/".format(ncode, part)
  
      res = request.urlopen(url)
      soup = BeautifulSoup(res, "html.parser")
      ptags=soup.select("div#novel_honbun p")
      for i in range (1, len(ptags)+1):
        tmp = "#L{:d}".format(i)
        honbun = soup.select_one(tmp).text
        honbun += "\n"  # 次の部分との間は念のため改行しておく
    
        # if honbun == "☆\n":
        #     honbun = ""
        if honbun in "\n":
          honbun = ""
        
        honbun = re.sub(r" ","",honbun)
  
        # honbun = re.sub(r"[「」『』]","",honbun)
        # honbun = honbun.lstrip()
        
        # 保存
        f.write(honbun)
    
        # time.sleep(0.1)  # 次の部分取得までは1秒間の時間を空ける
      print("part {:d} downloaded (total: {:d} parts)".format(part, num_parts))  # 進捗を表示
      time.sleep(0.001)
    ncode = ""
  