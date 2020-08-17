'''
Module for requests to open weather API
'''
import requests

'''
returns the response for openweather queried for Montreal as the city
'''
def request():
    return requests.get("http://api.openweathermap.org/data/2.5/weather?q=Montreal&appid=9ee255b8e671643ab089e28c1ef7a303").json()

'''
takes as input a city name and returns the openweather response for that city
'''
def requestCity(name):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=9ee255b8e671643ab089e28c1ef7a303"
    url = url.format(name)
    return requests.get(url).json()