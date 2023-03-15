#!/usr/bin/env python3
"""
Entry file for flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

# initialize flask app
app = Flask(__name__)

# Instantiate auth object
AUTH = Auth()


@app.route("/", strict_slashes=False)
def home():
    """Home route for flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    email, password = request.form['email'], request.form['password']
    try:
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
