import requests
from dotenv import dotenv_values

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY =  dotenv_values(".env")["TEQUILA_API_KEY"]

