from twilio.rest import Client
import datetime as dt
import requests


weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "8639910cc89ef37d6390fa4ad15bb573"

from_number = "+15406607654"
to_number = "+886975505680"

now = str(dt.datetime.now()).split(" ")[0]
message = "今日天氣預報\n" + now + "\n"

weather_params = {
    "lat": 24.8066333,
    "lon": 120.9686833,
    "appid": api_key
}

response = requests.get(weather_endpoint, params=weather_params)
data = response.json()["list"]
today_weather = [day for day in data if day["dt_txt"].split(" ")[0] == now]

for i in today_weather:
    weather = i["weather"][0]["description"]
    time = i["dt_txt"].split(" ")[1][:5]

    message += time + " " + weather + "\n"

account_sid = "ACffcda66b1c47c83468df800b08ed955e"
auth_token = "9264e0b8ab025078ce556efa936c2b83"

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body=message,
        from_=from_number,
        to=to_number
    )

print(message.sid)
