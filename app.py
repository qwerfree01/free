from flask import Flask,jsonify,session
from hashlib import sha256
import requests,json

app=Flask(__name__)
app.secret_key = 'secret_key'  # مفتاح سري لتوقيع الجلسة
@app.route("/")

def ctv_sh():
						url = "https://services.orange.eg/GetToken.svc/GenerateToken"
						headers = {"Content-Type": "application/json; charset=UTF-8",
						"Content-Length": "78",
						"Host": "services.orange.eg",
						"Connection": "Keep-Alive",
						"User-Agent": "okhttp/3.12.1"}
						data = {"channel": {
						"ChannelName": "MobinilAndMe",
						"Password": "ig3yh*mk5l42@oj7QAR8yF"}}
						
						r = requests.post(url, headers=headers, json=data)
						ctv = r.json()["GenerateTokenResult"]["Token"]
						a = ctv +',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
						htv = (sha256(a.encode('utf-8')).hexdigest())
						if 'count' not in session:
							session['count'] = 1
						else:
							session['count'] += 1
							
						return jsonify({"c":ctv,"h":htv.upper(),"len": f"{session['count']}"})
			 
if __name__=="__main__":
	app.run(debug=True)