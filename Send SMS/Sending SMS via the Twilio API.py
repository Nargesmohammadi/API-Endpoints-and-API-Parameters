"""API Key"""
import requests
from twilio.rest import Client
from twilio.http_client import TwilioHttpClient
import os

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWN_API_KEY")
account_sid = "AC19e0bea7c8b5961081ed0005ae89708d"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 46.947975,
    "lon": 19.458600,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = (response.json())
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an ☔ 🌂 ", from_="+19285978286",
                                     to="+989350880105")
    print(message.status)
