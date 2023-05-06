from twilio.rest import Client

import keys

client = Client(keys.account_side, keys.auth_token)

message = input("write the message which want you send .")
client.messages.create(body=message,
                       from_=keys.twilio_number,
                       to=keys.my_phone_number
                       )
