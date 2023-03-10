import smtplib
import datetime as dt
import random

### Check .env for user info ###
my_email = ""
password = ""

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:

    connection.starttls()

    connection.login(user=my_email, password=password)



    now = dt.datetime.now()
    year = now.year
    day = now.day
    month = now.month
    day_of_week = now.weekday()
    # print(day_of_week)

    with open("quotes.txt", "r") as quotes:
        data = quotes.read()
        quotes_list = data.split("\n")
        ## can also use readlines() ##
        
        
        if day_of_week == 4:
            random_quote = random.choice(quotes_list)
            connection.sendmail(from_addr=my_email, to_addrs="frozzel@me.com", msg=f"Subject: Happy Friday!\n\n{random_quote}")