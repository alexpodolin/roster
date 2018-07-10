# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:28:19 2018

@author: podolin
"""

import calendar


cal = calendar.Calendar(firstweekday=0)
a = cal.yeardatescalendar(2018, width=3)
print(a)