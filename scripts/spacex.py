#!/usr/bin/env python
import requests
import json
import datetime


response = requests.get("https://api.spacexdata.com/v4/launches/next")

data = json.loads(response.content)

mission_name=data["name"]
date_utc=data["date_utc"]
date_precision=data["date_precision"]

date_time_obj = datetime.datetime.strptime(date_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
date_formatted=date_time_obj.strftime("%A the %d")
hour_formatted=date_time_obj.strftime("%H %M %p")



n=date_time_obj.strftime("%d")
suffix = { 1: "st", 2: "nd", 3: "rd" }.get(n if (int(n) < 20) else (int(n) % 10), 'th')


if "hour" in date_precision:
	msg= f"The next launch is {mission_name} on {date_formatted} at {hour_formatted}"
else:
	msg= f"The next launch is {mission_name} on {date_formatted}{suffix}"

print(msg)
