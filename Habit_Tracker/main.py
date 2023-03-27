import requests
from datetime import datetime

USERNAME=""
TOKEN=""
GRAPH_ID=""

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## visit https://pixe.la/@frozzel to see your graph
# https://pixe.la/v1/users/frozzel/graphs/graph1.html

# res = requests.post(url=pixela_endpoint, json=user_params)
# print(res.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
       "id": GRAPH_ID,
       "name": "Daily Workout",
       "unit": "min",
       "type": "int",
       "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(res.text)
today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
piixel_params = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many minutes did you workout today?")
}

res = requests.post(url=pixel_endpoint, json=piixel_params, headers=headers)
print(res.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "110"
}

# res = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(res.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# res = requests.delete(url=delete_endpoint, headers=headers)
# print(res.text)


