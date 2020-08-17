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