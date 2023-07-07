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
#from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
#from beduserinput import getuserresponse, beds
#from beduserinputGUI import getuserresponse, beds
#from size import dimension, soil
#from savebedstofile import save_beds
#from fertilization import fert_cal, nfd
#getuserresponse(beds)
#save_beds(beds)
#getuserresponse(plant_names)
#save_plants(plant_names)



import sys
from typing import Self
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QScrollArea, QMainWindow, QPushButton, QWidget
from PyQt6.QtCore import Qt
from PyQt6 import *
from PyQt6 import uic
from page1 import page1
from os.path import exists



class PlantWitch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.names={}
        self.beds={}
        self.initUI()
        

    def initUI(self):

        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = page1(self)                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout() 
        
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.button = QPushButton("Change Page")
        self.button.clicked.connect(lambda: self.change_page(page1))
        self.vbox.addWidget(self.button)

        self.vbox.addWidget(self.scroll)
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.vbox)
        #self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle(' ')
        self.show() 

    def change_page(self,page):
        #self.widget=page(self)
        self.widget=page(self, self.names)
        self.scroll.setWidget(self.widget)   

             
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PlantWitch()
    sys.exit(app.exec())
    