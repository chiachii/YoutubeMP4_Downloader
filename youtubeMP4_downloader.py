import datetime; #取得現在時間
import os
import youtube_dl
import time

now_time = datetime.datetime.now(); #設定預計執行的時間
url = input("輸入網址：")

file_path = 'D:\\Users\\Desktop\\Videos' 
if not os.path.exists(file_path):
    try:
        os.mkdir(file_path)
    except:
        print("目標資料夾已經存在")
        # path = os.getcwd() #取得當前路徑
os.chdir(r'D:\\Users\\Desktop\\Videos')  # 修改當前路徑
       
while True:
    try:
        with youtube_dl.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=True)
        break
    except:
        print(now_time)
        now_time = datetime.datetime.now();
        time.sleep(60)