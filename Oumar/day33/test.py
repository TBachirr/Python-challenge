import requests
import datetime as dt
import smtplib
import time

LAT = 38.907192
LNG = -77.036870
PARAMS = {"lat": LAT, "lng": LNG, "formatted": 0}
EMAIL = "rd144103@gmail.com"
PASSWORD = "ugbh qulb ikez cuwi"


now = dt.datetime.now()

def send_mail():
    time.sleep(60)n
    while True:
        iss_response = requests.get("http://api.open-notify.org/iss-now.json").json()
        sunrise_response = requests.get("http://api.sunrise-sunset.org/json", params=PARAMS).json()
        sunrise = sunrise_response["results"]["sunrise"].split("T")[1].split(":")[0]
        sunset = sunrise_response["results"]["sunset"].split("T")[1].split(":")[0]
        iss_lats = iss_response["iss_position"]["latitude"]
        iss_longs = iss_response["iss_position"]["longitude"]

        my_location = (LAT, LNG)
        iss_location = (iss_lats, iss_longs)

        if iss_location == my_location and now.hour >= int(sunrise) and now.hour <= int(sunset):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg="Subject:Look up!\n\nThe ISS is above you in the sky."
                )

