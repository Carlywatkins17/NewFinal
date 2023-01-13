
# https://www.geeksforgeeks.org/calling-a-super-class-constructor-in-python/ this is where I read about subclasses.  This site did not suggest the "subclass" part in the 
# constructor init though. That was this tool. 
 
import json

class plants():
    def __init__(self,  name='', quantity=int, sun='full', drainage='high', water='', bed='', seasonality='perrenial', storage='', fert ='', sow_time='', sow_loc='',
                 sow_depth='', sow_space='', p_height='', germ_time='', notes=''): 
        self.name = name
        self.quantity = quantity
        self.sun = sun
        self.drainage = drainage 
        self.water = water
        self.bed = bed
        self.seasonality = seasonality
        self.storage = storage
        self.fert = fert
        self.sow_time = sow_time
        self.sow_loc = sow_loc
        self.sow_depth = sow_depth
        self.sow_space = sow_space
        self.height = p_height 
        self.germ_time = germ_time       
        self.notes = notes     

    def toJSON(self):
        return self.__dict__   
        
#CONTROL + H DOES FIND AND REPLACE

class herbs(plants):
    def __init__(self, name='', quantity=int, sun='full', drainage='high', water='', bed='', seasonality='perrenial', smoke='N', burn='Y', edible='Y', storage='', fert='',
                 sow_time='', sow_loc='', sow_depth='', sow_space='', p_height='', germ_time='', notes=''):
        plants.__init__(self, name, quantity, sun, drainage, water, bed, seasonality, storage, fert, sow_time, sow_loc, sow_depth, sow_space, p_height, germ_time, notes,)

        self.smoke = smoke
        self.burn = burn
        self.edible = edible

    def toJSON(self):
        return self.__dict__    

class vegetables(plants):
    def __init__(self, name='', quantity=int, sun='full', drainage='moderate', water='daily', bed='', seasonality='perrenial', storage='', reap='', fert='', sow_time='', 
                 sow_loc='', sow_depth='', sow_space='', p_height='', germ_time='', notes = ''):
        plants.__init__(self, name, quantity, sun, drainage, water, bed, seasonality, storage, fert, sow_time, sow_loc, sow_depth, sow_space, p_height, germ_time, notes)
    
        self.reap= reap
        
    def toJSON(self):
        return self.__dict__ 

class flowers(plants):
    def __init__(self, name='', quantity=int, color='', safety='', sun='full', drainage='moderte', water='daily', bed='', seasonality='', storage='', smoke='N', burn='', 
                edible='', fert='', sow_time='', sow_loc='', sow_depth='', sow_space='', p_height='', germ_time='', notes=''):
        plants.__init__(self, name, quantity, sun, drainage, water, bed, seasonality, storage, fert, sow_time, sow_loc, sow_depth, sow_space, p_height, germ_time, notes)

        self.color = color
        self.safety= safety
        self.smoke = smoke
        self.burn = burn
        self.edible = edible
    def toJSON(self):
        return self.__dict__ 
