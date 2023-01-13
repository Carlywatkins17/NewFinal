# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html


from createbeds1 import bed 
from datetime import date, timedelta, datetime

import json

# solicits user input on the garden beds
beds = {}
def getuserresponse():
    QN = input('What is the bed name? Enter "done" if finished:') 
    while QN != 'done':
        QL = input('What is the length of ' + QN + ' ?: ')
        QW = input('What is the width of ' + QN + ' ?: ')
        QD= input('What is the depth of ' + QN + ' ?: ')
        QS= input('Does ' + QN + ' have shade, partial, or full sun?: ')
        QDr= input('Does ' + QN + ' have low, moderate, or high drainage?: ')
        Qffd= input('What was the first fertilization date? If unknown enter 05/10/2023:  ')
        Qpfd= input('What was the last date you fertilized? If unknown enter the date today: ')
        Qfinfd= input('What should be your last fertilization date?  If unknown enter 10/15/2023: ')
   
       
        beds[QN]=bed(QN, QL, QW, QD, QS, QDr, Qffd, Qpfd, Qfinfd)
        
        QN = input('What is the bed name?: Enter "done" if finished: \n') #this line isnt working as intended.  I dont think I understand loops. 

        #If I enter a new bed name instead of entering "done" here, it will write both to the file, but as a single line. 
