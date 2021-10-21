import requests
import json

URL = 'http://127.0.0.1:8000/student/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)

    req = requests.get(url=URL, data = json_data)

    data = req.json()
    print('data', data)

# get_data()

def post_data():
    data={'name': 'Ubaid', 'roll': 44, 'city': 'Lahore'}
    json_data = json.dumps(data)
    r = requests.post(url = URL , data = json_data)
    data = r.json()
    print('post data', data)

# post_data()

def update_data():
    data={'id': 1, 'name': 'Call me salman', 'city': 'Lahore'}
    json_data = json.dumps(data)
    r = requests.put(url = URL , data = json_data)
    data = r.json()
    print('update data', data)

update_data()