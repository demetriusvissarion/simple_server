import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, world!"

@app.route('/endpoint', methods=['POST'])
def post_data():
    try:
        data = request.json 
        username = data.get('username')  
        password = data.get('password')
        phoneNumber = data.get('phoneNumber')

        # Perform any processing or store data as needed
        # For now, just echoing back the received data
        return jsonify({'message': f'Success! Received username: {username}, password: {password}, phoneNumber: {phoneNumber}'}), 200

    except Exception as e:
        return jsonify({'error': f'Error processing the request: {str(e)}'}), 400
    
todos = [
    {
        'title': 'Walk the dog',
        'done': False
    },
    {
        'title': 'Buy some food',
        'done': False
    }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    try:
        return jsonify(todos), 200
    except Exception as e:
        return jsonify({'error': f'Error processing the request: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(
      debug=True,
      host="0.0.0.0" 
    )