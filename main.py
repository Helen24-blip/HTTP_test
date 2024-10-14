import requests
import pprint

params = {'q': 'HTML'}
response = requests.get('https://api.github.com/search/repositories', params=params)

print("Статус-код:", response.status_code)

json_response = response.json()
pprint.pprint(json_response)

print(f"Количество репозиториев с использованием HTML: {json_response['total_count']}")

