# https://www.twilio.com/docs

from twilio.rest import Client 
 
account_sid = '[Auth SID]' 
auth_token = '[Auth Token]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(from_='+12054795723', body='Hey there!!', to='phonenumber') 
 
print(message.sid)
