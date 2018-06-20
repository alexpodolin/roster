# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:51:58 2018

@author: podolin
"""

from datetime import datetime
import os
import locale
import calendar

# текущий год
def current_year() -> int:
    '''Получить текущий год в формате ХХХХ'''
    current_year = datetime.now().year
    return current_year

# номер текущего месяца
def current_month_num() -> int:
    '''Получить номер текущего месяца'''
    current_month_num = datetime.now().month
    return current_month_num
    
# название текущего месяца
def current_month_name() -> str: 
    '''Получить название текущего месяца'''
    current_month_num = datetime.now().month
    if os.name == 'nt':        
        locale.setlocale(locale.LC_ALL, 'ru')
        current_month_name = calendar.month_name[current_month_num]
    if os.name == 'posix':
        locale.setlocale(locale.LC_ALL, 'ru_RU')
        current_month_name = calendar.month_name[current_month_num]        
    return current_month_name

# создание календаря для данного месяца
def make_calendar():   
    '''Создадим экземпляр класса calendar, \
       затем получим номера дней данного месяца и сделаем из них список, \
       список отдадим как рез-т работы функции'''
    cal = calendar.Calendar(firstweekday=0)
    date_list = list(cal.itermonthdays(current_year(), current_month_num()))
    return date_list

    
