from createbeds import Bed
from datetime import timedelta

def fert_cal(bed):
    delta = timedelta(weeks=2)
    cal = 'Here is your fertilization calendar: \n'
    start_date = bed.ffd
    end_date = bed.finfd
    while start_date <= end_date:
        cal += str(start_date) + '\n'
        start_date += delta
    return cal

def nfd(bed):
    delta = timedelta(weeks=2)
    schedule = 'Here is your fertilization schedule: \n'
    start_date = bed.pfd
    end_date = bed.finfd
    while start_date <= end_date:
        schedule += str(start_date) + '\n'
        start_date += delta
    return schedule
