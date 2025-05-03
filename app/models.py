from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    return app
from datetime import datetime
from app.db import db

from app.db import db
import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

class Ride(db.Model):
    __tablename__ = 'rides'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pickup = db.Column(db.String(120), nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    fare = db.Column(db.Float, nullable=True)
    eta_minutes = db.Column(db.Integer, nullable=True)
    currency = db.Column(db.String(10), default="KZT")
    status = db.Column(db.String(50), default="requested")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

