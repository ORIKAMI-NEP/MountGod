import requests
data = requests.get(
    "https://localhost:8080").json()
print(data)
