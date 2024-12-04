from flask import *
from hashlib import sha256
import requests,json,base64,time
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
						
						
						
@app.route("/vodafone_flex")
def orange():
	return render_template("index.html",backage="اختيار حجم الباقة")
	

@app.route("/voda",methods=["POST","GET"])
def subscribe():
	if request.method=="POST":
		change_id=request.form["options"]
		
		if change_id == "add":
			return render_template_string('''
			<!DOCTYPE html>
			<html lang="en">
			<head>
			    <meta charset="UTF-8">
			    <meta http-equiv="X-UA-Compatible" content="IE=edge">
			    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			    </head>
			    
			    <body align="center">
			    
			    <h2><font color="red">Designed by sherif omar</font></h2>
			    <p>إضافة</p>
			    
			    <form method="post" action="/add">
			    
			    	<input type="number" name="number" placeholder="Enter Your Phone owner" required="">
			    	
			    	<br><br>
			    	
			    	<input type="password" name="pas" placeholder="Enter Your Password" required="">
			    	
			    	<br><br>
			    	
			    	<input type="number" name="member" placeholder="Enter Your Phone Member" required="">
			    	
			    	<br><br><br>
			    	
			    	<button><font color="green">Add</font></button>
			    	<br><br>~~
			    	
			    	
			    </form>
			    
			</body>
			</html>''')
		elif change_id == "accept":
			
			return render_template_string('''
			<!DOCTYPE html>
			<html lang="en">
			<head>
			    <meta charset="UTF-8">
			    <meta http-equiv="X-UA-Compatible" content="IE=edge">
			    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			    </head>
			    
			    <body align="center">
			    
			    <h2><font color="red">Designed by sherif omar</font></h2>
			    <p>قبول الطلب</p>
			    
			    <form method="post" action="/accept">
			    
			    	<input type="number" name="number" placeholder="Enter Your Phone Member" required="">
			    	
			    	<br><br>
			    	
			    	<input type="password" name="pas" placeholder="Enter Your Password Member" required="">
			    	
			    	<br><br>
			    	
			    	<input type="number" name="owner" placeholder="Enter Your Phone Owner" required="">
			    	
			    	<br><br><br>
			    	
			    	<button><font color="green">Accept</font></button>
			    	<br><br>~~
			    	
			    	
			    </form>
			    
			</body>
			</html>''')
			
		elif change_id == "delete":
			return render_template_string('''
			<!DOCTYPE html>
			<html lang="en">
			<head>
			    <meta charset="UTF-8">
			    <meta http-equiv="X-UA-Compatible" content="IE=edge">
			    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			    </head>
			    
			    <body align="center">
			    
			    <h2><font color="red">Designed by sherif omar</font></h2>
			    <p>حذف رقم من العيلة</p>
			    
			    <form method="post" action="/delete">
			    
			    	<input type="number" name="number" placeholder="Enter Your Phone owner" required="">
			    	
			    	<br><br>
			    	
			    	<input type="password" name="pas" placeholder="Enter Your Password Owner" required="">
			    	
			    	<br><br>
			    	
			    	<input type="number" name="member" placeholder="Enter Your Phone member" required="">
			    	
			    	<br><br><br>
			    	
			    	<button><font color="green">Delete</font></button>
			    	<br><br>~~
			    	
			    	
			    </form>
			    
			</body>
			</html>''')
		
		
		
