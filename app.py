#pylint:disable=W0123
import json,requests

from flask import  Flask,render_template_string,request
app=Flask(__name__)

@app.route("/")
def rea():
	url=requests.get("https://yousefsherif.pythonanywhere.com/data_url").text
	#print(url.strip())
	li=[]
	for i in url.split("\n"):
		try:
			#return (i.strip())
			status=(requests.get(i.strip()).status_code)
			li.append(status)
		except:
			finsh=("finsh")
			li.append(finsh)
			
	return render_template_string('''
	<center>
	{}<br><br>
	{}
	</center>
	'''.format(str(url),str(li)))
	
	

if __name__=="__main__":
	app.run(debug=True,port=5000)


