import requests

request = requests.get('https://official-joke-api.appspot.com/random_joke')
tekst = request.text
print(tekst)