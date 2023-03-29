from twilio.rest import Client
from dotenv import dotenv_values

TWILIO_SID = dotenv_values(".env")["TWILIO_SID"]
TWILIO_AUTH_TOKEN = dotenv_values(".env")["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = dotenv_values(".env")["TWILIO_VIRTUAL_NUMBER"]
TWILIO_VERIFIED_NUMBER = dotenv_values(".env")["TWILIO_VERIFIED_NUMBER"]

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)