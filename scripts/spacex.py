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


if "hour" in date_precision:
	msg= f"The next launch is {mission_name} on {date_formatted} at {hour_formatted}"
else:
	msg= f"The next launch is {mission_name} on {date_formatted}"

print(msg)
