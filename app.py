import sqlite3
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required 
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'Rihab'
api = Api(app)
jwt = JWT(app, authenticate, identity)

# Connect to the database
conn = sqlite3.connect('nft.db')
cursor = conn.cursor()

# Create the nft table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nft (
        id INTEGER PRIMARY KEY,
        name TEXT,
        image_url TEXT,
        metadata TEXT
    )
''')
conn.commit()

class Nft(Resource):
    @jwt_required()
    def get(self, id=0):
        if id == 0:
            cursor.execute('SELECT * FROM nft')
            nft = cursor.fetchone()
            return {'nft': {'id': nft[0], 'name': nft[1], 'image_url': nft[2], 'metadata': nft[3]}}, 200
        else:
            cursor.execute('SELECT * FROM nft WHERE id=?', (id,))
            nft = cursor.fetchone()
            if nft:
                return {'nft': {'id': nft[0], 'name': nft[1], 'image_url': nft[2], 'metadata': nft[3]}}, 200
            else:
                return {'message': 'Nft is not found'}, 404
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("image_url")
        parser.add_argument("metadata")
        args = parser.parse_args()

        cursor.execute('INSERT INTO nft (name, image_url, metadata) VALUES (?, ?, ?)', (args['name'], args['image_url'], args['metadata']))
        conn.commit()

        cursor.execute('SELECT last_insert_rowid()')
        id = cursor.fetchone()[0]

        return {'nft': {'id': id, 'name': args['name'], 'image_url': args['image_url'], 'metadata': args['metadata']}}, 201
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("image_url")
        parser.add_argument("metadata")
        args = parser.parse_args()

        cursor.execute('SELECT * FROM nft WHERE id=?', (id,))
        nft = cursor.fetchone()
        if nft:
            cursor.execute('UPDATE nft SET name=?, image_url=?, metadata=? WHERE id=?', (args['name'], args['image_url'], args['metadata'], id))
            conn.commit()
            return {'nft': {'id': id, 'name': args['name'], 'image_url': args['image_url'], 'metadata': args['metadata']}}, 201
        else:
            return {'message': 'Nft not found'}, 404

    def delete(self, id):
        cursor.execute('DELETE FROM nft WHERE id=?', (id,))
        if cursor.rowcount > 0:
            conn.commit()
            return {'message': f'Nft with id {id} is deleted'}, 200
        else:
            return {'message': 'Nft not found'}, 404

api.add_resource(Nft, "/nft/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
