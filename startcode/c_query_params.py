import requests
naam = input("wat is jouw naam: ")
response = requests.get(
    url=f"https://api.agify.io/",
    params={"name": naam}
)
if response.status_code == 200:
    data = response.json()
    leeftijd = ["age"]
    print(data["age"])
else:
    print(f"error code{response.status_code}")