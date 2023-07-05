from app import db
from ..models.transactions_model import Transaction
from ..schemas.transactions_chemas import CreateTransaction

def create(transaction_data: CreateTransaction, seller_wallet: str) -> str:
    transaction = Transaction(buyer_wallet=transaction_data.buyer_wallet,
                              amount=transaction_data.amount,
                              project_id=transaction_data.project_id,
                              seller_wallet=seller_wallet)
    db.session.add(transaction)
    db.session.commit()

    return f'transaction {transaction} created'


def get_transactions_list():
    transactions = Transaction.query.all()
    return transactions


def get_current_transaction(transaction_id: int):
    transaction = db.session.query(Transaction).filter(Transaction.id==transaction_id).first()
    return transaction


def get_transactions_list_for_user(buyer_wallet: str):
    transactions = db.session.query(Transaction).filter(Transaction.buyer_wallet==buyer_wallet)
    return transactions


def get_transactions_list_for_project(project_id: int):
    transactions = db.session.query(Transaction).filter(Transaction.project_id==project_id)
    return transactions
