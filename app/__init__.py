from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
login_manager = LoginManager(app)
app.config.from_object('config')
db = SQLAlchemy(app)
# Handles all migrations.
migrate = Migrate(app, db)

from app import views, models
from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))