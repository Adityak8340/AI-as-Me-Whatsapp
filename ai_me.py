import time
import json
import requests
from gradio_client import Client
from datetime import datetime
from typing import Dict, Optional

class WhatsAppBot:
    # API Configuration
    WA_INSTANCE = "your green-api instance"
    WA_TOKEN = "your green-api token"
    BASE_URL = f"your green-api base url"
    ALLOWED_SENDER = "Recipient"
    TARGET_CHAT_ID = "{Recipient_WA_no}@c.us"
    POLL_INTERVAL = 1  # seconds

    def __init__(self):
        self.ai_client = Client("aadi8anant/Agent-47")  # Fine-tuned AI model from hugging-space
        self.last_message_time = datetime.now()

    def get_last_message(self) -> Optional[Dict]:
        """Fetch the last incoming message"""
        url = f"{self.BASE_URL}/lastIncomingMessages/{self.WA_TOKEN}"
        
        try:
            response = requests.get(url, data={"minutes": 0.1})
            response.raise_for_status()
            messages = response.json()
            
            if messages and len(messages) > 0:
                return messages[0]
            return None
            
        except requests.RequestException as e:
            print(f"Error fetching messages: {e}")
            return None

    def send_message(self, message: str) -> bool:
        """Send a message to WhatsApp"""
        url = f"{self.BASE_URL}/sendMessage/{self.WA_TOKEN}"
        
        payload = {
            "chatId": self.TARGET_CHAT_ID,
            "message": message,
            "linkPreview": True
        }
        
        try:
            response = requests.post(
                url, 
                json=payload, 
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return True
            
        except requests.RequestException as e:
            print(f"Error sending message: {e}")
            return False

    def get_ai_response(self, message: str) -> str:
        """Get response from AI model"""
        try:
            return self.ai_client.predict(
                message=message,
                api_name="/chat"
            )
        except Exception as e:
            print(f"Error getting AI response: {e}")
            return "Sorry, I couldn't process that request."

    def process_new_message(self, message_data: Dict) -> None:
        """Process a new incoming message"""
        sender_name = message_data.get('senderName')
        text_message = message_data.get('textMessage')
        message_time = datetime.fromtimestamp(message_data.get('timestamp', 0))

        # Check if message is newer than last processed message
        if message_time <= self.last_message_time:
            return

        self.last_message_time = message_time
        
        if sender_name == self.ALLOWED_SENDER and text_message:
            ai_response = self.get_ai_response(text_message)
            if ai_response:
                self.send_message(ai_response)

    def run(self):
        """Main bot loop"""
        print("WhatsApp Bot Started. Monitoring for messages...")
        
        while True:
            try:
                message_data = self.get_last_message()
                if message_data:
                    self.process_new_message(message_data)
                
                time.sleep(self.POLL_INTERVAL)
                
            except KeyboardInterrupt:
                print("\nBot stopped by user")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                time.sleep(self.POLL_INTERVAL)

if __name__ == "__main__":
    bot = WhatsAppBot()
    bot.run()