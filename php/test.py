import requests
data = requests.get(
    "api.php").json()
print(data)
