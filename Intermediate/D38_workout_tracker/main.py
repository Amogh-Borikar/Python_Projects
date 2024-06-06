import requests
import datetime as dt

WEIGHT_KG = 80
HEIGHT_CM = 180
AGE = 26

APP_ID = "_DUMMY_"
API_KEY = "_DUMMY_"

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/_DUMMY_"

exercise_text = input("Which exercises did you perform: ")


header = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
  }

API_CONFIG = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
  }

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=API_CONFIG, headers=header)
data = response.json()
exercises_list = data['exercises']

today = dt.datetime.now()
workout_date = today.strftime("%Y/%m/%d")
workout_time = today.strftime("%H:%M:%S")
print(workout_date)
print(workout_time)
for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": str(workout_date),
            "time": str(workout_time),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
    print(sheety_response.text) 