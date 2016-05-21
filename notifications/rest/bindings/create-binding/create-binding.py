# NOTE: This example uses the next generation Twilio helper library - for more
# information on how to download and install this version, visit
# https://www.twilio.com/docs/libraries/python
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
token = "{{ auth_token }}"
client = Client(account, token)

service = client.notifications.v1.services("ISxxx")

binding = service.bindings.create(endpoint="xxx", identity="bob", binding_type="gcm", address ="xxx", tag="premium")

print binding