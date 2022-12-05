import requests 
from datetime import datetime as dt

# Enterキー押したときの処理
def ctl(barnum):
    tdatetime = dt.now()
    tstr = tdatetime.strftime('%Y-%m-%d %H:%M:%S')
    if barnum.isdecimal(): # intに変換できるか確認
        try:
            payload = {
                'token': 'gzeK6Q1MWhSKzOMV',
                'barnum': barnum,
                }
            r = requests.post(
                "https://api-stoful.meiden-travel.jp/api/store/store.php",
                data=payload,
                timeout=2,
                )
            # print(r.status_code)
            print(r.text) # 出力
        except:
            print('timeout')
            with open('error.txt', 'a') as fout:
                fout.write('Timeout ' + tstr + ' : ' + barnum + '\n')

    else:
        #print('Noint')
        pass
    
while True:
    num= input()
    ctl(num)