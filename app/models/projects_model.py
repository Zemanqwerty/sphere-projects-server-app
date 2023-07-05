from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app import db


class Project(db.Model):

    __tablename__ = 'project'
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    uuid = db.Column(
        db.String(36),
        default=uuid.uuid4,
        nullable=False
    )

    name = db.Column(
        db.String(128),
        comment='Project name',
        nullable=False
    )

    description = db.Column(
        db.String(),
        comment='Project description',
        nullable=False
    )

    owner_wallet = db.Column(
        db.String(128),
        comment='Owner eth waller',
        nullable=False
    )

    coins_count = db.Column(
        db.Integer(),
        comment='Count of projects coins for ILO',
        nullable=False
    )

    current_coins_count = db.Column(
        db.Integer(),
        comment='Current count of projects coins for ILO',
        nullable=False
    )

    coins_price = db.Column(
        db.Float(),
        comment='Price of projects coin',
        nullable=False
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )

    modified_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )


    def __repr__(self):
        return f'{self.uuid} {self.name}'