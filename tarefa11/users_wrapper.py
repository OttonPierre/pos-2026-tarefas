import requests

API_URL = "https://jsonplaceholder.typicode.com"

def list():
    response = requests.get(f"{API_URL}/users/")
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def read(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def create(dados):
    response = requests.post(f"{API_URL}/users/", json=dados)
    if response.status_code == 201:
        return response.json()
    else:
        return False
     
def update(user_id, dados):
    response = requests.put(f"{API_URL}/users/{user_id}", json=dados)
    if response.status_code == 200:
        return response.json()
    else:
        return False

def delete(user_id):
    response = requests.delete(f"{API_URL}/users/{user_id}")
    if response.status_code == 204:
        return True
    else:
        return False