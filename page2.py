#from datetime import date, timedelta, datetime
#from createbeds1 import bed
#from createplants import plants, herbs, vegetables, flowers
#from saveplantstofile import save_plants
#from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
#from beduserinput import getuserresponse, beds
#from beduserinputGUI import getuserresponse, beds
#from size import dimension, soil
#from savebedstofile import save_beds
#from fertilization import fert_cal, nfd
#from userinteractiontest import PlantWitch, change_pg


import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QScrollArea, QScrollBar, QMainWindow
from PyQt6.QtCore import Qt, QSize
from PyQt6 import *
from page3 import page3
from createnames import name 
from savenamestofile import save_names
from storage import names 
import json
from os.path import exists
from flask import Flask, request, render_template   

class page2(QWidget):

    def __init__(self, plantwitch, names):
        super().__init__()

        self.plantwitch=plantwitch
        self.names = names 
       

        # Create a label for page 2
        self.gardenerlbl = QLabel("What is your name?", self)
        self.gardenerlbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenerlbl.setStyleSheet("QLabel {color: black; text-align: center; font-size: 80px;}")

        # Create an entry for page 2
        self.gardenerName = QLineEdit(self)
        self.gardenerName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenerName.setStyleSheet("QLineEdit {background-color: black; font-size: 40px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        # Create a label for page 2
        self.gardenlbl = QLabel("What is your garden name?", self)
        self.gardenlbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenlbl.setStyleSheet("QLabel {color: black; text-align: center; font-size: 80px;}")

        # Create an entry for page 2
        self.gardenName = QLineEdit(self)
        self.gardenName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenName.setStyleSheet("QLineEdit {background-color: black; font-size: 40px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        # Create a button for page 2
        self.nextbtn = QPushButton("Next>>", self)
        self.nextbtn.setStyleSheet("QPushButton {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        self.nextbtn.clicked.connect(self.nextpage)

        # Create a layout
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.gardenerlbl)
        self.vbox.addWidget(self.gardenerName)
        self.vbox.addStretch()
        self.vbox.addWidget(self.gardenlbl)
        self.vbox.addWidget(self.gardenName)
        self.vbox.addStretch()
        self.vbox.addWidget(self.nextbtn)
        self.vbox.addStretch()
        self.setContentsMargins(100,100,100,100)


    def nextpage(self):

        GDN = self.gardenerName.text() 
        GN = self.gardenName.text()

        self.names[GDN]=name(GDN, GN) 

        save_names(self.names) 

        self.plantwitch.change_page(page3)
    #self.plantwitch.change_page(page2(self.plantwitch))
        

