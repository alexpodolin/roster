# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:03:49 2018

@author: podolin
"""

from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(15), unique=False, nullable=False)
    name = db.Column(db.String(15), unique=False, nullable=False)    
    patronymic = db.Column(db.String(15), unique=False, nullable=False)
    user_color = db.Column(db.CHAR(length=6), unique=False, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return '<Users surname: {}, name: {}, patronymic: {}, user_color: {}>'\
                .format(self.surname, self.name, self.patronymic, self.user_color)
                
