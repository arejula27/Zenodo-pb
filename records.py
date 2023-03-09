import requests
headers = {"Content-Type": "application/json"}
response = requests.get("https://zenodo.org/api/records/7712947",  headers=headers)

#responseList = requests.get('https://zenodo.org/api/records',
 #                       params={"q":"geosapi: GeoServer REST API R Interface"})


#los ids son los numeros del doi


print(response.json())
#print(responseList.json())