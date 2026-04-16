import requests

def post(url, json_data):
    response = requests.post(url, json=json_data)
    return response

def get(url, headers=None):
    response = requests.get(url, headers=headers)
    return response
