# -*- coding: utf-8 -*-
from datetime import datetime
from app import db
from dataclasses import dataclass, field
from os import path, getcwd
from flask_login import UserMixin
from app import db

@dataclass
class Map(db.Model):
    __tablename__ = 'Map'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)
    square = db.Column(db.Integer)
    kadastr_number = db.Column(db.String(20))
    available = db.Column(db.BOOLEAN())

    # для json
    number: int
    square: int
    available: bool

@dataclass
class Admin(db.Model, UserMixin):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(16))


    def check_password(self, password):
        return self.password == password
