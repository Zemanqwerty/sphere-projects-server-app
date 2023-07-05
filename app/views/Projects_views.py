from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from ..schemas.projects_schemas import CreateProject, UpdateProject
from flask_pydantic import validate
from ..services import projects_service
from flask_sqlalchemy import SQLAlchemy
from app import app
from flask.views import View


@app.route('/projects/create', methods=['POST'])
@validate()
def create_project(body: CreateProject):
    return projects_service.create_project(project_data=body)


@app.route('/projects/all', methods=['GET'])
def get_all_projects():
    return projects_service.get_all_projects()


@app.route('/projects/<project_id>/update', methods=['PUT'])
@validate()
def update_project(body: UpdateProject, project_id: int):
    return projects_service.update_project(project_data=body, project_id=project_id)


@app.route('/projects/<project_id>/delete', methods=['DELETE'])
@validate()
def delete_project(project_id: int):
    return projects_service.delete_project(project_id=project_id)


@app.route('/projects/<project_id>', methods=['GET'])
@validate()
def get_current_project(project_id: int):
    return projects_service.get_current_project(project_id=project_id)
