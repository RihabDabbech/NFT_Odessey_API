# NFT_Odessey_API
NFT API
This is a RESTful API for managing non-fungible tokens (NFTs). The API allows for CRUD (Create, Read, Update, Delete) operations on a database of NFT items, each of which has an ID, name, image URL, and metadata.

Getting Started

1.Clone the repository:
git clone https://github.com/<your-username>/nft-api.git

2.Install the dependencies:
pip install -r requirements.txt

3.Run the app:
python app.py

4.Test the API using a tool such as Insomnia.
https://insomnia.rest

Endpoints
The following endpoints are available:

/nft/int:id (GET, POST, PUT, DELETE)
This endpoint is used to retrieve, create, update and delete an NFT item.

GET: Retrieve an NFT item by ID. If no ID is specified, retrieves the first NFT item in the database.

POST: Create a new NFT item. The following parameters are required in the request body:

name: The name of the NFT item
image_url: The URL of the image associated with the NFT item
metadata: Any additional metadata associated with the NFT item
PUT: Update an existing NFT item by ID. The following parameters are required in the request body:

name: The name of the NFT item
image_url: The URL of the image associated with the NFT item
metadata: Any additional metadata associated with the NFT item
DELETE: Delete an NFT item by ID.

/login (POST)
This endpoint is used to authenticate users and get an access token.

POST: Authenticate a user. The following parameters are required in the request body:
username: The username of the user
password: The password of the user
Security
This API uses JSON Web Tokens (JWT) for authentication. Users must provide a valid access token in the Authorization header to access the API.

Built With
Flask - The web framework used
SQLite3 - The database used
Flask-RESTful - Extension for Flask to create RESTful APIs
Flask-JWT - Extension for Flask to handle JWT authentication


Author
Rihab Dabbech - Your Github URL
License
This project is licensed under the MIT License - see the LICENSE.md file for details.


