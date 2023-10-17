import json,requests

from flask import  Flask,render_template_string,request
app=Flask(__name__)
@app.route("/")
def home():
	return render_template_string("""<br><br>
	<center>
	<form method="get" action="/send" >
	<input style="width: 40%;height: 0,3%;" type="text" name="url" placeholder="enter url"><br><br>
	<button type="submit">submit</button>
	</form>
	</center>
	
	""")
@app.route("/send",methods=["GET"])
def sh():
	data=request.args.get("url")
	url="http://" in data or "https://" in data
	if data=="" or url==False :
		return "error"
	else:
		file=open("new.text","a")
		file.write(data+"\n")
		return "success"
		
@app.route("/data")
def rea():
	file=open("new.text","r")
	x=(file.read())
	li=[]
	for i in x.split():
		li.append(str(requests.get(i).status_code))
	return li
	
	
if __name__=="__main__":
	app.run(debug=True,port=5000)


