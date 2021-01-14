import requests
import twilio
from twilio.rest import Client
# get your => account_sid phone_number,auth_token,api_key from twilio
account_sid = "--------------"
phone_number = "-------------"
auth_token = "----------------------"
your_number = "provide a number to get notification"

latitude = 22.804565
longitude = 86.202873

Owm_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "--------------------"
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=Owm_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()
weather_data = data['hourly'][:12]
will_rain = False
for hour_data in weather_data:
    condition_data = hour_data['weather'][0]['id']
    if int(condition_data) < 900:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Cold weather",
        from_=phone_number,
        to=your_number
    )
    print(message.status)
