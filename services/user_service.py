import json
import os
from models.users import User 

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'users.json')

def load_users():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(DATA_PATH, 'w') as f:
        json.dump(users, f)

def add_user(user):
    users = load_users()
    for u in users:
        if u['user_id'] == user.user_id:
            print("User ID already exists")
            return
    users.append(user.to_dict())
    save_users(users)
    print("User added successfully")

def list_users():
    users = load_users()
    if not users:
        print("No users found")
        return
    for u in users:
        print("ID:", u['user_id'], "Name:", u['name'])

def remove_user(user_id):
    users = load_users()
    new_users = [u for u in users if u['user_id'] != user_id]
    if len(new_users) == len(users):
        print("User not found")
        return
    save_users(new_users)
    print("User removed")
