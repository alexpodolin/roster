# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:21:30 2018

@author: podolin
"""

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://roster:password@192.168.160.131/roster'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret key'
    
    