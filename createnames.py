# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html




import json
from datetime import datetime, timedelta, date

class name:
 
    def __init__(self, gardener_name='', garden_name='' ):
        self.gardener_name = gardener_name                              
        self.garden_name = garden_name
        
       
    def toJSON(self):
         return {'gardener_name':self.gardener_name, 'garden_name': self.garden_name}