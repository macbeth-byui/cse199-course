# Install the following packages: flask, requests, geopy
# Windows:   py -m pip install <package>
# Mac/Linux: pip3 install <package>

from flask import Flask, request, render_template
import requests
from geopy.geocoders import Nominatim

app = None
geoapp = Nominatim(user_agent="wx")

def index():
    pass


# API Calls:
#    1) Get Latitude/Longitude from City, State:
#       location = geoapp.geocode(citystate).raw
#       print(location["lat"], location["lon"])
#    2) Get Forecast Zone for Latitude and Longitude:
#       https://api.weather.gov/points/latitude,longitude
#       Zone Forecast HTML Request: result["properties"]["forecast"]    
#    3) Get Zone Forecast:
#       Forecast Details: result["properties"]["periods"]

def weather():
    pass

if __name__ == "__main__":
    app.run()