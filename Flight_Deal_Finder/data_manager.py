import requests 
from requests.auth import HTTPBasicAuth
from dotenv import dotenv_values


USER= dotenv_values(".env")["USER"]
PASS= dotenv_values(".env")["PASS"]

basic= HTTPBasicAuth(USER, PASS)
sheety_endpoint= "https://api.sheety.co/4405a332b998aff756b6487fee262faf/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint, auth=basic)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                auth=basic
            )
            print(response.text)