import requests
from requests.auth import HTTPBasicAuth
from dotenv import dotenv_values
from datetime import datetime

GENDER= dotenv_values(".env")["GENDER"]
WEIGHT_KG= dotenv_values(".env")["WEIGHT_KG"]
HEIGHT_CM= dotenv_values(".env")["HEIGHT_CM"]
AGE= dotenv_values(".env")["AGE"]

APP_ID= dotenv_values(".env")["APP_ID"]
API_KEY= dotenv_values(".env")["API_KEY"]
USER= dotenv_values(".env")["USER"]
PASS= dotenv_values(".env")["PASS"]


basic= HTTPBasicAuth(USER, PASS)

exercise_text = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/4405a332b998aff756b6487fee262faf/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
 "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

res = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = res.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_res = requests.post(sheety_endpoint, json=sheety_params, auth=basic)