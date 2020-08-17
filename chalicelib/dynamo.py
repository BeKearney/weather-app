'''
module for dynamodb funcitons for the weather-data table
'''
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather-data')

'''
gets a record from the table by id
'''
def get(id):
    response = table.get_item(Key={'time': id})
    return response['Item']

'''
takes as input the item id and the json data and inserts it in the table
'''
def put(id, data):
    table.put_item(
        Item={
            'time': id,
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'feel': round(data['main']['feels_like'] - 273),
            'high': round(data['main']['temp_max'] - 273),
            'humidity': data['main']['humidity'],
            'low': round(data['main']['temp_min'] - 273),
            'temp': round(data['main']['temp'] - 273),
            'weather': data['weather'][0]['main'],
        }
    )

