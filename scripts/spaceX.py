#!/usr/bin/env python
import requests
import json

response = requests.get('https://api.spacexdata.com/v4/launches/next')

data = json.loads(response.content)

Mission_Name= data["name"]
date_utc= data ["date_utc"]

msg= f"The next SpaceX launch is {Mission_Name} at the following date: {date_utc}"

print(msg)
