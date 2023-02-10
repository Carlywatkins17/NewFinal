import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QScrollArea, QScrollBar, QMainWindow
from PyQt6.QtCore import Qt, QSize
from PyQt6 import *
from datetime import date, timedelta, datetime
from createbeds1 import bed
from createplants import plants, herbs, vegetables, flowers
from saveplantstofile import save_plants
from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
#from beduserinput import getuserresponse, beds
#from beduserinputGUI import getuserresponse, beds
#from size import dimension, soil
#from savebedstofile import save_beds
#from fertilization import fert_cal, nfd
from userinteractiontest import PlantWitch
from page6 import page6
import json
from os.path import exists

class pag5(QWidget):

    def __init__(self, plantwitch):
        super().__init__()

        # Remove the widgets from page 3
        self.gardenerlbl.hide()
        self.gardenerName.hide()
        self.gardenlbl.hide()
        self.gardenName.hide()
        self.nextbtn.hide()

         # Get the user input from page 2
        name = self.gardenerName.text()
        garden_name = self.gardenName.text()

        
        # Create a label for page 4 with the garden name input
        self.gardenHeader = QLabel(garden_name, self)
        self.gardenHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenHeader.setStyleSheet("QLabel {color: black; text-align: center; font-size: 40px;}")

        # Create a label for page 4 with the name input
        self.gardenerSubhead = QLabel(name, self)
        self.gardenerSubhead.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenerSubhead.setStyleSheet("QLabel {color: black; text-align: center; font-size: 20px;}")

        # Begin integrating  plantuserinput questions here 
        self.lblpname = QLabel('What is the plant name? enter "done" if finished: ', self)
        self.lblpname.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpname.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpname = QLineEdit(self)
        self.txtpname.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpname.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblqty = QLabel('How many ' + self.txtpname.text() + ' do you have currently?: ', self)
        self.lblqty.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblqty.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtqty = QLineEdit(self)
        self.txtqty.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtqty.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblpsun = QLabel('How much sun does ' + self.txtpname.text() + ' need?: ', self)
        self.lblpsun.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpsun.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpsun = QLineEdit(self)
        self.txtpsun.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpsun.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblpdrain = QLabel('Does ' + self.txtpname.text() + ' need low, moderate, or high drainage?: ', self)
        self.lblpdrain.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpdrain.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpdrain = QLineEdit(self)
        self.txtpdrain.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpdrain.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblwtr = QLabel('What are the water needs for ' + self.txtpname.text()  + ' ?: ', self)
        self.lblwtr.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblwtr.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtwtr = QLineEdit(self)
        self.txtwtr.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtwtr.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblpbed = QLabel('What bed is ' + self.txtpname.text()  + ' in?: ', self)
        self.lblpbed.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpbed.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpbed = QLineEdit(self)
        self.txtpbed.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpbed.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblsesn = QLabel('What is the seasonality of ' + self.txtpname.text()  + ' ?: ', self)
        self.lblsesn.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblsesn.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtsesn = QLineEdit(self)
        self.txtsesn.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtsesn.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblpfert = QLabel('What are the fertlization needs of ' + self.txtpname.text() + ' ?: ', self)
        self.lblpfert.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpfert.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpfert = QLineEdit(self)
        self.txtpfert.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpfert.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblsow = QLabel('When do you sow ' + self.txtpname.text() + ' ?: ', self)
        self.lblsow.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblsow.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtsow = QLineEdit(self)
        self.txtsow.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtsow.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblsowlo = QLabel('Do you sow ' + self.txtpname.text() + ' indoors or in ground?: ', self)
        self.lblsowlo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblsowlo.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtsowlo = QLineEdit(self)
        self.txtsowlo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtsowlo.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblpdep = QLabel('How deep do you sow ' + self.txtpname.text() + ' ?: ', self)
        self.lblpdep .setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpdep .setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpdep  = QLineEdit(self)
        self.txtpdep .setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpdep .setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblpspc = QLabel('What is the plant spacing for ' + self.txtpname.text() + ' ?: ', self)
        self.lblpspc.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpspc.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpspc = QLineEdit(self)
        self.txtpspc.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpspc.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lbltall = QLabel('How tall does ' + self.txtpname.text() + ' get?: ', self)
        self.lbltall.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lbltall.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txttall = QLineEdit(self)
        self.txttall.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txttall.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblgerm = QLabel('How long does it take for ' + self.self.txtpname.text() + ' to germinate?: ', self)
        self.lblgerm.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblgerm.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtgerm = QLineEdit(self)
        self.txtgerm.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtgerm.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblnote = QLabel('Please enter any additional notes about ' + self.txtpname.text() + ' here: ', self)
        self.lblnote.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblnote.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtnote = QLineEdit(self)
        self.txtnote.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtnote.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lblptyp = QLabel('Is ' + self.txtpname.text() + ' an herb, vegetable, or flower?: ', self)
        self.lblptyp.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblptyp.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtptyp = QLineEdit(self)
        self.txtptyp.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtptyp.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")


        #INTEGRATE SUB CLASS GUI OBJECTS#

        if self.txtptyp.text()  == 'herb':
            
            self.lblhsmdg = QLabel('Can you use ' + self.txtpname.text() + ' for smudge?: ', self)
            self.lblhsmdg.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblhsmdg.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txthsmdg  = QLineEdit(self)
            self.txthsmdg.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txthsmdg.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblptyp)
            self.vbox.addWidget(self.txtptyp)

            
            self.lblhsmk = QLabel('Can you smoke ' + self.txtpname.text() + ' ?: ', self)
            self.lblhsmk.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblhsmk.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txthsmk = QLineEdit(self)
            self.txthsmk.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txthsmk.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblhsmk)
            self.vbox.addWidget(self.txthsmk)

            self.lblhedbl = QLabel('Is ' + self.txtpname.text() + ' edible?:', self)
            self.lblhedbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblhedbl.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txthedbl = QLineEdit(self)
            self.txthedbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txthedbl.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblhedbl)
            self.vbox.addWidget(self.txthedbl)
            
            # does this go in my next page function?
            #self.herb_deets[QN]=herbs(QBr, QSm, QE)

        if self.txtptyp.text() == 'vegetable':
            
            self.lblhvst = QLabel('When do you harvest ' + self.txtpname.text()  + '?: ', self)
            self.lblhvst.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblhvst.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txthvst = QLineEdit(self)
            self.txthvst.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txthvst.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblhvst)
            self.vbox.addWidget(self.txthvst)

            #does this go in the nextpage function below?
            #self.veg_deets[QN]=vegetables(QR)
            
            
        if self.txtptyp.text() == 'flower':
            
            self.lblclr = QLabel('What colors are ' + self.txtpname.text()  + ' ?: ', self)
            self.lblclr.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblclr.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txtclr = QLineEdit(self)
            self.txtclr.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txtclr.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblclr)
            self.vbox.addWidget(self.txtclr)

    
            self.lblpsn = QLabel('Is ' + self.txtpname.text() + ' poisonous?: ', self)
            self.lblpsn.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblpsn.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txtpsn = QLineEdit(self)
            self.txtpsn.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txtpsn.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblpsn)
            self.vbox.addWidget(self.txtpsn)

            
            self.lblfsmk = QLabel('Can you smoke ' + self.txtpname.text() + ' ?: ', self)
            self.lblfsmk.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblfsmk.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txtfsmk  = QLineEdit(self)
            self.txtfsmk.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txtfsmk.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblfsmk)
            self.vbox.addWidget(self.txtfsmk)

            
            self.lblfsmdg = QLabel('Can you use ' + self.txtpname.text() + ' for smudge?: ', self)
            self.lblfsmdg.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblfsmdg.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txtfsmdg = QLineEdit(self)
            self.txtfsmdg.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txtfsmdg.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblhfsmdg)
            self.vbox.addWidget(self.txtfsmdg)

            
            self.lblfedbl = QLabel('Is ' + self.txtpname.text()  + ' edible?:', self)
            self.lblfedbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.lblfedbl.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

            self.txtfedbl = QLineEdit(self)
            self.txtfedbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.txtfedbl.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
           
            #How do you handle the layout if the objects are conditional?  Is this where they go?
            self.vbox.addWidget(self.lblfedbl)
            self.vbox.addWidget(self.txtfedbl)

            #does this go in the next page function?
            #flower_deets[QN]=flowers(QC, QSf, QSm_f, QBr_f, QE_f)

        #IS this where and how I want to ask for repeat entries?    
        QN = input('What is the plant name? enter "done" if finished: ') 

         # Create next button for page 
        self.nextbtn = QPushButton("Next>>", self)
        self.nextbtn.setStyleSheet("QPushButton {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        self.nextbtn.clicked.connect(self.nextpage)

         # create a layout
        self.widget.setLayout(self.vbox)
        self.vbox.addWidget(self.gardenHeader)
        self.vbox.addWidget(self.gardenerSubhead)
        self.vbox.addWidget(self.lblpname)
        self.vbox.addWidget(self.txtpname)
        self.vbox.addWidget(self.lblqty)
        self.vbox.addWidget(self.txtqty)
        self.vbox.addWidget(self.lblpsun)
        self.vbox.addWidget(self.txtpsun)
        self.vbox.addWidget(self.lblpdrain)
        self.vbox.addWidget(self.txtpdrain)
        self.vbox.addWidget(self.lblwtr)
        self.vbox.addWidget(self.txtwtr)
        self.vbox.addWidget(self.lblpbed)
        self.vbox.addWidget(self.txtpbed)
        self.vbox.addWidget(self.lblsesn)
        self.vbox.addWidget(self.txtsesn)
        self.vbox.addWidget(self.lblpfert)
        self.vbox.addWidget(self.txtpfert)
        self.vbox.addWidget(self.lblsow)
        self.vbox.addWidget(self.txtsow)
        self.vbox.addWidget(self.lblsowlo)
        self.vbox.addWidget(self.txtsowlo)
        self.vbox.addWidget(self.lblpdep)
        self.vbox.addWidget(self.txtpdep)
        self.vbox.addWidget(self.lblpspc)
        self.vbox.addWidget(self.txtpspc)
        self.vbox.addWidget(self.lbltall)
        self.vbox.addWidget(self.txttall)
        self.vbox.addWidget(self.lblgerm)
        self.vbox.addWidget(self.txtgerm)
        self.vbox.addWidget(self.lblnote)
        self.vbox.addWidget(self.txtnote)
        self.vbox.addWidget(self.lblptyp)
        self.vbox.addWidget(self.txtptyp)


        

        self.vbox.addWidget(self.nextbtn)
        
        def nextpage(self):
         
            QN = self.txtpname.text() 
            Q = self.txtqty.text()
            QS = self.txtpsun.text()
            QDr= self.txtpdrain.text()
            QW= self.txtwtr.text()
            QB= self.txtpbed.text()
            QSe= self.txtsesn.text()
            QF= self.txtpfert.text()
            QTm= self.txtsow.text()
            QL= self.txtsowlo.text()
            QDp= self.txtpdep.text()
            QSp= self.txtpspc.text()
            QH= self.txttall.text()
            QG= self.txtgerm.text()
            QP= self.txtnote.text()
            QT= self.txtptyp.text()

            QBr = self.txthsmdg.text()
            QSm = self.txthsmk.text()
            QE = self.txthedbl.text()

            QR = self.txthvst.text()

            QC = self.txtclr.text()
            QSf = self.txtpsn.text()
            QSm_f = self.txtfsmk.text()
            QBr_f = self.txtfsmdg.text()
            QE_f = self.txtfedbl.text()
        
    
            self.plant_names[QN]=plants(QN, Q, QS, QDr, QW, QB, QSe, QF, QTm, QL, QDp, QSp, QH, QG, QP, QT)
            self.herb_deets[QN]=herbs(QBr, QSm, QE)
            self.veg_deets[QN]=vegetables(QR)
            self.flower_deets[QN]=flowers(QC, QSf, QSm_f, QBr_f, QE_f)

            save_plants(plant_names)

            self.plantwitch.change_pg(page6(self.plantwitch))
        
        #self.setWindowTitle(' ')