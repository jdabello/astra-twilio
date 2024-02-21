import os
from dotenv import load_dotenv
from twilio.rest import Client
from uuid import uuid4

class TwilioHelper:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_number = os.getenv("TWILIO_NUMBER")
        self.status_callback_url = os.getenv("TWILIO_CALLBACK_URL")

        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, to_number, message_body):
        try:
            message = self.client.messages.create(
                from_=self.twilio_number,
                to=to_number,
                body=message_body,
                status_callback=self.status_callback_url
            )
            print(f"Message sent successfully! SID: {message.sid}")
            return message.sid
        except Exception as e:
            print(f"Error sending SMS: {e}")

