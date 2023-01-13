# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html


from createbeds1 import bed 
from beduserinput import beds 
import json
from savebedstofile import save_beds

#calculates the size of the bed 



def dimension():
    for s in beds:
        bed=beds[s] 
        print(bed.name + " is " + str(int(bed.length)*int(bed.width)) + " sq ft" ) 


                    


# solicits user input on which beds need more soil and calculates the volume needed in units that the product is sold in.

def soil():
    for s in beds:
        bed=beds[s]
        print('You need ' + str((int(bed.length) * int(bed.width) * int(bed.depth))/27) + " cubic yards of soil")
