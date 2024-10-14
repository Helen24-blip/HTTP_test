import requests
import pprint

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

print("Статус-код:", response.status_code)

json_response = response.json()
pprint.pprint(json_response)
