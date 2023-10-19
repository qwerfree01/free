#pylint:disable=W0123
import json,requests

from flask import  Flask,render_template_string,request
app=Flask(__name__)
@app.route("/")
def home():
	file=open("new.text","r")
	x=eval(file.read())
	return render_template_string("""<br><br>
	<center><br><br>
	{}
	<br><br>
	<form method="get" action="/send" >
	<input style="width: 40%;height: 0,3%;" type="text" name="url" placeholder="enter url"><br><br>
	<button type="submit">submit</button>
	</form><br><br>
	<a href="/data">data status code</a><br><br>
	<a href="/delete">Delete url</a>
	
	</center>
	
	""".format(x))
	
@app.route("/send",methods=["GET"])
def sh():
	data=request.args.get("url")
	url="http://" in data or "https://" in data
	if data=="" or url==False :
		return "error"
	else:
			file=open("new.text","r")
			x=eval(file.read())
			x.append(data)
			#print(x)
			
			file=open("new.text","w")
			file.write(str(x))
			return "success"

@app.route("/data")
def rea():
	file=open("new.text","r")
	x=eval(file.read())
	li=[]
	for i in x:
		li.append(str(requests.get(i).status_code))
	return li
	
@app.route("/delete")
def delte():
	file=open("new.text","r")
	d=eval(file.read())
	return render_template_string("""
	<center><br><br>
	{}
	<br><br>
	<form method="get" action="/del" >
	<input style="width: 40%;height: 0,3%;" type="text" name="del" placeholder="enter url Delete"><br><br>
	<button type="submit">submit</button>
	</form><br><br>
	
	
	""".format(d))
@app.route("/del",methods=["GET"])
def dele():
	delete=request.args.get("del")
	
	file=open("new.text","r")
	x=eval(file.read())
	x.remove(str(delete))
	file=open("new.text","w")
	file.write(str(x))
	return "success delete"
	
if __name__=="__main__":
	app.run(debug=True,port=5000)


