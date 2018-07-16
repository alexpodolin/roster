# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:03:49 2018

@author: podolin
"""
from app import db
from flask_security import UserMixin, RoleMixin

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(15), unique=False, nullable=False)
    name = db.Column(db.String(15), unique=False, nullable=False)    
    patronymic = db.Column(db.String(15), unique=False, nullable=False)
    user_color = db.Column(db.CHAR(length=6), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=True, nullable=False)    
    dates = db.relationship('DutyDates', backref='user', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return '<Users id: {}, surname: {}, name: {}, patronymic: {}, \
                user_color: {}, email: {}, phone: {}>' \
                .format(self.id, self.surname, self.name, self.patronymic, \
                        self.user_color, self.email, self.phone )
                
class DutyDates(db.Model):
    __tablename__ = 'duty_dates'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    id_user = db.Column(db.SmallInteger, db.ForeignKey('users.id'))
    date = db.Column(db.Date, nullable=False)
    
    def __init__(self, *args, **kwargs):
        super(DutyDates, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        return '<DutyDates id: {}, id_user: {}, date: {}>' \
                .format(self.id, self.id_user, self.date)