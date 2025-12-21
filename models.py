"""Database models."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# -------------------------
# Tabellen volgens jouw ERD
# -------------------------

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String, nullable=True)

    transactions = db.relationship('Transaction', backref='user', lazy=True)


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.BigInteger, primary_key=True)
    amount = db.Column(db.Float, nullable=True)
    date = db.Column(db.Date, nullable=True)
    description = db.Column(db.String, nullable=True)

    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=True)
    category_id = db.Column(db.BigInteger, db.ForeignKey('category.id'), nullable=True)
    receipt_id = db.Column(db.BigInteger, db.ForeignKey('receipt.id'), nullable=True)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=True)

    transactions = db.relationship('Transaction', backref='category', lazy=True)


class Receipt(db.Model):
    __tablename__ = 'receipt'
    id = db.Column(db.BigInteger, primary_key=True)
    file_path = db.Column(db.String, nullable=True)
    parsed_amount = db.Column(db.BigInteger, nullable=True)
    parsed_date = db.Column(db.Date, nullable=True)
    parsed_vendor = db.Column(db.String, nullable=True)
    parsed_quantity = db.Column(db.BigInteger, nullable=True)

    transactions = db.relationship('Transaction', backref='receipt', lazy=True)