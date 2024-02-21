# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6d4a7718b9c2e2ac42bf76f1e09b2662'
auth_token = "7b10b8c550c54be7cecb00dcdf37f06d"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+918796775539',
                        from_='+18145606374'
                    )

print(call)