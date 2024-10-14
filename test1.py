import requests
import pprint

params = {'userId': 1}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

print("Статус-код:", response.status_code)

json_response = response.json()
pprint.pprint(json_response)
