from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	resp = VoiceResponse()
	resp.say("Hello Emma! This is a message from Jim.")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
