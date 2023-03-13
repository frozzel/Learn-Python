import requests
from datetime import datetime

MY_LAT = 33.748997
MY_LON = -84.387985

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =sunrise = data["results"]["sunset"].split("T")[1].split(":")[0]

print( sunrise, sunset)

time_now = datetime.now()
print(time_now.hour)
