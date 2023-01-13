# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html


from createbeds1 import bed 
from datetime import date, timedelta, datetime
from beduserinput import beds, getuserresponse
import json

# writes the user input/class data to a file as json       
def save_beds():
    f = open('../NewFinal/the_beds_list.json', 'w')
    f.write(' \n')
    getuserresponse() 
    bed_data={}
    bed_json=[]

    for key in beds:
        b=beds[key]
        bed_json.append({
            'name': b.name,
            'length': b.length,
            'width': b.width,
            'depth': b.depth,
            'ffd': b.ffd.strftime('%Y-%m-%d'),  # convert datetime object to string
            'finfd': b.finfd.strftime('%Y-%m-%d'),  # convert datetime object to string
            'pfd': b.pfd.strftime('%Y-%m-%d')  # convert datetime object to string
        })
    
    bed_data['bed'] = bed_json
    f.write(json.dumps(bed_data))
    f.close()
            
                            


def load_beds():
    f = open('../data/plants.json', 'r')
    bed_data=json.loads(f.read())
    f.close()
    for b in bed_data['bed']:
        beds[b['name']] = bed(b['name'], b['length'], b['width'], b['depth'], b['sun'], b['drainage'], datetime.strptime(b['ffd'], '%Y-%m-%d'), datetime.strptime(b['finfd'],
         '%Y-%m-%d'), datetime.strptime(b['pfd'], '%Y-%m-%d'))
