# Carly Watkins
# 10/31/22
# CS-100A - Final project
# License: Copyright 2022 Carly Watkins
# Resources used: https://google.github.io/styleguide/pyguide.html
# https://www.geeksforgeeks.org/python-datetime-strptime-function/
# User Burnash, https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python, edited June 9 2021, accessed October 31 2022

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
from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("Plant Witch 2023")

        a = QLabel(self)
        a.setText('Welcome to Plant-Witch 2023!')

        labels = ['first name', 'last name', 'email']
        self.textboxes = {}

        layout = QFormLayout()
        self.setLayout(layout)

        for l in labels:
            #now add a label and a textbox,
            # and also hold the textbox in the dictionary so we can use it later
            txt = QLineEdit()
            layout.addRow(l, txt)
            self.textboxes[l] = txt

        #finally, add a button
        b = QPushButton("Submit")
        b.clicked.connect(self.button_clicked)
        layout.addWidget(b)

        #Create a label, leave it empty, and add it to the bottom
        self.labelResult = QLabel()
        layout.addWidget(self.labelResult)

        self.show()
    
    def button_clicked(self):
        self.labelResult.setText(self.self.textboxes['first name'].text())

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()