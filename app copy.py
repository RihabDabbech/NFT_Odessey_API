from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import os
from flask import Flask, request, jsonify



app = Flask(__name__)

api = Api(app)
nft_list = [
{
    "id": 1,
    "name": "CryptoKitty #1",
    "image_url": "https://cryptokitties.com/kitty/1",
    "metadata": {
        "breed": "Siamese",
        "generation": 5,
        "owner": "0x123456..."
    }
},
{
    "id": 2,
    "name": "CryptoKitty #2",
    "image_url": "https://cryptokitties.com/kitty/2",
    "metadata": {
        "breed": "British Shorthair",
        "generation": 3,
        "owner": "0x789012..."
    }
},
{
    "id": 3,
    "name": "CryptoKitty #3",
    "image_url": "https://cryptokitties.com/kitty/3",
    "metadata": {
        "breed": "Persian",
        "generation": 6,
        "owner": "0x456789..."
    }
},
{
    "id": 4,
    "name": "CryptoKitty #4",
    "image_url": "https://cryptokitties.com/kitty/4",
    "metadata": {
        "breed": "Manx",
        "generation": 4,
        "owner": "0x24680..."
    }
},
{
    "id": 5,
    "name": "CryptoKitty #5",
    "image_url": "https://cryptokitties.com/kitty/5",
    "metadata": {
        "breed": "Siamese",
        "generation": 2,
        "owner": "0x135790..."
    }
},
{
    "id": 6,
    "name": "CryptoKitty #6",
    "image_url": "https://cryptokitties.com/kitty/6",
    "metadata": {
        "breed": "Manx",
        "generation": 7,
        "owner": "0x369258..."
    }
}

]
class Nft(Resource):
    def __init__(self):
        pass

class Nft(Resource):  

    def get(self, id=0):
        if id == 0:
            return random.choice(nft_list), 200

        for nft in nft_list:
            if(nft["id"] == id):
                return nft, 200
        return "Nft is not found", 404
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        parser.add_argument("image_url")
        parser.add_argument("metadata")
        args = parser.parse_args()

        nft = {
            "id": args["id"],
            "name": args["name"],
            "image_url": args["image_url"],
            "metadata": args["metadata"]
        }
        nft_list.append(nft)
        return nft, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("image_url")
        parser.add_argument("metadata")

        params = parser.parse_args()

        for nft in nft_list:
            if(id == nft["id"]):
                nft["name"] = params["name"]
                nft["image_url"] = params["image_url"]
                nft["metadata"] = params["metadata"]

                return nft, 200

        nft = {
            "id": id,
            "name": params["name"],
            "image_url": params["image_url"],
            "metadata": params["metadata"],
        }

        nft_list.append(nft)
        return nft, 201
    
    def delete(self, id):
        global nft_list
        nft_list = [nft for nft in nft_list if nft["id"] != id]
        return f"Nft with id {id} is deleted"
api.add_resource(Nft, "/nft_list", "/nft_list/", "/nft_list/<int:id>")



if __name__ == '__main__':
    app.run(debug=True)
######################################################
from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import os
from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required 
from security import authenticate, identity
from user import UserRegister 


app = Flask(__name__)
app.secret_key = 'Rihab'
api = Api(app)

    # authenticate the user and return a JWT token
    # verify the JWT token and return the user

jwt = JWT(app, authenticate, identity) #/auth

nft_list = [
    {
        "id": 1,
        "name": "CryptoKitty #1",
        "image_url": "https://cryptokitties.com/kitty/1",
        "metadata": {
            "breed": "Siamese",
            "generation": 5,
            "owner": "0x123456..."
        }
    }
]

class Nft(Resource):
    @jwt_required()
    def get(self, id=0):
        if id == 0:
            return random.choice(nft_list), 200

        for nft in nft_list:
            if(nft["id"] == id):
                return nft, 200
        return "Nft is not found", 404
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        parser.add_argument("image_url")
        parser.add_argument("metadata")
        args = parser.parse_args()

        nft = {
            "id": args["id"],
            "name": args["name"],
            "image_url": args["image_url"],
            "metadata": args["metadata"]
        }
        nft_list.append(nft)
        return nft, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("image_url")
        parser.add_argument("metadata")

        params = parser.parse_args()

        for nft in nft_list:
            if(id == nft["id"]):
                nft["name"] = params["name"]
                nft["image_url"] = params["image_url"]
                nft["metadata"] = params["metadata"]

                return nft, 200

        nft = {
            "id": id,
            "name": params["name"],
            "image_url": params["image_url"],
            "metadata": params["metadata"],
        }

        nft_list.append(nft)
        return nft, 201
    
    
    def delete(self, id):
        global nft_list
        nft_list = [nft for nft in nft_list if nft["id"] != id]
        return f"Nft with id {id} is deleted"
api.add_resource(Nft, "/nft_list", "/nft_list/", "/nft_list/<int:id>")


if __name__ == '__main__':
    app.run(debug=True)
####################################################################################
import hmac
import hashlib

from user import User

users = [
    User(1, 'rihab', 'azerty')
]

username_mapping = {user.username: user for user in users}
userid_mapping = {user.id: user for user in users}


def authenticate(username, password):
    user = User.find_by_username(username)
    if user:
        # Use hmac_digest to compute a digest of the password and compare it with the stored password digest
        password_digest = hmac.digest(user.password.encode(), password.encode(), hashlib.sha256)
        if password_digest == user.password:
            return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
###########################################################################
import os
import sqlite3

from flask_restful import Resource, reqparse

dir_path = os.path.dirname(os.path.realpath(__file__))
database_location = os.path.join(dir_path, 'data.db')


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username, ))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id, ))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field is required.')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field is required.')
    
    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists.'}, 400

        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {'message': 'User created successfully.'}, 201

