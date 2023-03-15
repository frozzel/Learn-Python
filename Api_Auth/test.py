import requests


END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = ""
LAT = 33.748997
LON = -84.387985
UNITS = "imperial"

params = {
    "lat": LAT,
    "lon": LON,
    "units": UNITS,
    "appid": API_KEY
}

response = requests.get(END_POINT, params=params)
response.raise_for_status()
data = response.json()

test = data["list"]
drill = test[0]["weather"]
description = drill[0]["description"]
id = drill[0]["id"]

if id < 800:
    print(f"Bring an Umbrella ☂️, the weather forcast is  '{description}'")
else:
    print(f"Weather Forcast '{description}'")