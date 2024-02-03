import requests
from datetime import datetime
import os

APP_ID = 'd0b75dcd'
API_KEY = 'ffd9dd13a5f056f72685a17476f554ba'
sheet_endpoint = 'https://api.sheety.co/d7d3a2b518511cb0571a8e129edd1462/copyOfMyWorkouts/workouts'
domain = 'https://trackapi.nutritionix.com'
end_point = '/v2/natural/exercise'

user_params = {
    'query': 'I ran 1 mile',
    'weight_kg': 55,
    'height_cm': 167,
    'age': 45
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response = requests.post(url=f'{domain}{end_point}', json=user_params, headers=headers)
result = response.json()
print(result)
print(APP_ID)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
