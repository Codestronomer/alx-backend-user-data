#!/usr/bin/env python3
"""
Entry file for flask app
"""
from flask import (
        Flask,
        jsonify,
        request,
        make_response,
        abort
        )
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
    """ User registration route """
    email, password = request.form['email'], request.form['password']
    try:
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """user login route"""
    email, password = request.form['email'], request.form['password']
    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            resp = make_response(jsonify({"email": email,
                                          "message": "logged in"}))
            resp.set_cookie("session_id", session_id)
            return resp
        else:
            return abort(401)
    except Exception as err:
        return err


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
