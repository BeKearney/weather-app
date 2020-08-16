from chalice import Chalice, Rate
import requests
import boto3
import time
import json

app = Chalice(app_name='weather-app')

'''
Return Weather Data for Montreal
'''
@app.route('/')
def index():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Montreal&appid=9ee255b8e671643ab089e28c1ef7a303")
    data = response.json()
    return data
'''
Return Weather Data for the City defined in the Route
'''
@app.route('/{city}')
def weatherByCityName(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=9ee255b8e671643ab089e28c1ef7a303"
    url = url.format(city)
    response = requests.get(url)
    data = response.json()
    return data
'''
Uploads curent weather data to S3 every minute
'''
@app.schedule(Rate(5, unit=Rate.MINUTES))
def periodic_task(event):
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Montreal&appid=9ee255b8e671643ab089e28c1ef7a303")
    data = response.json()
    name = str(round(time.time()))

    s3 = boto3.client('s3')
    f = open("weatherdata", "w")
    f.write(json.dumps(data))
    f.close()

    try:
        s3.upload_file("weatherdata", "weather-app-data", name)
        return {"Success": "True"}
    except:
        return {"Success": "False"}

@app.route('/testS3')
def test_S3():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Montreal&appid=9ee255b8e671643ab089e28c1ef7a303")
    data = response.json()
    name = str(round(time.time()))

    s3 = boto3.client('s3')
    f = open("weatherdata", "w")
    f.write(json.dumps(data))
    f.close()

    try:
        s3.upload_file("weatherdata", "weather-app-data", name)
        return {"Success": "True"}
    except:
        return {"Success": "False"}
