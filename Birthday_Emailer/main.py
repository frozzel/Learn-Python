import datetime as dt
import pandas as pd
import random
import smtplib

my_email = ""
password = ""

#--------------------------Check todays Date------------------------#
now = dt.datetime.now()
day = now.day
month = now.month
today = (month,day)

#-----------------------Compare it to Birthdays---------------------#
data = pd.read_csv('birthdays.csv')
birth_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows() }
if (today in birth_dict):
    birth_person = birth_dict[today]
    fpath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(fpath) as letter_file:
        contents = letter_file.read()
        new_content = contents.replace("[NAME]", birth_person["name"])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=birth_person.email, 
                            msg=f"Subject: Happy Birthday!\n\n{new_content}")
        

