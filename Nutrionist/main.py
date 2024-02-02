import requests
from datetime import datetime
import os

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
sheet_endpoint = os.getenv('SHEET_ENDPOINT')

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
