import requests
from twilio.rest import Client
from details import *


weather_params = {
    'lat': 11.831098,
    'lon': 13.150967,
    'appid': API_KEY,
    'cnt': 4
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()['list']

will_rain = False

for weather in weather_data:
    condition_code = weather['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=from_number,
        to=recipient_number,
    )

    print(message.status)


