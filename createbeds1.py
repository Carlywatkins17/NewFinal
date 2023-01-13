# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html




import json
from datetime import datetime, timedelta, date



class bed:
 
    def __init__(self, name='', length=0, width=0, depth=0, sun='', drainage='', ffd='05/01/2023', pfd='07/20/2022', finfd='09/15/2023'):
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.sun = sun
        self.drainage = drainage
        self.ffd = datetime.strptime(ffd, '%m/%d/%Y') 
        self.pfd = datetime.strptime(pfd, '%m/%d/%Y') 
        self.finfd = datetime.strptime(finfd, '%m/%d/%Y') 
   
        
    def toJSON(self):
         return {'name': self.name, 'length': self.length, 'width': self.width, 'depth': self.depth, 'sun': self.sun, 'style': self.style, 'ffd': self.ffd.strptime("%Y-%m-%d"), 'pfd': 
                 self.pfd.strptime("%Y-%m-%d"), 'finfd': self.finfd.strptime("%Y-%m-%d")}


