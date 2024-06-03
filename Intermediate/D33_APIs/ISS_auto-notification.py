import requests
import datetime as dt
import smtplib
import time

#pittsburgh lat and long
MY_LAT = 40.440624
MY_LONG = -79.995888
FORMATTED = 0
MY_EMAIL = "amoghborikartest@gmail.com"
MY_PASSWORD = "dummy_password"

# if ISS is overhead
def is_iss_overhead():
    # ISS data API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_lng <= MY_LONG+5:
        return True

# check if it is night time
def is_night():
    #My location API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": FORMATTED
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data =  response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up 👆🏻\n\nThe ISS is above you in the sky!"
        )

