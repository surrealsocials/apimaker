

from flask import Flask,Response,request
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

print(gimage('hello'))


app = Flask(__name__)

@app.route("/")
def index():
	res= "welcome to your API"
	return res, 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/getfun",methods=["GET"])
def getfun():
	args1 = request.args['text']
	return gimage(args1), 200, {"Access-Control-Allow-Origin": "*"}
	

@app.route("/postfun",methods=["POST"])
def postfun():
	return

#if __name__ == '__main__':
app.run(host='0.0.0.0', port=8080, debug=False)

