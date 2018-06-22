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

app = Flask(__name__)

# подключим файл с настройками
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)