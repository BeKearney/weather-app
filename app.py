from chalice import Chalice
import requests

app = Chalice(app_name='weather-app')

@app.route('/')
def index():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Montreal&appid=9ee255b8e671643ab089e28c1ef7a303")
    data = response.json()
    return data

@app.route('/{city}')
def weatherByCityName(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=9ee255b8e671643ab089e28c1ef7a303"
    url = url.format(city)
    response = requests.get(url)
    data = response.json()
    return data

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
