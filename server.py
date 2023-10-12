from flask import Flask

from threading import Thread

app=Flask("app")
@app.route("/")
def home():
	return "refresh"
	
def run():
	app.run(host="0.0.0.0",port=5000)
	
def refresh():
	t=Thread(target=run)
	t.start()