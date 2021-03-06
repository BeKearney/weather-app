from chalice import Chalice, Rate, Response
from chalicelib import req, dynamo, jin
import boto3
import time
import json
import os
import xmltodict

app = Chalice(app_name='weather-app')
s3 = boto3.client('s3', region_name='ca-central-1')
bucket = os.environ["s3_bucket"]

'''
Return Website with most recent weather data for Montreal from Dynamo
'''
@app.route('/')
def index():
    context = {'data': dynamo.getLatest()}
    template = jin.render("chalicelib/templates/index.html", context)    
    return Response(template, status_code=200, headers={"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"})
'''
Return Latest Montreal Weather from Dynamo
'''
@app.route("/currentweather")
def current_weather():
    return dynamo.getLatest()
'''
Return Weather website for the City defined in the Route
'''
@app.route('/{city}')
def siteByCityName(city):
    context = {'data': req.requestCityParsed(city)}
    template = jin.render("chalicelib/templates/index.html", context)    
    return Response(template, status_code=200, headers={"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"})
'''
Return Weather Data for the City defined in the Route
'''
@app.route('/json/{city}')
def weatherByCityName(city):
    return req.requestCity(city)

@app.route('/xml')
def weatherXML():
    return xmltodict.parse(req.requestXML('Montreal'))
'''
Uploads curent weather data to S3 every minute
'''
@app.schedule(Rate(5, unit=Rate.MINUTES))
def periodic_task(event):
    data = req.request()
    name = str(round(time.time()))

    f = open("/tmp/weatherdata", "w")
    f.write(json.dumps(data))
    f.close()

    s3.upload_file("/tmp/weatherdata", bucket, name)
'''
Whenever weather data is uploaded to S3, insert it into dynamo DB
'''
@app.on_s3_event(bucket=bucket)
def file_uploaded(event):
    objName = event.key
    data = "{}"

    try:
        with open('/tmp/weatherdownload', 'wb') as f:
            s3.download_fileobj(bucket, objName, f)
    
        with open('/tmp/weatherdownload', 'r') as f:
            data = json.loads(f.read())
    except:
        app.log.error("error retrieving S3 data")
        data = '{"name":"Error retrieving data"}'


    dynamo.put(objName, data)