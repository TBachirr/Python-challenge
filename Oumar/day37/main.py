import requests
from datetime import datetime

PIXELA_TOKEN = "1234567890"
PIXELA_USERNAME = "oumdji"
PIXELA_GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{PIXELA_GRAPH_ID}"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

pixel_config = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": 10
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)

update_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{PIXELA_GRAPH_ID}/{pixel_config['date']}"

update_config = {
    "quantity": "40"
}

response = requests.put(url=update_endpoint, headers=headers, json=update_config)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{PIXELA_GRAPH_ID}/{pixel_config['date']}"

delete_config = {
    "date": datetime.now().strftime("%Y%m%d"),
}

response = requests.delete(url=delete_endpoint, headers=headers, json=delete_config)
print(response.text)

