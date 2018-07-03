# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:29:41 2018

@author: podolin
"""

from app import app, db
from flask import render_template, request
from models import Users, DutyDates
from cust_func import current_month_name, current_month_num, current_year, \
                        make_calendar, weeks_count
from re import sub
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
dict_color = dict()
for i in schedule:
    # обработанный результат запроса schedule
    duty_list = dict([(str(i[5]), str(i[1]).capitalize() + ' ' \
                       + str(i[2][0]).upper() + '.' \
                       + str(i[3][0]).upper() + '.')])
    # отбросим первый 0 если он есть, 
    # т.к. в нашем календаре числа без нулей вначале
    for day, person in duty_list.items():
        day = sub('^[0-9]{4}-[0-9]{2}-', '', day)
        day = int(day)
        # в переменной duty_list словари дата:фио в нужном формате
        duty_list = dict([(day, person)])
        
        # по всем ключам получим значения и сформируем новый словарь
        # key = day, value = person
        for day in duty_list.keys():		
		       dict_format[day] = duty_list[day]

    # какому id пользователя, какой цвет соответствует
    # key = user_id, value = user_color
    u_color_list = dict([(str(i[0]), '#' + str(i[4]))])
    for id in u_color_list.keys():
        dict_color[id] = u_color_list[id]
        
# отрисовка гланой страницы
@app.route('/', methods=['GET'])
def index() -> 'html':
    '''Вызов страницы index.html'''
    # список всех дат текущего месяца     
    dates=make_calendar()
    # номер текущего месяца
    #current_month_num()

    return render_template('index.html', \
                           current_month_name=current_month_name(), \
                           current_year=current_year(), dates=dates, \
                           weeks_count=weeks_count(), \
                           current_month_num=current_month_num(), \
                           users=users, persons=dict_format, u_id=u_color_list)
# всплывающее окно
@app.route('/add_duty_date', methods=['GET'])
def add_duty_date() -> 'html':
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
                
    return render_template('index.html')