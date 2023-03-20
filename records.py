import requests
headers = {"Content-Type": "application/json"}
#response = requests.get("https://zenodo.org/api/records/7712947",  headers=headers)

responseList = requests.get('https://zenodo.org/api/records',
                       params={'type': 'publication'})


#los ids son los numeros del doi

print(responseList.json()["hits"]["total"])
#print(len(responseList.json()))

#print(responseList.json())