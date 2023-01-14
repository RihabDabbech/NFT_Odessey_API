# security.py

users = [
    {
        "id": 1,
        "username": "user1",
        "password": "password1"
    },
    {
        "id": 2,
        "username": "user2",
        "password": "password2"
    }
]

def authenticate(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

def identity(payload):
    user_id = payload["identity"]
    for user in users:
        if user["id"] == user_id:
            return user
    return None
