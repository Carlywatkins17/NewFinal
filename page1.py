# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
# User Burnash, https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python, 
# edited June 9 2021, accessed October 31 2022
#  https://forum.qt.io/topic/130569/center-align-in-pyqt6-python/5
# This code was inspired by suggestions provided by an OpenAI's GPT-3 model 
# (https://openai.com) on January 16th 2023
#https://python-commandments.org/pyqt-stylesheet/
#https://www.pythontutorial.net/pyqt/qt-style-sheets/
#https://stackoverflow.com/questions/10082299/qvboxlayout-how-to-vertically-align-widgets-to-the-top-instead-of-the-center
#https://www.pythonguis.com/tutorials/pyqt6-qscrollarea/ This is how I learned to add a scroll bar

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
from datetime import date, timedelta, datetime
from page2 import page2
import json
from os.path import exists
from storage import names


class page1(QWidget):

    def __init__(self, plantwitch):
        super().__init__()


        self.plantwitch=plantwitch  
        
        self.welcomelbl = QLabel("Welcome to Plant Witch 2023!")
        self.welcomelbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcomelbl.setStyleSheet("QLabel {color: black; text-align: center; font-size: 100px;}")

        # Create a button for the first page
        self.welcomebtn = QPushButton("Click here to get started")
        self.welcomebtn.setStyleSheet("QPushButton {background-color: black; font-size: 40px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        #self.button1.setGeometry(50,50,50,500)
        self.welcomebtn.clicked.connect(self.nextpage)

        # Create a layout
        self.vbox = QVBoxLayout(self)
        self.vbox.addStretch()
        self.vbox.addWidget(self.welcomelbl)
        self.vbox.setSpacing(100)
        self.vbox.addWidget(self.welcomebtn)

        #self.button1.setGeometry(50,50,50,500)
        
        self.setLayout(self.vbox)
        self.setGeometry(1000, 1000, 1500, 1000)
        self.setContentsMargins(100,100,100,100)
        self.setWindowTitle("Plant Witch 2023")
        self.setStyleSheet("background-color: green;")

    def nextpage(self):
        self.plantwitch.change_page(page2)
        #self.plantwitch.change_page(page2(self.plantwitch))