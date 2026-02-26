# Install the following packages: flask, requests, geopy
# Windows:   py -m pip install <package>
# Mac/Linux: pip3 install <package>

from flask import Flask, request, render_template
import requests
from geopy.geocoders import Nominatim

app = Flask(__name__)
geoapp = Nominatim(user_agent="wx")

@app.route('/', methods=["GET"])
def index():
    return "Hello World"

# API Calls:
#    1) Get Latitude/Longitude from City, State:
#       location = geoapp.geocode(citystate).raw
#       print(location["lat"], location["lon"])
#    2) Get Forecast Zone for Latitude and Longitude:
#       https://api.weather.gov/points/latitude,longitude
#       Zone Forecast HTML Request: result["properties"]["forecast"]    
#    3) Get Zone Forecast:
#       Forecast Details: result["properties"]["periods"]

@app.route('/weather', methods=["GET","POST"])
def weather():
    if request.method == 'POST':
        citystate = request.form.get("citystate")
        location = geoapp.geocode(citystate).raw
        zone = requests.get(f"https://api.weather.gov/points/{location["lat"]},{location["lon"]}").json()
        forecast = requests.get(zone["properties"]["forecast"]).json()
        return render_template('weather.html', wx=forecast["properties"]["periods"], location=f"{citystate.upper()} ({location["lat"]}, {location["lon"]})")
    return render_template('weather.html', wx = [], location = None)
    
if __name__ == "__main__":
    app.run()