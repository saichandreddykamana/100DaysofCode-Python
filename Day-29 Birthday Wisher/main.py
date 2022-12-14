import smtplib, datetime
import pandas as pd
import random

EMAIL = "sender.one.bday.wisher@gmail.com"
PASSWORD = 'ntckfswypgpmjzvv'

data = pd.read_csv('birthdays.csv')
data_dict = data.to_dict(orient="records")
current = datetime.datetime.now()
current_day = current.day
current_month = current.month
birthdays = [person for person in data_dict if person['month'] == current_month and person['day'] == current_day]
for person in birthdays:
    random_letter = random.randint(1, 3)
    with open(f'letter_templates/letter_{random_letter}.txt', 'r') as template:
        template_data = template.read()
        template_data = template_data.replace('[NAME]', person['name'])
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=person['email'], msg=template_data)





