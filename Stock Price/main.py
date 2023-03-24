import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API = ""
NEWS_API = ""
account_sid = ""
auth_token = ""


stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]['4. close']
daybefore_yesterday_data = data_list[1]['4. close']
difference = float(yesterday_data) - float(daybefore_yesterday_data)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
    
dif_percent = round((difference / float(yesterday_data)) * 100)


news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API,
    "pageSize": 3,
    "page": 1,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()["articles"]
three_articles = news_data[:3]

formatted_art = [f"{STOCK_NAME}: {up_down}{dif_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


if abs(dif_percent) > .1:
    for article in formatted_art:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                body=article,
                from_='',
                to=''
            )
        print(message.status)
        print(article)
 
else:
    print("No News")

