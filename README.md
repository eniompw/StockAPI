# Python Stock API

* [Finnhub example.py](https://github.com/eniompw/stockAPI/blob/main/finnhub-example.py)

      import requests
      r = requests.get("https://finnhub.io/api/v1/quote?symbol=AAPL&token=")
      dict = r.json()
      print(dict['c'])

* [CS50 Yahoo Finance example](https://github.com/eniompw/StockAPI/blob/main/cs50-lookup.py)

### Ref:
* [requests](https://www.w3schools.com/python/ref_requests_response.asp)
* [finnhub.io quote](https://finnhub.io/docs/api/quote)
* [CS50 Finance lookup](https://cdn.cs50.net/2024/x/psets/9/finance/helpers.py?highlight)
