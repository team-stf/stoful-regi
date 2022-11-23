# xhost 
# xhost + localhost
# http://httpbin.org/post",
import tkinter as tk
import requests # pip install requests
import json

root = tk.Tk()

root.title(u"売店リーダ")
root.geometry("400x300")

# Enterキー押したときの処理
import tkinter as tk
def enter_key():
    barnum = txt.get()  #barnum取得
    # txt.delete("1.0","end") # txtbox clear
    print(type(barnum))
    if barnum.isdecimal(): # intに変換できるか確認
        print("実行！")
        url = 'http://localhost:9000/api/store/store.php'
        payload = {
            'token': 'gzeK6Q1MWhSKzOMV',
            'barnum': barnum,
            }
        r = requests.post(
            "http://192.168.0.50:9000/api/store/store.php",
            data=payload,
            )
        print(r.status_code)    # HTTPのステータスコード取得
        print(r.text)    # レスポンスのHTMLを文字列で取得
    else:
        print('Noint')
        print(barnum)
    
# ラベル
lbl = tk.Label(text='Code')
lbl.place(x=30, y=70)

#テキストボックス
txt = tk.Entry(width=20)
txt.place(x=90, y=70)
txt.bind("<Return>", lambda event: enter_key())

#実行
root.mainloop()