import datetime
import json
import requests
import time

HOUR_LIMIT_JSON = json.loads("{\"message\": \"2000 per 1 hour\", \"status\": \"429\"}")
MIN_LIMIT_JSON = json.loads("{\"message\": \"60 per 1 minute\", \"status\": \"429\"}")
ZENODO_SIZE_LIMIT=10000


publications = []
date = datetime.date(2009, 12, 31)
week_delta = datetime.timedelta(days=7)
first_rqt_time= datetime.datetime.now().time()

while date < datetime.date.today():

    start_date = date
    end_date = date + week_delta

    responseList = requests.get('https://zenodo.org/api/records', params={'type': 'publication', 'q': f'publication_date:[{start_date} TO {end_date}]', 'size': ZENODO_SIZE_LIMIT})

    try:
        print(f"Trying {start_date} - {end_date}.")
        if len(responseList.json()['hits']['hits']) < ZENODO_SIZE_LIMIT:
            print(f"{len(responseList.json()['hits']['hits'])} publications found.")  
            publications.extend(responseList.json()['hits']['hits'])
    
        else:
            print(f"Week {start_date} - {end_date} have more than {ZENODO_SIZE_LIMIT} records.Performing daily queries...")
            day_delta = datetime.timedelta(days=1)
            current_date = start_date
            while current_date <= end_date:
                print(f"Trying {current_date}.")
                responseList = requests.get('https://zenodo.org/api/records', params={'type': 'publication', 'q': f'publication_date:{current_date}', 'size': ZENODO_SIZE_LIMIT})
                print(f"{len(responseList.json()['hits']['hits'])} publications found.") 
                if len(responseList.json()['hits']['hits']) >= ZENODO_SIZE_LIMIT:
                    print(f"Day {current_date} have more than {ZENODO_SIZE_LIMIT} records. Data will be lost")
                publications.extend(responseList.json()['hits']['hits'])
                current_date += day_delta
        date += week_delta+datetime.timedelta(days=1)
    except:
        if responseList.json()==MIN_LIMIT_JSON:
            time.sleep(50)
        elif responseList.json()==HOUR_LIMIT_JSON:
             remaining_time = datetime.timedelta(hours=1)-first_rqt_time
             print( f"Request limit per hour reached, the process will sleep{remaining_time}")
             time.sleep(remaining_time)
             first_rqt_time= datetime.datetime.now().time()


   

  
   

print(f"Se encontraron {len(publications)} publicaciones.")    
