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

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6 import *
from datetime import date, timedelta, datetime
from createbeds1 import bed
from createplants import plants, herbs, vegetables, flowers
from saveplantstofile import save_plants
from plantuserinput import getuserresponse, plant_names, herb_deets, veg_deets, flower_deets
from beduserinput import getuserresponse,  beds
from size import dimension, soil
from savebedstofile import save_beds
from fertilization import fert_cal, nfd
import json
from os.path import exists

class PlantWitch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a label for the first page
        self.label1 = QLabel("Welcome to Plant Witch 2023!", self)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setStyleSheet("QLabel {color: black; text-align: center; font-size: 100px;}")

        # Create a button for the first page
        self.button1 = QPushButton("Click here to get started", self)
        self.button1.setStyleSheet("QPushButton {background-color: black; font-size: 40px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        #self.button1.setGeometry(50,50,50,500)
        self.button1.clicked.connect(self.page2)

        # Create a layout
        self.vbox = QVBoxLayout(self)
        self.vbox.addStretch()
        self.vbox.addWidget(self.label1)
        self.vbox.setSpacing(100)
        self.vbox.addWidget(self.button1)
        #self.button1.setGeometry(50,50,50,500)
        self.vbox.addStretch()
        self.setLayout(self.vbox)
        self.setGeometry(1000, 1000, 1500, 1000)
        self.setContentsMargins(100,100,100,100)
        self.setWindowTitle("Plant Witch 2023")
        self.setStyleSheet("background-color: green;")
        self.show()

    def page2(self):
        # Remove the widgets from page 1
        self.label1.hide()
        self.button1.hide()

        # Create a label for page 2
        self.label2 = QLabel("What is your name?", self)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setStyleSheet("QLabel {color: black; text-align: center; font-size: 80px;}")

        # Create an entry for page 2
        self.entry1 = QLineEdit(self)
        self.entry1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry1.setStyleSheet("QLineEdit {background-color: black; font-size: 40px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        # Create a label for page 2
        self.label3 = QLabel("What is your garden name?", self)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3.setStyleSheet("QLabel {color: black; text-align: center; font-size: 80px;}")

        # Create an entry for page 2
        self.entry2 = QLineEdit(self)
        self.entry2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry2.setStyleSheet("QLineEdit {background-color: black; font-size: 40px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        # Create a button for page 2
        self.button2 = QPushButton("Next>>", self)
        self.button2.setStyleSheet("QPushButton {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        self.button2.clicked.connect(self.page3)

        # Create a layout
        
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.entry1)
        self.vbox.addStretch()
        self.vbox.addWidget(self.label3)
        self.vbox.addWidget(self.entry2)
        self.vbox.addStretch()
        self.vbox.addWidget(self.button2)
        self.vbox.addStretch()
        self.setContentsMargins(100,100,100,100)

    def page3(self):
        # Remove the widgets from page 2
        self.label2.hide()
        self.entry1.hide()
        self.label3.hide()
        self.entry2.hide()
        self.button2.hide()

        # Get the user input from page 2
        name = self.entry1.text()
        garden_name = self.entry2.text()

        # Create a label for page 3 with the garden name input
        self.label4 = QLabel(garden_name, self)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label4.setStyleSheet("QLabel {color: black; text-align: center; font-size: 40px;}")

        # Create a label for page 3 with the name input
        self.label5 = QLabel(name, self)
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label5.setStyleSheet("QLabel {color: black; text-align: center; font-size: 20px;}")

        # Create a layout
        self.vbox.addWidget(self.label4)
        self.vbox.addWidget(self.label5)
        self.vbox.addStretch()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PlantWitch()
    sys.exit(app.exec())