# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:14:48 2018

@author: podolin
"""

from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel

app = Flask(__name__)

# подключим файл с настройками
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# ADMIN
from models import *
admin = Admin(app)
admin.add_view(ModelView(Users, db.session, 'Дежурные'))
admin.add_view(ModelView(DutyDates, db.session, 'Даты дежурств'))

babel = Babel(app)
@babel.localeselector
def get_locale():
        return 'ru'