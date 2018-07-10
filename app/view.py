# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:29:41 2018

@author: podolin
"""

from app import app, db
from flask import render_template, request, redirect
from models import DutyDates
from cust_func import get_current_year, create_month_data, get_duty_users, \
                get_schedule


@app.route('/', methods=['GET'])
def index() -> 'html':
    '''Корневая страница'''    
    current_year = get_current_year()
    months_data = create_month_data()
    users = get_duty_users()    
    schedule = get_schedule()
    
    return render_template('index.html', current_year=current_year, months_data=months_data, \
                           users=users, schedule=schedule)

@app.route('/add_duty_date', methods=['GET'])
def add_duty_date() -> 'html':
    ''' Всплывающее окно '''
    # полученные из ajax данные
    id = request.args.get('user_id')
    date = request.args.get('date')

    # ищем записи строки с заданной датой 
    get_row_date = db.session.query(DutyDates). \
                        filter_by(date=date).first()
                        
    # если для заданной даты уже назнаен пользователь, 
    # то обновим id пользователя для заданной даты
    if get_row_date:      
        db.session.query(DutyDates).filter(get_row_date.id == DutyDates.id). \
                                    update({"id_user": id})
        db.session.commit()  
    else:
        add_duty_day = DutyDates(id_user=id, date=date)
        db.session.add(add_duty_day)
        db.session.commit()
                
    return redirect('index.html')