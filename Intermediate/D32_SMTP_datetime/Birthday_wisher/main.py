import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "my_mail_dummy@dumm.com"
MY_PASSWORD = "dummy_password"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("Intermediate/D32_SMTP_datetime/Birthday_wisher/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"Intermediate/D32_SMTP_datetime/Birthday_wisher/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )

