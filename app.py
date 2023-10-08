from flask import Flask
from hashlib import sha256
import requests,json
app=Flask(__name__)
@app.route("/")

def get_ctv_and_htv():
			 def ctv_htv():
			     try:
			     	url="https://myflasksherif.sherifomar.repl.co/"
			     	head={'Host': 'myflasksherif.sherifomar.repl.co',
			     	'sec-ch-ua-mobile': '?1',
			     	'sec-ch-ua-platform': 'Android',
			     	'upgrade-insecure-requests': '1',
			     	'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
			     	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			     	'sec-fetch-site': 'none',
			     	'sec-fetch-mode': 'navigate',
			     	'sec-fetch-user': '?1',
			     	'sec-fetch-dest': 'document',
			     	'accept-encoding': 'gzip, deflate, br',
			     	'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
			     	r=requests.get(url,headers=head).text
			     	url = 'https://services.orange.eg/GetToken.svc/GenerateToken'
			     	headers = {
			     	"Content-Type": "application/json; charset=UTF-8",
			     	"Content-Length": "78",
			     	"Host": "services.orange.eg",
			     	"Connection": "Keep-Alive",
			     	"User-Agent": "okhttp/3.12.1"}
			     	data = {
			     	"channel": {
			     	"ChannelName": "MobinilAndMe",
			     	"Password": "ig3yh*mk5l42@oj7QAR8yF"
			     	}}
			     	r = requests.post(url, headers=headers, json=data).json()
			     	ctv = r["GenerateTokenResult"]["Token"]
			     	a = ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
			     	htv = (sha256(a.encode('utf-8')).hexdigest().upper())
			     	return ctv + ' ' + htv
			     except :
			     	return "Error"
			 ctv_htv = ctv_htv().split(' ')
			 return {"ctv":ctv_htv[0],"htv":ctv_htv[1]}
			 
if __name__=="__main__":
	app.run(debug=True)