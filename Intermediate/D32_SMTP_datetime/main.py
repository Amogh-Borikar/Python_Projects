import smtplib
import datetime as dt
import random

MY_EMAIL = "my_mail_dummy@dumm.com"
MY_PASSWORD = "dummy_password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("Intermediate/D32_SMTP_datetime/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="awaleshruti0@gmail.com",
            msg=f"Subject:Motivation for you!\n\n{random_quote}"
        )














# import smtplib

# my_email = "amoghborikartest@gmail.com"
# my_password = "uluj dftt tgpv hheq"


