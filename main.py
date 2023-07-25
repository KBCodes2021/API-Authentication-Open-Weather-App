import requests
#install twilio
import os
from twilio.rest import Client

OMW_Endpoint = "http://api.openweathermap.org/data/2.5/weather"
# How to declare API in project:
api_key = os.environ.get("OMW_API_KEY")
account_sid = ""
auth_token = ""

coord = {
    "lat": 51,
    "lon": 0,
    "appid": api_key
}

response = requests.get(OMW_Endpoint, params=coord)

# If get 200 or good response from server
response.raise_for_status()
weather_data = response.json()
print(weather_data)
# Copy the output and put it into the JSON viewer https://jsonviewer.stack.hu/
wind_speed = weather_data["wind"]["speed"]
# To get the wind speed value, do a value check if wind strong do this

# Used twilio SMS to send text if windy
if wind_speed > 1:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="",
        from_="",
        to=""
    )
print(message.status)


