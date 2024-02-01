import requests

APP_ID = 'd0b75dcd'
API_KEY = 'ffd9dd13a5f056f72685a17476f554ba'

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
print(response.text)
