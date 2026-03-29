#!/usr/bin/env python
import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

data = json.loads(response.content)

price = data["bpi"]["GBP"]["rate"]

print(f"The Price of Bitcoin is £{price} damn high.")
