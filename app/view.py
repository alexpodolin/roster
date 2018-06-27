# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:29:41 2018

@author: podolin
"""

from app import app, db
from flask import render_template, request, redirect
from models import Users, DutyDates
from cust_func import current_month_name, current_month_num, current_year, \
                        make_calendar

@app.route('/', methods=['GET'])
def index() -> 'html':
    '''Вызов страницы index.html'''
    # список всех дат текущего месяца     
    dates=make_calendar()
    # номер текущего месяца
    #current_month_num()
    
    # получим список пользователей
    users = Users.query.all() 
    
    return render_template('index.html', \
                           current_month_name=current_month_name(), \
                           current_year=current_year(), dates=dates, \
                           current_month_num=current_month_num(), \
                           users=users)
    
@app.route('/add_duty_date', methods=['GET'])
def add_duty_date() -> 'html':
    # полученные из ajax данные
    id = request.args.get('user_id')
    date = request.args.get('date')

    # ищем id записи строки с заданной датой 
    get_row = db.session.query(DutyDates). \
                        filter_by(date=date).first()                    
    
    # если для заданной даты уже назнаен пользователь, 
    # то обновим id пользователя для заданной даты
    if get_row:       
        db.session.query(DutyDates).filter(get_row.id == DutyDates.id). \
                                    update({"id_user": id})
        db.session.commit()  
    else:
        add_duty_day = DutyDates(id_user=id, date=date)
        db.session.add(add_duty_day)
        db.session.commit()        
        
    return render_template('index.html')