import os
import datetime
from ..repositories import projects_repository, transactions_repository
from ..schemas.projects_schemas import CreateProject, UpdateProject
from flask import jsonify
import datetime


def create_project(project_data: CreateProject):
    try:
        return jsonify(projects_repository.create(project_data=project_data))
    except Exception as error:
        return f'ERROR MESSAGE: {error}'
    

def get_all_projects():
    try:
        projects_list = []

        for project in projects_repository.get_projects_list():
            projects_list.append(
                {
                    'id': project.id,
                    'name': project.name,
                    'coin_price': project.coins_price,
                    'coins_count': project.coins_count,
                    'current_coins_count': project.current_coins_count
                }
            )
            
        return jsonify(projects_list)
    except Exception as error:
        return f'ERROR MESSAGE: {error}'


def update_project(project_data: UpdateProject, project_id: int):
    try:
        return jsonify(projects_repository.update_project(project_data=project_data, project_id=project_id))
    except Exception as error:
        return f'ERROR MESSAGE: {error}'
    

def delete_project(project_id: int):
    try:
        return jsonify(projects_repository.delete_project(project_id=project_id))
    except Exception as error:
        return f'ERROR MESSAGE: {error}'


def get_current_project(project_id: int):
    try:
        project = projects_repository.get_current_project(project_id=project_id)
        transactions = transactions_repository.get_transactions_list_for_project(project_id=project_id)

        total_transactions_count = 0

        for transaction in transactions:
            total_transactions_count += 1

        transactions_pear_day = 0

        median_amount_pear_day = 0

        for transaction in transactions:
            current_date = str(datetime.datetime.now()).split(' ')
            transaction_date = str(transaction.created_at).split(' ')
            if current_date[0] == transaction_date[0]:
                transactions_pear_day += 1
                median_amount_pear_day += transaction.amount

        try:
            coins_median_amount_pear_day = median_amount_pear_day / transactions_pear_day
        except Exception as e:
            coins_median_amount_pear_day = 0

        usdt_median_amount_pear_day = coins_median_amount_pear_day * project.coins_price



        current_project = {
                    'id': project.id,
                    'name': project.name,
                    'coin_price': project.coins_price,
                    'coins_count': project.coins_count,
                    'current_coins_count': project.current_coins_count,
                    'total_transactions_count': total_transactions_count,
                    'transactions_pear_day': transactions_pear_day,
                    'coins_median_amount_pear_day': coins_median_amount_pear_day,
                    'usdt_median_amount_pear_day': usdt_median_amount_pear_day
                }
        return jsonify(current_project)
    except Exception as error:
        return f'ERROR MESSAGE: {error}'
