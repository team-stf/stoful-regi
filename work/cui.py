import requests 
import json

url="http://192.168.0.50:9000/api/store/store.php"

# Enterキー押したときの処理
def ctl(barnum):
    if barnum.isdecimal(): # intに変換できるか確認
        url = 'http://localhost:9000/api/store/store.php'
        payload = {
            'token': 'gzeK6Q1MWhSKzOMV',
            'barnum': barnum,
            }
        r = requests.post(
            "http://192.168.0.50:9000/api/store/store.php",
            data=payload,
            )
        # print(r.status_code)    # HTTPのステータスコード取得
        print(r.text)    # レスポンスのHTMLを文字列で取得
    else:
        # print('Noint')
        pass
    
while True:
    num= input()
    ctl(num)