import requests
TOKEN = 'jd;ls;jdlj9o'
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': 'erchey',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/erchey/graphs'

graph_config = {
    ''
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/erchey/graphs/{GRAPH_ID}'
pixel_data = {
    'date': '20230130',
    'quantity': '9.7'
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
