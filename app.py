#pylint:disable=W0123
import json,requests

from flask import  Flask,render_template_string,request
app=Flask(__name__)
@app.route("/")
def home():
	file=open("file_url.text","r")
	x=(file.read())
	file_list=x.splitlines()
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
	
	""".format(file_list))
	
@app.route("/send",methods=["GET"])
def sh():
	data=request.args.get("url")
	url="http://" in data or "https://" in data
	if data=="" or url==False :
		return "error"
	else:
			file=open("file_url.text","a")
			file.write(str(data+"\n"))
			return "success"

@app.route("/data")
def rea():
	file=open("file_url.text","r")
	x=(file.read())
	a=x.splitlines()
	li=[]
	for i in a:
		res=requests.get(i).status_code
		li.append(res)
	return li

	
@app.route("/delete")
def delte():
	file=open("file_url.text","r")
	d=file.read()
	file_list=d.splitlines()
	return render_template_string("""
	<center><br><br>
	{}
	<br><br>
	<form method="get" action="/del" >
	<input style="width: 40%;height: 0,3%;" type="text" name="del" placeholder="enter url Delete"><br><br>
	<button type="submit">submit</button>
	</form><br><br>
	
	
	""".format(file_list))
@app.route("/del",methods=["GET"])
def dele():
	delete=request.args.get("del")
	
	def delete_line(line_number):
	  
	  # opens the file, reads and stores each line into a list
	  with open("file_url.text") as file:
	    lines = file.readlines()
	  
	  # if the line number is in the file, we can delete it
	  if (line_number <= len(lines)):
	  
	    # delete the line from the list, which will be at line_number - 1 because 
	    # lists are zero-indexed in Python
	    del lines[line_number - 1]
	    
	    # open the file for writing with "w" which will make the file blank
	    with open("file_url.text", "w") as file:
	
	      # write as the new content of the file, the remaining lines in the list
	      for line in lines:
	        file.write(line)
	  
	  # if the line number exceeds the length of the file, output an error message
	  else:
	    
	    # inform the user the line is not in the file, and how many lines there is
	    print("Line", line_number, "not in file.")
	    print("File has", len(lines), "lines.")
	
	
	# prompt the user for the filename and line number
	#delete_line_number = int(input("Line: "))
	
	# call the delete_line function to delete the line at that line number from 
	# the file with that filename
	delete_line(int(delete))

	return "success delete"
if __name__=="__main__":
	app.run(debug=True,port=5000)


