import datetime as dt
import smtplib
import random

file = open("quotes.txt", "r")
quotes = file.read()
quotes_list = quotes.split("\n")
random_quote = quotes_list[random.randint(0, len(quotes_list)-1)]


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    email1 = "xyz@gmail.com"
    password1 = "***"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email1, password=password1)
        connection.sendmail(from_addr=email1, to_addrs="abc@yahoo.com", msg=f"Subject:Hello\n\n{random_quote}")
        connection.close()