@app.route("/add",methods=["POST","GET"])
def add():
	if request.method=="POST":
		number=request.form["number"]
		password=request.form["pas"]
		member=request.form["member"]
		try:
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
			access_token = response["access_token"]
			
			url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
			
			head={"api-host":"ProductOrderingManagement","useCase": "MIProfile",
			"Authorization": f"Bearer {access_token}",
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
			"Content-Length": "151",
			"Host": "mobile.vodafone.com.eg",
			"Connection": "Keep-Alive",
			"Accept-Encoding": "gzip",
			"User-Agent": "okhttp/4.11.0"}
			#add
			data={"category":[{"listHierarchyId":"PackageID","value":"523"},{"listHierarchyId":"TemplateID","value":"10"},{"listHierarchyId":"TierID","value":"523"}],"parts":{"characteristicsValue":{"characteristicsValue":[{"characteristicName":"quotaDist1","type":"percentage","value":"10"}]},"member":[{"id":[{"schemeName":"MSISDN","value":number}],"type":"Owner"},{"id":[{"schemeName":"MSISDN","value":member}],"type":"Member"}]},"type":"SendInvitation"}
			
			response = requests.post(url, headers=head, json=data).json()
			if str(response)=="{}":
				return '''<center><br><br>تم الاضافة بنجاح اذهب الي قبول الطلب</center>'''
			else:
				return '''<center><br><h1>لم يتم الاضافة ربما الرقم ف مجموعة تاني او ربما الاونر منضاف به ارقام اخرا راجع ع الاونر والفرد</h1></center>'''
		except:
			return '''<center>Password Error</center>''' 
		


@app.route("/accept",methods=["POST","GET"])
def accept():
	if request.method=="POST":
		member=request.form["number"]
		password=request.form["pas"]
		owner=request.form["owner"]
		try:
			
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
			    "username": member,
			    "password": password,
			    "grant_type": "password",
			    "client_secret": "a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",
			    "client_id": "my-vodafone-app"
			}
			response = requests.post(url, headers=headers, data=data).json()
			access_token = response["access_token"]
			
			url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
			
			head={"api-host":"ProductOrderingManagement","useCase": "MIProfile",
			"Authorization": f"Bearer {access_token}",
			"api-version": "v2",
			"x-agent-operatingsystem": "9",
			"clientId": "AnaVodafoneAndroid",
			"x-agent-device": "Xiaomi Redmi 6A",
			"x-agent-version": "2024.3.2",
			"x-agent-build": "592",
			"msisdn": member,
			"Accept": "application/json",
			"Accept-Language": "ar",
			"Content-Type": "application/json; charset=UTF-8",
			"Content-Length": "151",
			"Host": "mobile.vodafone.com.eg",
			"Connection": "Keep-Alive",
			"Accept-Encoding": "gzip",
			"User-Agent": "okhttp/4.11.0"}
			#add
			data='{"category":[{"listHierarchyId":"TemplateID","value":"47"}],"name":"FlexFamily","parts":{"member":[{"id":[{"schemeName":"MSISDN","value":"%s"}],"type":"Owner"},{"id":[{"schemeName":"MSISDN","value":"%s"}],"type":"Member"}]},"type":"AcceptInvitation"}'%(owner,member)
			
			response = requests.post(url, headers=head, data=data).json()
			
			if str(response)=="{}":
				return '''<center><br><h1>تم القبول الطلب</h1></center>'''
				
			elif response['reason']== 'Generic System Error':
				return '''<center><br><h1>انتظر قليلا ثم حاول في وقت لاحق</h1></center>'''
			if response['reason']=='Customer not eligible-Family member':
				return '''<center><br><h1>الرقم منضاف بالفعل تاكد من التطبيق</h1></center>'''
				
			else:
				return '''<center><br><h1></h1></center>'''
				
		except:
			return '''<center><h1>Password Error</h1></center>'''
		


@app.route("/delete",methods=["POST","GET"])
def delete():
	if request.method=="POST":
		number=request.form["number"]
		pas=request.form["pas"]
		member=request.form["member"]
		
		return number+pas+member


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
		

@app.route("/vodafone_add_mb")
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
			
			data={"promoId":2633,"channelId":"1","wlistId":2553,"contextualPromoId":"13","triggerId":189,"param3":"5","param4":14,"param6":0,"param1":"2","param2":500}
			response = requests.post(url, headers=head, json=data).json()
				
			return str(response["eDesc"])
		
	

			 
if __name__=="__main__":
	app.run()