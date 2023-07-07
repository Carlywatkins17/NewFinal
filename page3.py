#from createplants import plants, herbs, vegetables, flowers
#from saveplantstofile import save_plants
#from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
#from beduserinput import getuserresponse, beds
#from beduserinputGUI import getuserresponse, beds
#from size import dimension, soil
#from fertilization import fert_cal, nfd
#from userinteractiontest import PlantWitch

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QScrollArea, QScrollBar, QMainWindow
from PyQt6.QtCore import Qt, QSize
from PyQt6 import *
from datetime import date, timedelta, datetime
from createbeds1 import bed
from createnames import name
from savebedstofile import save_beds
from savenamestofile import save_names
from storage import beds, names

from page4 import page4
import json
from os.path import exists
from flask import Flask, request, render_template

class page3(QWidget):

    def __init__(self, plantwitch, names):
        super().__init__()

        self.plantwitch=plantwitch  
        self.names = names

        # Remove the widgets from page 2
        #self.gardenerlbl.hide()
        #self.gardenerName.hide()
        #self.gardenlbl.hide()
        #self.gardenName.hide()
        #self.nextbtn.hide()


        # Get the user input from page 2
        name = self.gardenerName.text()
        garden_name = self.gardenName.text()

        
        # Create a label for page 3 with the garden name input
        self.gardenHeader = QLabel(garden_name, self)
        self.gardenHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenHeader.setStyleSheet("QLabel {color: black; text-align: center; font-size: 40px;}")

        # Create a label for page 3 with the name input
        self.gardenerSubhead = QLabel(name, self)
        self.gardenerSubhead.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenerSubhead.setStyleSheet("QLabel {color: black; text-align: center; font-size: 20px;}")

        # Begin integrating beduserinput  here 
        self.lblbed = QLabel('What is the bed name? Enter "done" if finished:', self)
        self.lblbed.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblbed.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        
        self.txtbed = QLineEdit(self)
        self.txtbed.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtbed.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        
        self.lblLength = QLabel("What is the length of " + self.txtbed.text()  + "?", self)
        self.lblLength.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblLength.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        
        self.txtLength = QLineEdit(self)
        self.txtLength.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtLength.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        
        self.lblwidth = QLabel("What is the width of " + self.txtbed.text() + "?", self)
        self.lblwidth.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblwidth.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        
        self.txtwidth = QLineEdit(self)
        self.txtwidth.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtwidth.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lbldepth = QLabel("What is the depth of " + self.txtbed.text() + "?", self)
        self.lbldepth.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lbldepth.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        
        self.txtdepth = QLineEdit(self)
        self.txtdepth.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtdepth.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        
        self.lblsun = QLabel('Does ' + self.txtbed.text() + ' have shade, partial, or full sun?: ', self)
        self.lblsun.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblsun.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtsun = QLineEdit(self)
        self.txtsun.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtsun.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        self.lbldrain = QLabel('Does ' + self.txtbed.text() + ' have low, moderate, or high drainage?: ', self)
        self.lbldrain.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lbldrain.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtdrain = QLineEdit(self)
        self.txtdrain.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtdrain.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        
        self.lblffd = QLabel('What was the first fertilization date? If unknown enter 05/10/2023:  ', self)
        self.lblffd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblffd.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtffd = QLineEdit(self)
        self.txtffd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtffd.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        
        self.lblpfd = QLabel('What was the last date you fertilized? If unknown enter the date today: ', self)
        self.lblpfd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblpfd.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtpfd = QLineEdit(self)
        self.txtpfd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtpfd.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        
        self.lblfinfd = QLabel('What should be your final fertilization date?  If unknown enter 10/15/2023: ', self)
        self.lblfinfd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblfinfd.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtfinfd = QLineEdit(self)
        self.txtfinfd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtfinfd.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

         # Create next button for page 3
        self.nextbtn = QPushButton("Next>>", self)
        self.nextbtn.setStyleSheet("QPushButton {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        self.nextbtn.clicked.connect(self.nextpage)

    

        # create a layout
        self.widget.setLayout(self.vbox)
        self.vbox.addWidget(self.gardenHeader)
        self.vbox.addWidget(self.gardenerSubhead)
        self.vbox.addWidget(self.lblbed)
        self.vbox.addWidget(self.txtbed)
        self.vbox.addWidget(self.lblLength)
        self.vbox.addWidget(self.txtLength)
        self.vbox.addWidget(self.lblwidth)
        self.vbox.addWidget(self.txtwidth)
        self.vbox.addWidget(self.lbldepth)
        self.vbox.addWidget(self.txtdepth)
        self.vbox.addWidget(self.lblsun)
        self.vbox.addWidget(self.txtsun)
        self.vbox.addWidget(self.lbldrain)
        self.vbox.addWidget(self.txtdrain)
        self.vbox.addWidget(self.lblffd)
        self.vbox.addWidget(self.txtffd)
        self.vbox.addWidget(self.lblpfd)
        self.vbox.addWidget(self.txtpfd)
        self.vbox.addWidget(self.lblfinfd)
        self.vbox.addWidget(self.txtfinfd)
        self.vbox.addWidget(self.nextbtn)


    def nextpage(self):
            
        QN = self.txtbed.text() 
        QL = self.txtLength.text()
        QW = self.txtwidth.text()
        QD= self.txtdepth.text()
        QS= self.txtsun.text()
        QDr= self.txtdrain.text()
        Qffd= self.txtffd.text()
        Qpfd= self.txtpfd.text()
        Qfinfd= self.txtfinfd.text()
        
        self.beds[QN]=bed(QN, QL, QW, QD, QS, QDr, Qffd, Qpfd, Qfinfd)
            
        save_beds(beds)

        GDN = self.gardenerName.text()
        GN = self.gardenName.text()

        self.names[GDN]=name(GDN, GN)

        save_names(self.names)

        self.plantwitch.change_page(page4)
            

            

        #self.setWindowTitle(' ')

    
                
