import requests
import json

def getLocation():
    url = 'http://127.0.0.1:8000/api/v1/locations'
    response = requests.get(url)
    if(response.status_code == 200):
        return response.json()
print(getLocation())