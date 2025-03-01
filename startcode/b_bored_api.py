import requests
response = requests.get('https://bored.api.lewagon.com/api/activity')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('error')
