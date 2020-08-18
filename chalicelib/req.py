'''
Module for requests to open weather API
'''
import requests
import os
import xmltodict
import json

url = os.environ["url"] + "q={}&" + os.environ["api_key"]

'''
returns the response for openweather queried for Montreal as the city
'''
def request():
    return requests.get(url.format("Montreal")).json()

'''
returns the response for openweather queried for the specified city as XML
'''
def requestXML(city):
    xml = url + "&units=metric&mode=xml"
    return requests.get(xml.format(city)).text

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
returns parsed weather data for the specified city from xml
'''
def requestCityParsed(name):
    try:
        data = xmltodict.parse(requestXML(name))['current']
        print(data['temperature']['@value'])
        print(type(data['temperature']['@value']))
        Item={
            'city': data['city']['@name'],
            'description': data['weather']['@value'],
            'icon': data['weather']['@icon'],
            'feel': round(int(float(data['feels_like']['@value']))),
            'high': round(int(float(data['temperature']['@max']))),
            'humidity': data['humidity']['@value'],
            'low': round(int(float(data['temperature']['@min']))),
            'temp': round(int(float(data['temperature']['@value']))),
            'country': data['city']['country']
        }
    except:
        return requestCityParsed('Montreal')
    return Item
