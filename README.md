# Python Stock API

* [example.py](https://github.com/eniompw/stockAPI/blob/main/example.py)

      import requests
      r = requests.get("https://finnhub.io/api/v1/quote?symbol=AAPL&token=")
      dict = r.json()
      print(dict['c'])

### Ref:
* [requests](https://www.w3schools.com/python/ref_requests_response.asp)
* [finnhub.io quote](https://finnhub.io/docs/api/quote)
