import requests
import asyncio


def getData():
    response = requests.get(f'https://freetestapi.com/api/v1/countries')
    return response   
response = getData()
print(response)
data = response.json()
print(data)
print(type(data))
