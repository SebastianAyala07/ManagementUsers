from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'

mongo = PyMongo(app)

CORS(app)

collection_users = mongo.db.users


@app.route('/users', methods=['POST'])
def create_user():
    id = collection_users.insert(
        {
            'name': request.json['name'],
            'email': request.json['email'],
            'password': request.json['password']
        }
    )
    return jsonify({'id': str(ObjectId(id))})

@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for doc in collection_users.find():
        users.append(
            {
                '_id': str(ObjectId(doc['_id'])),
                'name': doc['name'],
                'email': doc['email'],
                'password': doc['password'],
            }
        )
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = collection_users.find_one({'_id': ObjectId(id)})
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'password': user['password'],
    })

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    response = collection_users.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'User deleted'})

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    collection_users.update_one(
        {'_id': ObjectId(id)},
        {'$set':
            {
                'name': request.json['name'],
                'email': request.json['email'],
                'password': request.json['password']
            }
        }
    )
    return jsonify({'msg': 'User updated'})

if __name__ == "__main__":
    app.run(debug=True)