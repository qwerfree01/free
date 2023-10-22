#pylint:disable=W0123
import json,requests

from flask import  Flask,render_template_string,request
app=Flask(__name__)

@app.route("/")
def rea():
	def spam():
		try:
			spam="https://spam.qwerfree.repl.co"
			url1=requests.get(spam).status_code
			return url1
		except:
			return "error"
	spam()
	link="https://spam.qwerfree.repl.co"+"==>  "+str(spam())
	#ahmed
	def ahmed():
		try:
			ahmed_link="https://akwam.ahmedhassan165.repl.co"
			url2=requests.get(ahmed_link).status_code
			return url2
		except:
			return "error"
	ahmed()
	
	link="https://spam.qwerfree.repl.co"+"==>  "+str(spam())
	
	link2="https://akwam.ahmedhassan165.repl.co"+"==>  "+str(ahmed())
	
	return render_template_string('''
	<center>
	{}<br><br>
	{}
	</center>
	'''.format(link,link2))
	
	

if __name__=="__main__":
	app.run(debug=True,port=5000)


