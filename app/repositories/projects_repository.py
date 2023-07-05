from app import db
from ..models.projects_model import Project
from ..schemas.projects_schemas import CreateProject, UpdateProject

def create(project_data: CreateProject) -> str:
    project = Project(name=project_data.name,
                      description=project_data.description,
                      owner_wallet=project_data.owner_wallet,
                      coins_count=project_data.coins_count,
                      coins_price=project_data.coins_price,
                      current_coins_count=project_data.coins_count)
    db.session.add(project)
    db.session.commit()

    return f'project {project.name} created'


def get_projects_list():
    projects = Project.query.all()
    return projects


def update_project(project_data: UpdateProject, project_id: int) -> str:
    project = db.session.query(Project).filter(Project.id==project_id).first()
    project.name = project_data.name
    project.description = project_data.description
    project.coins_count = project_data.coins_count
    project.coins_price = project_data.coins_price

    db.session.commit()

    return f'project with id: "{project_id}" updated'


def sell_projects_tocken(project_id: int, amount: int) -> str:
    project = db.session.query(Project).filter(Project.id==project_id).first()
    project.current_coins_count -= amount

    db.session.commit()

    return f'project with id "{project_id}" selled {amount} tockens'


def delete_project(project_id: int) -> str:
    Project.query.filter_by(id=project_id).delete()
    db.session.commit()

    return f'project with id "{project_id}" deleted'


def get_current_project(project_id: int):
    project = db.session.query(Project).filter(Project.id==project_id).first()
    return project
