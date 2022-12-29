from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	response= "welcome to your API"
	response.headers['Access-Control-Allow-Origin'] = '*'
	return response

@app.route("/myfun",methods=["GET"])
def myfun():
	return

@app.route("/postfun",methods=["POST"])
def postfun():
	return

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080 ,debug=False)

