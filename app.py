import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import logging
from models import *

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
# db = SQLAlchemy(app)

db.init_app(app)

with app.app_context():
    logging.info("execute db.create_all()")
    db.create_all()

# Routes
@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask + SQLAlchemy + PostgreSQL!"})

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

if __name__ == "__main__":
    logging.info("start app")
    app.run(host="0.0.0.0", port=5000)
