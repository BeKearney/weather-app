import requests

def request():
    return requests.get("http://api.openweathermap.org/data/2.5/weather?q=Montreal&appid=9ee255b8e671643ab089e28c1ef7a303").json()


def requestCity(name):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=9ee255b8e671643ab089e28c1ef7a303"
    url = url.format(name)
    return requests.get(url).json()