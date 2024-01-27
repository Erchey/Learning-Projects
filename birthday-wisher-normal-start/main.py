##################### Normal Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random


MY_EMAIL = 'okpalatest@gmail.com'
MY_PASSWORD = 'akopkskunpepgbck'
smtp_server = 'smtp.gmail.com'
smtp_port = 465

wish_file = random.randint(1, 3)

today_month = dt.datetime.today().month
today_day = dt.datetime.today().day
today_tuple = (today_month, today_day)

data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]['name']
    file_path = f'letter_templates/letter_{wish_file}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login to the SMTP server
#

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f'Subject:Happy Birthday!!\n\n{contents}')
    print('Email sent successfully!')


