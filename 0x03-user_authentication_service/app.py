#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, request, jsonify
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
