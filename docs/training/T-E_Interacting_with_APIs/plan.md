# Training E - JSON and File Based Storage

## Background

* In the same way that it is common to save JSON data to a file, it is also very common to retrieve JSON data from a remote server.

* An API server is a web server that receives HTTP requests (e.g. GET, POST) for information.  The information is sent back in the HTTP response with JSON data in the payload.  

* Some API servers cost money and/or require a secret key.  Make sure the file that contains your secret key is always placed in the `.gitignore` file.  However, many API's exist that are free and anonymous ot use.

* The `requests` library in Python makes it really easy to send HTTP requests, receive responses, and extract the JSON data.  To install, you need to use the Python module PIP (Pip Installs Packages):

  * Windows: `py -m pip install requests`
  * Mac\Linux: `pip3 install requests`

* To read data from a server, call the `get` function with your URL.  To extract the JSON data and convert it to a dictionary or list, use the `json` function.  You can then use loops and indexing to find the data that you desire.

```python
import requests

response = requests.get(api_url)
data = response.json()

print(data)
```

## Example

1. Copy the following code into a file called `main.py`:

```python
# URL for flights over Idaho:  
# https://opensky-network.org/api/states/all?lamin=41.988&lomin=-117.243&lamax=49.001&lomax=-111.043

# Guide for processing Airplane JSON data:
# https://openskynetwork.github.io/opensky-api/rest.html#flights-by-aircraft

print("Callsign Origin          Longitude  Latitude   Altitude (ft)   Velocity (mph)")
print("-------- --------------- ---------- ---------- --------------- --------------")

    # print(f"{callsign:<8} {origin:<15} {longitude:<10} {latitude:<10} {altitude:<15} {velocity:<14}")

```

1. Open the URL in the code using a Web Browser to see the JSON data.

1. Install the `requests` package.

1. Use the `requests` library to read the JSON data using the URL.  Print out the results.

1. Pull out the list of flights in the data.  Print out the results.

1. Loop through each flight.  Pull out the Callsign, Country of Origin, Longitude, Latitude, Barometric Altitude, and Velocity.  Ensure your variable names match with the print statement in the code.  

1. Convert the altitude from meters to feet by multiplying by 3.28084.  Convert the velocity to miles per hour by multiplying by 2.236936.  If necessary check to ensure that the altitude and velocity are not equal to None.

1. Search for the callsign on [https://www.flightaware.com/](https://www.flightaware.com/) to verify some of the planes.

## Discussion

What API's might be useful in your project?  If you can't think of any, what API might be useful to you in a future project?

## Solution

* [main.py](main.py)
