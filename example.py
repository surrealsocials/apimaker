from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "welcome to your API"

@app.route("/myfun",methods=["GET"])
def myfun():
	return

@app.route("/postfun",methods=["POST"])
def postfun():
	return

if __name__ == '__main__':
	app.run()

