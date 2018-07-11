# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:51:58 2018

@author: podolin
"""
from datetime import datetime
import calendar
from models import Users, DutyDates
from app import db
from sqlalchemy import func
import re

# создадим объект календарь, первый день недели понедельник
cal = calendar.Calendar(firstweekday=0)

def get_current_year() -> int:
    '''Возвращает текущий год в формате ХХХХ'''
    cur_year = datetime.now().year
    return cur_year

def get_current_month_num() -> str:
    '''Получить номер текущего месяца'''
    current_month_num = datetime.now().month
    return current_month_num

def get_month_days_count(year, month) -> int:  
    '''Возвращает количество дней в месяце'''    
    days_count = calendar.monthrange(year, month)
    days_count = days_count[1]
    return days_count

def get_month_day_start(year, month) -> int:
    '''Возвращает индекс дня недели с которого начинается месяц'''
    month_days_list = list(cal.itermonthdays(year, month))
    first_day_week = 1
    for idx, num in enumerate(month_days_list):
        if num == first_day_week:
            first_day_index = idx
    return first_day_index
        
def get_week_month_count(year, month) -> int:
    '''Возвращает количество недель в месяце'''
    weeks_count = len(calendar.monthcalendar(year, month))
    return weeks_count

def month_days_list(year, month) -> int:  
    '''Список всех дней месяца'''
    month_days_list = cal.itermonthdays(year, month)    
    return month_days_list
    
months = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', \
          6:'июнь', 7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь', \
          11:'ноябрь', 12:'декабрь'} 
    
def create_month_data() -> None:
    '''Возвращает список списков состоящий из номера, названия, 
    количества дней для 12 месяцев'''
    # результирующий список куда попадут данные
    months_data = list()

    for key, value in months.items():
        data = list()
        month_number = data.append(key)
        month_name = data.append(value)
        weeks_count = data.append(get_week_month_count(get_current_year(), key))
        month_day_list = data.append(month_days_list(get_current_year(), key))
        month_data = months_data.append(data)
    return months_data

def get_duty_users() -> None:
    '''Вернет список дежурных из базы данных'''
    users = Users.query.all()
    return users

def get_schedule() -> None:
    '''Вернет список списков. 
    Состоящий из id дежурных, ФИО, цвета с фильтром по году и месяцу'''
    duty_list = list()
    for key, value in months.items():
        schedule = db.session.query(Users.id, Users.surname, Users.name, \
                                    Users.patronymic, Users.user_color, \
                                    DutyDates.date).\
                                    filter(Users.id==DutyDates.id_user).\
                                    filter(func.YEAR(DutyDates.date) == get_current_year()). \
                                    filter(func.MONTH(DutyDates.date) == key).all()        
        for el in schedule:
            el = [el[0], \
                       el[1].capitalize() + ' '+ el[2][0].upper() + '.' + el[3][0].upper() + '.', \
                       '#' + el[4], el[5].year, el[5].month, el[5].day]
            el_data = duty_list.append(el) 
            
    return duty_list             