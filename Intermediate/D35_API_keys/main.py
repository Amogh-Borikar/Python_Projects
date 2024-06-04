import requests
from twilio.rest import Client

account_sid = '__Twilio-Account-SID__'
auth_token = '__Twilio-auth-token__'
API_KEY = "__OPEN-WEATHER-MAP-API-KEY__"

parameters = {
    "lat": 20.844912,
    "lon": 106.688087,
    "appid": API_KEY,
    "cnt": 5
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='__twilio-number__',
    body='It is going to rain today, bring and ☂️',
    to='__personal-number__'
    )

    print(message.status)