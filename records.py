import requests
response = requests.get("https://zenodo.org/api/records/2790418")
print(response.json())
