# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:28:19 2018

@author: podolin
"""

from app import app, db
from flask import render_template, request
from models import Users, DutyDates
from cust_func import current_month_name, current_month_num, current_year, \
                        make_calendar, weeks_count
import re
from sqlalchemy import func

# получим список пользователей из БД с аттрибутами
users = Users.query.all()     

# список дат, id дежурных, цвета с фильтром по году и месяцу
schedule = db.session.query(Users.id, Users.surname, Users.name, \
                            Users.patronymic, Users.user_color, DutyDates.date). \
                            filter(Users.id==DutyDates.id_user). \
                            filter(func.YEAR(DutyDates.date) == current_year()). \
                            filter(func.MONTH(DutyDates.date) == current_month_num()).all()
       
# словарь содержащий дату и ФИО дежурных                                
dict_format = dict()    # пустой словарь, тут будет дата: фио

for i in schedule:
    # обработанный результат запроса schedule
    duty_list = {'day': str(i[5]), \
                 'initial': str(i[1]).capitalize() + ' ' \
                 + str(i[2][0]).upper() + '.' + str(i[3][0]).upper() + '.', \
                 'color': '#' + str(i[4])}          