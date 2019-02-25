from django.test import TestCase

# Create your tests here.

import requests, json
url = 'http://127.0.0.1:8000/login/'
parmas = {
    "username": "admin36",
    "password": "admin36"
}
response = requests.post(url, data=parmas)
re_dict = json.loads(response.text)
print('------------re_dict: ', re_dict)