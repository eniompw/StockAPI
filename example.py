import requests
res = requests.get("https://finnhub.io/api/v1/quote?symbol=AAPL&token=")

import json
dict = json.loads(res.text)
print(dict['c'])
