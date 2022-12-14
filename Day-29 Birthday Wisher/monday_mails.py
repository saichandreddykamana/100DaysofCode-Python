import smtplib
import random
import datetime

EMAIL = "sender.one.bday.wisher@gmail.com"
PASSWORD = 'ntckfswypgpmjzvv'
RECEIVER = 'receiver.onebdaywisher@yahoo.com'

current_date = datetime.datetime.now()
current_day = current_date.weekday()
if current_day == 0:
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=RECEIVER, msg=random.choice(quotes))
