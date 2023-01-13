# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html


from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
from createplants import plants, herbs, vegetables, flowers
import json
  
# writes the user input/class data to a file        
def save_plants():
    f = open('plants.json', 'w')
    #f.write(' \n')
    getuserresponse() 
    plant_data={}
    plant_json=[]
    herb_json=[]
    vegetable_json=[]
    flower_json=[]
    
    for key in plant_names:
        p=plant_names[key]
        plant_json.append(p.toJSON())

    plant_data['plant']=plant_json

    for key in herb_deets:
        h=herb_deets[key]
       
        herb_json.append(h.toJSON())

   
    plant_data['herb']=herb_json
       
    for key in veg_deets:
        v=veg_deets[key]
       
        vegetable_json.append(v.toJSON())
    
    plant_data['vegetable']=vegetable_json

    for key in flower_deets:
        fl=flower_deets[key]
        flower_json.append(fl.toJSON())

    
    plant_data['flower']=flower_json

    f.write(json.dumps(plant_data))
