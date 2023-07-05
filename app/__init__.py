from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os



BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object('config.DevelopConfig')
db = SQLAlchemy(app)
Session(app)
UPLOAD_FOLDER = os.path.join(BASEDIR, 'upload-files/')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'docx'}

from app.models import projects_model, transactions_model
from app.views import Projects_views, Transactions_views