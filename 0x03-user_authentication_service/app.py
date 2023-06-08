#!/usr/bin/env python3
"""A New App using Flask"""


from flask import Flask, jsonify, request
from flask import make_response, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """A base Route of the App"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """An Endpoint to register a User"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Get Email and Password from Request Form Data"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(401)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response_payload = {
        "email": email,
        "message": "logged in"
    }

    response = make_response(jsonify(response_payload))

    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """Logout a user by destroying the session."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        response = make_response(jsonify({"message": "logged out"}))
        response.set_cookie("session_id", expires=0)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """Endpoint to retrieve the user profile."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
