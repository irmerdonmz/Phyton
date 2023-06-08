import requests
import json
import jsonpath

#API url
url = "https://api.punkapi.com/v2/beers/8"

#1.Send GET request
response = requests.get(url)
print(response)

#verify status code 200
response.status_code
print(response.status_code)
assert response.status_code == 200

#verify name
print(response.json()[0]['name'])
assert response.json()[0]['name'] == "Fake Lager"

#verify abv
print(response.json()[0]['abv'])
assert response.json()[0]['abv'] == 4.7

#2.Send DELETE request
response2 = requests.delete(url)
print(response2)

#verify DELTE request status code
assert response2.status_code == 404
print(response2.status_code)

#verify DELETE message
print(response2.json()['message'])
assert response2.json()['message'] == "No endpoint found that matches '/v2/beers/8'"