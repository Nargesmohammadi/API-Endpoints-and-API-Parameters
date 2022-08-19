"""API Key"""
import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = "b6352b3dca0e8a98600ef53301a56b89"

weather_params = {
    "lat": 29.6103,
    "lon": 52.5311,
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
    print("Bring an umbrella.")
# print(weather_data["hourly"][0]["weather"][0]["id"])
