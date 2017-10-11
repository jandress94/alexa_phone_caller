from twilio.rest import Client

account_sid = "AC284875795ba9b598a3adaf8f2cb3d537"
auth_token = "8c26341a4b6abf4f6431c6b66ad7e97a"
client = Client(account_sid, auth_token)

emmaNum="+16319747038"
jimNum="+18652083894"
twilioNum="+18656354700"

call = client.api.account.calls.create(to=emmaNum, from_=jimNum, url="http://f74aef1f.ngrok.io")

print(call.sid)
