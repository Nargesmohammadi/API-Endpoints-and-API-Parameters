"""API Key"""
import requests
from twilio.rest import Client

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = "b6352b3dca0e8a98600ef53301a56b89"
account_sid = ""
auth_token = ""

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
    message = client.messages.create(body="It's going to rain today. Remember to bring an ☔ 🌂 ", from_="",
                                     to="")
    print(message.status)
