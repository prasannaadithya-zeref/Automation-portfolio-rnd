from flask import Flask, jsonify, request
import threading
import time
import sys

# Define app globally
app = Flask(__name__)

# Sample Data
users = {
    1: {"id": 1, "name": "Prasanna", "role": "Automation Engineer"},
    2: {"id": 2, "name": "Adithya", "role": "Data Engineer"}
}

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "UP", "service": "Mock API"}), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return jsonify({"message": "Not running with the Werkzeug Server"}), 500
    func()
    return jsonify({"message": "Server shutting down..."})

def start_server():
    app.run(port=5000)

if __name__ == '__main__':
    start_server()
