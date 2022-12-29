from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	res= "welcome to your API"
	return res, 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/myfun",methods=["GET"])
def myfun():
	return

@app.route("/postfun",methods=["POST"])
def postfun():
	return

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080 ,debug=False)

