import os
import datetime
from ..repositories import transactions_repository, projects_repository
from ..schemas.transactions_chemas import CreateTransaction
from flask import jsonify


def create_transaction(transaction_data: CreateTransaction):
    try:
        projects_repository.sell_projects_tocken(project_id=transaction_data.project_id, amount=transaction_data.amount)
        return jsonify(transactions_repository.create(transaction_data=transaction_data, seller_wallet='test_seller_wallet'))
    except Exception as error:
        return f'ERROR MESSAGE: {error}'
    

def get_all_transactions():
    try:
        transactions_list = []

        for transaction in transactions_repository.get_transactions_list():
            transactions_list.append(
                {
                    'id': transaction.id,
                    'buyer_wallet': transaction.buyer_wallet,
                    'amount': transaction.amount,
                    'seller_wallet': transaction.seller_wallet,
                    'project_id': transaction.project_id,
                    'created_at': transaction.created_at
                }
            )
            
        return jsonify(transactions_list)
    except Exception as error:
        return f'ERROR MESSAGE: {error}'


def get_current_transaction(transaction_id: int):
    try:
        transaction = transactions_repository.get_current_transaction(transaction_id=transaction_id)

        current_transaction = {
                    'id': transaction.id,
                    'buyer_wallet': transaction.buyer_wallet,
                    'amount': transaction.amount,
                    'seller_wallet': transaction.seller_wallet,
                    'project_id': transaction.project_id,
                    'created_at': transaction.created_at
                }
        return jsonify(current_transaction)
    except Exception as error:
        return f'ERROR MESSAGE: {error}'


def get_transactions_for_user(buyer_wallet: str):
    try:
        transactions_list = []

        for transaction in transactions_repository.get_transactions_list_for_user(buyer_wallet=buyer_wallet):
            transactions_list.append(
                {
                    'id': transaction.id,
                    'buyer_wallet': transaction.buyer_wallet,
                    'amount': transaction.amount,
                    'seller_wallet': transaction.seller_wallet,
                    'project_id': transaction.project_id,
                    'created_at': transaction.created_at
                }
            )
            
        return jsonify(transactions_list)
    except Exception as error:
        return f'ERROR MESSAGE: {error}'
    

def get_transactions_for_project(project_id: int):
    try:
        transactions_list = []

        for transaction in transactions_repository.get_transactions_list_for_project(project_id=project_id):
            transactions_list.append(
                {
                    'id': transaction.id,
                    'buyer_wallet': transaction.buyer_wallet,
                    'amount': transaction.amount,
                    'seller_wallet': transaction.seller_wallet,
                    'project_id': transaction.project_id,
                    'created_at': transaction.created_at
                }
            )
            
        return jsonify(transactions_list)
    except Exception as error:
        return f'ERROR MESSAGE: {error}'