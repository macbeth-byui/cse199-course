# Training G - Flask Web Applications

## Background

* A web application contains both a front-end and a back-end.  The front-end is what you see on the web browser.  The back-end runs on a remote server and does all of the processing needed to dynamically display data in the front-end.

* A back-end can interact with API's, databases, and other libraries to obtain data, change data, or analyze data.  The back-end can also manage user authorizations.

* There are many web application frameworks:
  * JavaScript/TypeScript - Express, , React, Angular
  * Python: Django, Flask
  * Rust: Actix Web, Rocket
  * C#: ASP.Net

* Web app frameworks handle multiple tasks making it easier for the programmer:
  * Routing of GET/POST requests
  * Rendering of HTML outputs using template language which connects data from the code with the HTML tags
  * Handling of Error Conditions (ex: 404 - Not Found, 500 - Internal Server Error)

* Flask has a very simple framework setup:
  * To create a flask app:
  
    ```python
    app = Flask(__name__)
    ```

  * To connect a route to a function:

    ```python
    @app.route('/', methods=["GET"])
    def index():
        return "Hello World"
    ```

  * To generate an HTML response:

    ```python
    first = "Bob"
    last = "Smith"
    return render_template('hello.html', first_name = first, last_name = last)
    ```

  * To add data variables to HTML (found in the `templates` folder):

    ```html
    <b>Hello {{first_name}} {{last_name}}<\b>
    ```

  * To add controls to HTML:

    ```html
    {% if first_name == "Bob" %}
        <b>Hi Bob!</b>
    {% endif %}
    {% for letter in last_name %}
        <b>{{letter}}</b>
        <p>
    {% endfor %}
    ```

## Example

1. Copy the following code into a file called `main.py`:

```python
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
```

1. Create a folder called `templates`.  Copy the following code and put into a file called `weather.html` inside the `templates` folder:

```html
<!doctype html>
<html lang="en">
<head>
  <title>Weather Forecast</title>
  <style>
    table, th, td {
      border: 1px solid black;
      text-align: center
    }
  </style>
</head>
<body>
  <h1>Weather Forecast</h1>

  <form action="/weather" method="POST">
    <Label>City, State: </Label>
    <input name="citystate"/>
    <button type="submit">Get Forecast</button>
  </form>


    <h2>Forecast for </h2>
    <table>
      <tr>
        <th>Period</th>
        <th>Temp (F)</th>
        <th>Wind Direction</th>
        <th>Wind Speed</th>
        <th>Precip Prob</th>
        <th>Forecast</th>
      </tr>

        <tr>
          <td><p><img src=""/></td>
          <td></td>
          <td></td>
          <td></td>
          <td>%</td>
          <td></td>
        </tr>

    </table>


</body>
</html>
```

1. Create a Flask application.

1. Create a route for the web server root (`http://127.0.0.1:5000/`) that will display `Hello World`.  Run the server and test it with a web browser.

1. Create a route for the weather app (`http://127.0.0.1:5000/weather/`)

1. Use the `geopy` app to convert the city and state submitted by the HTML form to latitude and longitude.

1. Use the `https://api.weather.gov/points/` API to get the NWS zone from the latitude and longitude.

1. Use the forecast link in the zone response to get the forecast details.

1. Pass the forecast details to the HTML.  Use tags to display the forecast (only if data was read from the API calls)

## Discussion

What web frameworks could you use in your project?  What is the benefit of using a web framework?

## Solution

* [main.py](main.py)
* [templates/weather.html](weather.html)
