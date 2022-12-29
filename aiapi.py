
from flask import Flask,Response,request,send_file
import openai
openai.api_key = "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"


def gimage(args1):
	response = openai.Image.create(
		prompt=args1,
		n=1,
		size="512x512"
		)
	image_url = response['data'][0]['url']
	return image_url

app = Flask(__name__)

@app.route("/")
def index():
	res= "welcome to your API"
	return send_file("index.html"), 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/getfun",methods=["GET"])
def getfun():
	args1 = request.args['text']
	return gimage(args1), 200, {"Access-Control-Allow-Origin": "*"}
	

@app.route("/art.png",methods=["GET"])
def art():
	return send_file("art.png")


@app.route("/wheel.gif",methods=["GET"])
def wheel():
	return send_file("wheel.gif")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=False)

