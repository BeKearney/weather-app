'''
Module for requests to open weather API
'''
import requests
import os

url = os.environ["url"] + "q={}&" + os.environ["api_key"]

'''
returns the response for openweather queried for Montreal as the city
'''
def request():
    return requests.get(url.format("Montreal")).json()

'''
takes as input a city name and returns the openweather response for that city
'''
def requestCity(name):
    return requests.get(url.format(name)).json()

'''
returns the response for a given url
'''
def requestUrl(address):
    return requests.get(address).json()

'''
returns parsed weather data for the specified city
'''
def requestCityParsed(name):
    data = requests.get(url.format(name)).json()
    Item={
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'feel': round(data['main']['feels_like'] - 273),
            'high': round(data['main']['temp_max'] - 273),
            'humidity': data['main']['humidity'],
            'low': round(data['main']['temp_min'] - 273),
            'temp': round(data['main']['temp'] - 273),
            'weather': data['weather'][0]['main'],
            'country': data['sys']['country']
        }
    return Item