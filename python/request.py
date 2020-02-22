import requests

response = requests.get('https://vk.ru')

print(response.text)