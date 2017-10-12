from twilio.rest import Client
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read("lambda.config")
account_sid = config.get("Twilio API", "account_sid")
auth_token = config.get("Twilio API", "auth_token")
twilio_script_url = config.get("Twilio API", "script_url")
client = Client(account_sid, auth_token)

emmaNum="+16319747038"
jimNum="+18652083894"
twilioNum="+18656354700"

call = client.api.account.calls.create(to=emmaNum, from_=jimNum, url=twilio_script_url)

print(call.sid)
