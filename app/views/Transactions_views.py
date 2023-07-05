from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from ..schemas.transactions_chemas import CreateTransaction
from flask_pydantic import validate
from ..services import transactions_services
from flask_sqlalchemy import SQLAlchemy
from app import app


@app.route('/transactions/create', methods=['POST'])
@validate()
def create_transaction(body: CreateTransaction):
    return transactions_services.create_transaction(transaction_data=body)


@app.route('/transactions/all', methods=['GET'])
def get_all_transactions():
    return transactions_services.get_all_transactions()


@app.route('/transactions/<transaction_id>', methods=['GET'])
@validate()
def get_current_transaction(transaction_id: int):
    return transactions_services.get_current_transaction(transaction_id=transaction_id)


@app.route('/transactions/projects/<project_id>', methods=['GET'])
@validate()
def get_all_transactions_for_project(project_id: int):
    return transactions_services.get_transactions_for_project(project_id=project_id)


@app.route('/transactions/buyers/<buyer_wallet>', methods=['GET'])
def get_all_transactions_for_buyer(buyer_wallet: str):
    return transactions_services.get_transactions_for_user(buyer_wallet=buyer_wallet)
