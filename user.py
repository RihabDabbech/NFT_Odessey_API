# user.py

from flask_restful import reqparse, Resource

users = [
    {
        "id": 1,
        "username": "user1",
        "password": "password1"
    }
]

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True, help="username cannot be blank")
        parser.add_argument("password", type=str, required=True, help="password cannot be blank")
        data = parser.parse_args()

        new_user = {
            "id": len(users) + 1,
            "username": data["username"],
            "password": data["password"]
        }
        users.append(new_user)
        return {"message": f"User {data['username']} has been created successfully."}, 201
