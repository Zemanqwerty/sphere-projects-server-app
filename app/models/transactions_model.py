from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app import db


class Transaction(db.Model):

    __tablename__ = 'transaction'
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    uuid = db.Column(
        db.String(36),
        default=uuid.uuid4,
        nullable=False
    )

    buyer_wallet = db.Column(
        db.String(128),
        comment='Buyer wallet address',
        nullable=False
    )

    amount = db.Column(
        db.Integer(),
        comment='Transaction amount',
        nullable=False
    )

    seller_wallet = db.Column(
        db.String(128),
        comment='Seller waller address',
        nullable=False
    )

    project_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'project.id'
        )
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

    project = db.relationship("Project", foreign_keys=[project_id])


    def __repr__(self):
        return f'{self.uuid}'