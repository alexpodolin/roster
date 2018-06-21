# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:14:48 2018

@author: podolin
"""

from flask import Flask
from config import Configuration

app = Flask(__name__)

# подключим файл с настройками
app.config.from_object(Configuration)
