#!/usr/bin/env python3
"""A New App using Flask"""


from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")