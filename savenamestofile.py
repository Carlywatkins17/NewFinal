#from beduserinput import beds, getuserresponse

from createnames import name 
import json

# writes the user input/class data to a file as json       
def save_names(names):
    f = open('../NewFinal/the_names_list.json', 'w')
    f.write(' \n')
    #getuserresponse() 
    name_data={}
    name_json=[]

    for key in names:
        n=names[key]
        name_json.append({
            'name': n.gardener_name,
            'garden': n.garden_name,
   
        })
    
    name_data['name'] = name_json
    f.write(json.dumps(name_data))
    f.close()