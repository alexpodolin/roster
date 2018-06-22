# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:29:41 2018

@author: podolin
"""

from app import app
from flask import render_template
from models import Users
from cust_func import current_month_name, current_month_num, current_year, \
                        make_calendar

@app.route('/', methods=['GET'])
def index() -> 'html':
    '''Вызов страницы index.html'''
    # список всех дат текущего месяца     
    dates=make_calendar()
    # номер текущего месяца
    current_month_num()
    
    # получим список пользователей
    users = Users.query.all() 
    
    return render_template('index.html', \
                           current_month_name=current_month_name(), \
                           current_year=current_year(), dates=dates, \
                           current_month_num = current_month_num(), \
                           users=users)