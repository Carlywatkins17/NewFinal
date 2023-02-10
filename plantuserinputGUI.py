from createplants import plants, herbs, vegetables, flowers
import json 

# solicits user input on the plants
plant_names = {}
herb_deets = {}
veg_deets = {}
flower_deets = {}


#plant_names = []
#herb_deets = []
#veg_deets = []
#flower_deets = []
def getuserresponse():
    QN = input('What is the plant name? enter "done" if finished: ') 
    while QN != 'done':
        Q = input('How many ' + QN + ' do you have currently?: ')
        QS = input('How much sun does ' + QN + ' need?: ')
        QDr= input('Does ' + QN + ' need low, moderate, or high drainage?: ')
        QW= input('What are the water needs for ' + QN + ' ?: ')
        QB = input('What bed is ' + QN + ' in?: ')
        QSe = input('What is the seasonality of ' + QN + ' ?: ')
        QF = input('What are the fertlization needs of ' + QN + ' ?: ')
        QTm = input('When do you sow ' + QN + ' ?: ')
        QL = input('Do you sow ' + QN + ' indoors or in ground?: ')
        QDp = input('How deep do you sow ' + QN + ' ?: ')
        QSp = input('What is the plant spacing for ' + QN + ' ?: ')
        QH = input('How tall does ' + QN + ' get?: ')
        QG = input('How long does it take for ' + QN + ' to germinate?: ')
        QP = input('Please enter any additional notes about ' + QN + ' here: ')
        QT = input('Is ' + QN + ' an herb, vegetable, or flower?: ')

        #plant_names.append(plants(QN, Q, QS, QDr, QW, QB, QSe, QF, QTm, QL, QDp, QSp, QH, QG, QP, QT)
        # )

        plant_names[QN]=plants(QN, Q, QS, QDr, QW, QB, QSe, QF, QTm, QL, QDp, QSp, QH, QG, QP, QT)

        if QT == 'herb':
            QBr = input('Can you use ' + QN + ' for smudge?: ')
            QSm = input('Can you smoke ' + QN + ' ?: ')
            QE = input('Is ' + QN + ' edible?:')
            #herb_deets.append(herbs(QBr, QSm, QE))
            
            herb_deets[QN]=herbs(QBr, QSm, QE)
            
        if QT == 'vegetable':
            QR = input('When do you harvest ' + QN + '?: ')
            #veg_deets.append(vegetables(QR))
            veg_deets[QN]=vegetables(QR)
            
            
        if QT == 'flower':
            QC = input('What colors are ' + QN + ' ?: ')
            QSf = input('Is ' + QN + ' poisonous?: ')
            QSm_f = input('Can you smoke ' + QN + ' ?: ')
            QBr_f = input('Can you use ' + QN + ' for smudge?: ')
            QE_f = input('Is ' + QN + ' edible?:')
            #flower_deets.append(flowers(QC, QSf, QSm_f, QBr_f, QE_f))
            flower_deets[QN]=flowers(QC, QSf, QSm_f, QBr_f, QE_f)
           
        QN = input('What is the plant name? enter "done" if finished: ') 

#getuserresponse()

        
  
        #QN = input('What is the plant name?:') 