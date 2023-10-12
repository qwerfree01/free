from server import refresh
import time,requests,os,re,datetime
from hashlib import sha256
refresh()


number1="01277644584"
pas="01277644584@mO"
member2="01228083123"
if "123456" == "123456":
	def orange_freemax(number2,number,password,time_value):
		try:
			with requests.Session()as req:
				url="https://services.orange.eg/SignIn.svc/SignInUser"
				
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
						"Password": "ig3yh*mk5l42@oj7QAR8yF"}}
						r = req.post(url, headers=headers, json=data).json()
						ctv = r["GenerateTokenResult"]["Token"]
						a = ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
						htv = (sha256(a.encode('utf-8')).hexdigest().upper())
						global c
						c=ctv
						global h
						h=htv
					except :
						return "Error"
				get_ctv_and_htv()
				
				head={"_ctv": c,
				"_htv": h,
				"Content-Type": "application/json; charset=UTF-8",
				"Content-Length": "167",
				"Host": "services.orange.eg",
				"Connection": "Keep-Alive",
				"Accept-Encoding": "gzip",
				"User-Agent": "okhttp/3.14.9"}
				
				data='{"appVersion":"6.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}'%(number,password)
				
				r=req.post(url,headers=head,data=data)
				#print(r)
				
				if r.json()["SignInUserResult"]["ErrorDescription"]=="Success":
					print("تم الدخول بنجاح ")
					#refresh()
					a=0
					while True:
						url1="https://backend.orange.eg/api/HybridFamily/ManageSharing"
						
						def sh_head():
							get_ctv_and_htv()
							head={"_ctv": c,
											"_htv": h,
											"x-microservice-name": "APMS",
											"Content-Type": "application/json; charset=UTF-8",
											"Content-Length": "155",
											"Host": "services.orange.eg",
											"Connection": "Keep-Alive",
											"Accept-Encoding": "gzip",
											"User-Agent": "okhttp/3.14.9"}
							head.update({"Host":"backend.orange.eg"})
							return (head)
						head0=(sh_head())
						
						sherif1='{"ActionType":"2","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":"%s","lang":"ar","Sharing":[{"SharedAmount":"1","SharingType":5}],"dial":"%s","IsEasyLogin":false,"password":"%s"}'%(number2,number,password)
						r2=req.post(url1,headers=head0,data=sherif1.encode("utf-8")).json()
						print(r2["ErrorDescription"])
						print("-"*55)
						time.sleep(time_value)
						url2="https://backend.orange.eg/api/HybridFamily/ManageSharing"
						head1=(sh_head())
						sherif2='{"ActionType":"4","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":"%s","lang":"ar","Sharing":[{"SharedAmount":"1","SharingType":5}],"dial":"%s","IsEasyLogin":false,"password":"%s"}'%(number2,number,password)
						delete=req.post(url2,headers=head1,data=sherif2.encode("utf-8")).json()
						print(delete["ErrorDescription"])
						a=a+1
						print(a)
						os.system("clear")
						print("success")
						
						month=(datetime.datetime.now().month)
						day=(datetime.datetime.now().day)
						hour=(datetime.datetime.now().time().hour)
						minute=(datetime.datetime.now().time().minute)
						second=(datetime.datetime.now().time().second)
						data=(str(month)+"-"+str(day),str(hour+3)+"-"+str(minute)+"-"+str(second))
						print(data)
						file=open("datatime.text","w")
						file.write(str(data)+"\n"*2+str(delete))
						print(requests.get("https://sherif.sherifomar.repl.co").status_code)
						
						try:
							print(os.remove("poetry.lock"))
							print(os.remove("pyproject.toml"))
						except:
							print("delet")
						
					
			
				else:
					print("الرقم او الباسورد غلط")
		except:
			print("error")
			return orange_freemax(member2,number1,pas,int(35))
	orange_freemax(member2,number1,pas,int(35))
	
else:
	print("الباسورد غلط")	
		
		