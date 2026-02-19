#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)
user = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}
@auth.verify_password
def verify(username, password):
    if username in users and check_password_hash(user[username]["password"], password):
        return username
    @app.route("/basic-protected")
    @auth.login_required
    def basic_protected():
        return jsonify(message="Basic Auth: Access Granted")
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if username in users and check_password_hash(user[username]["password"], password):
            token = create_access_token(identity=users[usename])
            return jsonify(create_token=token)
        return jsonify(error="Invalid credentials"), 401
    @app.route("/jwt-protected")
    @jwt_required()
    def jwt_protected():
        return jsonify(message="JWT Auth: Access Granted")
    @app.route("/admin-only")
    @jwt_required()
    def admin_only():
        identity = get_jwt_identity()
        if identity["role"] != "admin":
            return jsonify(error="Admin access required"), 403
        return jsonify(message="Admin Access: Granted")