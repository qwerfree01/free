from flask import Flask
from hashlib import sha256
import requests,json
app=Flask(__name__)
@app.route("/")

def get_ctv_and_htv():
			 def ctv_htv():
			     try:
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
			 c=requests.get("https://myflasksherif.sherifomar.repl.co").status_code
			 print(c)
			 return {"ctv":ctv_htv[0],"htv":ctv_htv[1]}
			 
if __name__=="__main__":
	app.run(debug=True)