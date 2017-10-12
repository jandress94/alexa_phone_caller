from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	resp = VoiceResponse()
	msg = request.args['message'] if 'message' in request.args else "Hello, this is the default message."
	resp.say(msg)

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
