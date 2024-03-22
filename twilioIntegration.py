from twilio.rest import Client
import os

def twilioIntegration(Message):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+18449682334',
    body=Message,
    to='+18777804236'
    )

    print(message.sid)