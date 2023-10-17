import requests
r = requests.get("https://finnhub.io/api/v1/quote?symbol=AAPL&token=")
dict = r.json()
print(dict['c'])
