import requests
headers = {"Content-Type": "application/json"}
#response = requests.get("https://zenodo.org/api/records/7712947",  headers=headers)

responseList = requests.get('https://zenodo.org/api/records', params={'type': 'publication', 'size': 5000, 'page': 4}) 


#los ids son los numeros del doi

try:
    print(len(responseList.json()["hits"]["hits"]))
except:
    print(responseList.json())

#print(len(responseList.json()))

#print(responseList.json())