"""API Key"""
import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = "6d238a4999ad9329c7da25f1196c3933"

weather_params = {
    "lat": 29.6103,
    "lon": 52.5311,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = (response.json())
