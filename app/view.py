# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:29:41 2018

@author: podolin
"""

from app import app
from flask import render_template

from cust_func import current_month_name, current_year, make_calendar

@app.route('/')
def index() -> 'html':
    '''Вызов страницы index.html'''      
    dates=make_calendar()
    return render_template('index.html', \
                           current_month_name=current_month_name(), \
                           current_year=current_year(), \
                           dates=dates )