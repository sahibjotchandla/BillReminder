import time
from datetime import datetime
import requests

reminderSent = False  

def messageReminder():
    global reminderSent 
    today = datetime.now()

    if today.day == 4 and not reminderSent:
        resp = requests.post('http://textbelt.com/text', {
            'phone': 'XXX-XXX-XXXX', # Enter number
            'message': 'Hello _____! Reminder to PAY your CREDIT :)', # Enter message
            'key': 'textbelt'
        })

        print(resp.json())

        # Update flag
        reminderSent = True

        # Checks for time remaing on next day, sleeps accordingly
        tomorrow = today.replace(day=28)
        sleep_time = (tomorrow - today).total_seconds()
        time.sleep(sleep_time)

while True:
    messageReminder() # Run 
