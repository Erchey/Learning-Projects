import requests
from datetime import datetime
import smtplib

my_email = 'okpalatest@gmail.com'
my_password = 'akopkskunpepgbck'
MY_LAT = 6.488080  # Your latitude
MY_LONG = 3.334561  # Your longitude


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude >= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg='Subject:Look Overhead\n\nGo outside and look up!')
        #return True


if iss_overhead() and is_dark():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg='Subject:Look Overhead\n\nGo outside and look up!')


# If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
