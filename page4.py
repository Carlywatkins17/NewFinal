#from beduserinput import getuserresponse, beds
#from beduserinputGUI import getuserresponse, beds
#from savebedstofile import save_beds

from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget
from PyQt6.QtCore import Qt
from PyQt6 import *
from size import Size
from fertilization import Fertilization
from storage import beds
from page5 import page5



class page4(QWidget):

    def __init__(self, plantwitch):
        super().__init__()

        self.plantwitch=plantwitch

        # Remove the widgets from page 2
        #self.gardenerlbl.hide()
        #self.gardenerName.hide()
        #self.gardenlbl.hide()
        #self.gardenName.hide()
        #self.nextbtn.hide()


        # Get the user input from page 2
        gardener_name = self.gardenerName.text()
        garden_name = self.gardenName.text()

        
        # Create a label for page 4 with the garden name input
        self.gardenHeader = QLabel(garden_name, self)
        self.gardenHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenHeader.setStyleSheet("QLabel {color: black; text-align: center; font-size: 40px;}")

        # Create a label for page 4 with the name input
        self.gardenerSubhead = QLabel(gardener_name, self)
        self.gardenerSubhead.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gardenerSubhead.setStyleSheet("QLabel {color: black; text-align: center; font-size: 20px;}")


        # schedule and soil questions here 
        self.lblsched = QLabel('Are you on schedule for fertilizing? yes or no:', self)
        self.lblsched.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblsched.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtsched = QLineEdit(self)
        self.txtsched.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtsched.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        
        for b in beds:
            sched = self.txtsched
            if self.txtsched != 'no':
                fert = Fertilization() 
                st = fert.fert_cal()
                self.lblsched.setText(self.lblsched.text + st)  #might need to look this up
            else:
                fert = Fertilization()
                st = fert.nfd()
                self.lblsched.setText(self.lblsched.text + st) 

        self.lblbedsz = QLabel('Do you need the bed size? yes or no: ', self)
        self.lblbedsz.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblbedsz.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtbedsz = QLineEdit(self)
        self.txtbedsz.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtbedsz.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        for b in beds: 
            size = Size()
            st = size.dimension()
            self.lblbedsz.setText(self.lblbedsz.text + st)

        self.lblsoil = QLabel('Do you need to calculate your soil order volume? yes or no: ', self)
        self.lblsoil.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lblsoil.setStyleSheet("QLabel {color: black; text-align: left; font-size: 20px;}")

        self.txtsoil = QLineEdit(self)
        self.txtsoil.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.txtsoil.setStyleSheet("QLineEdit {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")

        for b in beds: 
            soil = Size()
            st = size.soil()
            self.lblsoil.setText(self.lblsoil.text + st)

         # Create next button for page 
        self.nextbtn = QPushButton("Next>>", self)
        self.nextbtn.setStyleSheet("QPushButton {background-color: black; font-size: 20px; border-radius: 8px; border: 1px solid; border-color: orange; padding: 5px 15px; outline: 0px; color: orange;}")
        self.nextbtn.clicked.connect(self.nextpage)

         # create a layout
        self.widget.setLayout(self.vbox)
        self.vbox.addWidget(self.gardenHeader)
        self.vbox.addWidget(self.gardenerSubhead)
        self.vbox.addWidget(self.lblsched)
        self.vbox.addWidget(self.txtsched)
        self.vbox.addWidget(self.lblbedsz)
        self.vbox.addWidget(self.txtbedsz)
        self.vbox.addWidget(self.lblsoil)
        self.vbox.addWidget(self.txtsoil)
        self.vbox.addWidget(self.nextbtn)

      

        def nextpage(self):
            self.plantwitch.change_page(page5(self.plantwitch))

            
   
        #self.setWindowTitle(' ')