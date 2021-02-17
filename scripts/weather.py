#!/usr/bin/env python
import requests
import json
import sys
from geopy.geocoders import GoogleV3

arg = os.environ.get('IRCCAT_ARGS')
loc = ''.join(e for e in arg if e.isalnum())
if len(loc) > 0:
    geolocator = GoogleV3(api_key='keygoeshere')
    location = geolocator.geocode(loc, language='en')
    if location != None:
        coords = str(location.latitude) + "," + str(location.longitude)
        url = "https://api.forecast.io/forecast/d893c4af044563aed2283d7dc40e2d63/" + coords + "?units=uk"
        response = requests.get(url)
    else:
        print ("No location!" , location)
        raise SystemExit       
else:    
    response = requests.get('https://api.forecast.io/forecast/d893c4af044563aed2283d7dc40e2d63/51.531801,-0.060318?units=uk')

data = json.loads(response.content)
 

current_summary = data['currently']['summary']
temp_c = data['currently']['temperature']
temp_f = (temp_c * 9.0 / 5) + 32
app_temp_c = data['currently']['apparentTemperature']
app_temp_f = (app_temp_c * 9.0 / 5) + 32
humidity = data['currently']['humidity']
wind_bearing = data['currently']['windBearing']
wind_compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N'][int(wind_bearing / 45.0 + 0.5)]
wind_speed = data['currently']['windSpeed']
minute_summary = data['minutely']['summary']
day_summary = data['daily']['summary']
        
feels_like = ''
if app_temp_c != temp_c:
    feels_like = u' (feels like %.1f\u00b0)' % (
        app_temp_c,
    )
            
msg = u'Currently %.1f\u00b0C%s, humidity %s%%, wind: %s at %.0fmph. %s %s' % (
    temp_c,     
    feels_like, 
    int(humidity * 100),
    wind_compass,
    wind_speed,     
    minute_summary,
    day_summary,
)
print (msg.encode('utf-8'))