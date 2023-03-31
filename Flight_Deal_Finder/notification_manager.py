from twilio.rest import Client
from dotenv import dotenv_values
import smtplib

TWILIO_SID = dotenv_values(".env")["TWILIO_SID"]
TWILIO_AUTH_TOKEN = dotenv_values(".env")["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = dotenv_values(".env")["TWILIO_VIRTUAL_NUMBER"]
TWILIO_VERIFIED_NUMBER = dotenv_values(".env")["TWILIO_VERIFIED_NUMBER"]
EMAIL_PROVIDER_SMTP_ADDRESS="smtp.gmail.com"
MY_EMAIL= dotenv_values(".env")["MY_EMAIL"]
MY_PASSWORD= dotenv_values(".env")["MY_PASSWORD"]

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
        
    def send_emails(self, emails, message, link):
            with smtplib.SMTP(host=EMAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                for email in emails:
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}".encode('utf-8')
                    )
                    print("Email sent to " + email)