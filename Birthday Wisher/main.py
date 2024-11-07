import smtplib
from random import *
import datetime as dt

my_email = "Write your email here"
password = "Write your password here"

quote_list = []

with open("quotes.txt", "r") as file:
    for line in file:
        quote_list.append(line.strip())

selected_quote = quote_list[randint(0, len(quote_list))]

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="Type email address here", msg=selected_quote)



