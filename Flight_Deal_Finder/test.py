import requests
from requests.auth import HTTPBasicAuth
from dotenv import dotenv_values

USER= dotenv_values(".env")["USER"]
PASS= dotenv_values(".env")["PASS"]

basic= HTTPBasicAuth(USER, PASS)

sheety_endpoint= "https://api.sheety.co/4405a332b998aff756b6487fee262faf/flightDeals/users"

print("Welcome to Flight Club!")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?  ")
last_name = input("What is your last name?  ")
email1 = input("What is your email?  ")
email2 = input("Type your email again.")

if email1 == email2:
  new_data = {
        "user": {
            "firstname": first_name,
            "lastname": last_name,
            "email": email1
        }
    }
    
  
  res = requests.post(url=sheety_endpoint,  json=new_data, auth=basic)
  print("You're in the club!")
else:
    print("Emails didn't match!")
