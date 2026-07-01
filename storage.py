import json
import os
DATA_FILE = "credentials.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return{}
    with open (DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data: dict):
    with open (DATA_FILE, "w") as f:
        json.dump(data, f, indent = 5)

def add_entry(service: str, username: str, encrypted_password: str):
    data = load_data()
    data[service] = {
        "username": username,
        "password": encrypted_password
    }
    save_data(data)

def get_entry(service: str):
    data= load_data()
    return data.get(service)

def delete_entry(service: str) -> bool:
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        return True
    return False

def list_services():
    data=load_data()
    return list(data.keys())

