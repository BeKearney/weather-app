'''
module for dynamodb funcitons for the weather-data table
'''
import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather-data')

'''
gets a record from the table by id
'''
def get(id):
    response = table.get_item(Key={'time': id})
    return response['Item']

'''
gets the latest record from the table
'''
def getLatest():
    response = table.scan(Limit=1, Select='ALL_ATTRIBUTES', ConsistentRead=True)
    return response['Items'][0]

'''
takes as input the item id and the json data and inserts it in the table
'''
def put(id, data):
    ttl = int(id) + 432000
    table.put_item(
        Item={
            'time': id,
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'feel': round(data['main']['feels_like'] - 273),
            'high': round(data['main']['temp_max'] - 273),
            'humidity': data['main']['humidity'],
            'low': round(data['main']['temp_min'] - 273),
            'temp': round(data['main']['temp'] - 273),
            'weather': data['weather'][0]['main'],
            'TTL': str(ttl)
        }
    )