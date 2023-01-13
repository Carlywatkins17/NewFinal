# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
# User Burnash, https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python, edited June 9 2021, accessed October 31 2022

from createbeds1 import bed 
from datetime import date, timedelta, datetime
from beduserinput import beds


#creates a calendar of that years recommended fertilization dates for that bed


def fert_cal():
    delta = timedelta(weeks=2)
    
    
    for b in beds:
        bed=beds[b]
        print('Here is your fertilization calendar: ')

        start_date = bed.ffd
        end_date = bed.finfd
        while start_date <= end_date:
            print(start_date)
            start_date += delta 
 

def nfd():
    delta = timedelta(weeks=2)
    print('Here is your fertilization schedule: ')
    for b in beds:
        bed=beds[b]
        start_date = bed.pfd
        end_date = bed.finfd
        while start_date <= end_date:
            print(start_date)
            start_date += delta
