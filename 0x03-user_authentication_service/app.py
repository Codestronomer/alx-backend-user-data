#!/usr/bin/env python3
"""
Entry file for flask app
"""
from flask import (
        Flask,
        jsonify,
        request,
        make_response,
        abort,
        redirect,
        url_for
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """user logout route"""
    session_id = request.cookies.get('session_id')
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            return redirect('/')
    return abort(403)


@app.route('/profile', strict_slashes=False)
def profile():
    """Get a user profile from the session_id in cookie"""
    session_id = request.cookies.get('session_id')
    if session_id is not None:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            return jsonify({"email": user.email})
    return abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ Get reset password token """
    email = request.form['email']
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": reset_token})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
