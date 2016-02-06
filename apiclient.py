import requests
#apiclient to test POST
url = 'http://localhost:5000/api/'

data = {"line" : "1", "string" : "lol"}
response = requests.post(url, json=data)
print response.status_code
print response.text