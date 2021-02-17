#!/usr/bin/env python
import requests
import json
import datetime
response = requests.get('https://api.spacexdata.com/v4/launches/next')

data = json.loads(response.content)

Mission_Name=data["name"]
date_utc=data["date_utc"]
date_time_obj = datetime.datetime.strptime(date_utc, '%Y-%m-%dT%H:%M:%S.%fZ')
date_formatted=date_time_obj.strftime("%c")
msg= "The next SpaceX launch is " + Mission_Name + " at the following date: " + date_formatted

print(msg)
