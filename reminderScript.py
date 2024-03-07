import time
from datetime import datetime, timedelta
import requests

reminderSent = False  

def messageReminder(name, number, reminderDate):
    global reminderSent

    today = datetime.now()
    reminderDate = datetime.strptime(reminderDate, '%Y-%m-%d')

    if today.date() == reminderDate.date() and not reminderSent:
        resp = requests.post('http://textbelt.com/text', {
            'phone': number,                                            # number
            'message': f'Hello {name}! Reminder to PAY your CREDIT :)', # message
            'key': 'textbelt'
        })

        print(resp.json())

        reminderSent = True

        tomorrow = today + timedelta(days=1)
        sleep_time = (tomorrow - today).total_seconds()
        time.sleep(sleep_time)

def main():
    while True:
        # user input 
        name = input("Enter your name: ")
        number = input("Enter your phone number: ")
        reminderDate = input("Enter the reminder date (YYYY-MM-DD): ")

        messageReminder(name, number, reminderDate)

if __name__ == "__main__":
    main()
