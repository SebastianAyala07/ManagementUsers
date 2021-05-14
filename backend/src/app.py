from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'

mongo = PyMongo(app)

collection_users = mongo.db.users


@app.route('/users', methods=['POST'])
def create_user():
    return 'received'

@app.route('/users', methods=['GET'])
def get_users():
    return 'received'

@app.route('/user/<id>', methods=['GET'])
def get_user():
    return 'received'

@app.route('/users/<id>', methods=['GET'])
def delete_user():
    return 'received'

@app.route('/users/<id>', methods=['PUT'])
def update_user():
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)