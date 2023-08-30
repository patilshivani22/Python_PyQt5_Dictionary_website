import sys                #provide(access to some variables) info about constants,functions,methods
from PyQt5 import QtWidgets    #UI control that provides the basic application constructor
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow
from PyQt5.uic import loadUi
from wordhoard import Definitions, Homophones, Synonyms, Antonyms     #Library of Dictionary

class Choose(QDialog):
    def __init__(self):   #constructor in object oriented concepts   #self is our main window object.
        super(Choose, self).__init__()          #super() function returns objects represented in the parent's class 
        loadUi("choose.ui",self)
        self.englishButton.clicked.connect(self.gotoengD)
        self.maths.clicked.connect(self.gotomathsD)

    def gotoengD(self):
        eng = Eng()      #creation of eng object for class Eng
        widget.addWidget(eng)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomathsD(self):
        ari=Ari()       #creation of ari obj for class Ari
        widget.addWidget(ari)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class Eng(QDialog):
    def __init__(self):
        super(Eng, self).__init__()        
        loadUi("EnglishDictionary.ui",self)
        self.b6.clicked.connect(self.definitions)
        self.goback.clicked.connect(self.gotochoose)
    
    def definitions(self):
        w = str(self.word.text())
        d = Definitions(w)
        d_r = d.find_definitions()
        s =  Synonyms(w)
        s_r = s.find_synonyms()
        a =  Antonyms(w)
        a_r = a.find_antonyms()
        h =  Homophones(w)
        h_r = h.find_homophones()
        self.mean.setText(str(d_r))
        #self.view.setLayoutDirection(QtCore.Qt.RightToLeft)     
        self.syno.setText(str(s_r))
        self.homo.setText(str(h_r))
        self.anto.setText(str(a_r))

    def gotochoose(self):
        choose = Choose()
        widget.addWidget(choose)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Ari(QDialog):
    def __init__(self):
        super(Ari, self).__init__()    
        loadUi("untitled1.ui",self)        
        self.b1.clicked.connect(self.Addition)
        self.b2.clicked.connect(self.Substract)
        self.b3.clicked.connect(self.Multiply)
        self.b4.clicked.connect(self.Divide)
        self.goback1.clicked.connect(self.gotochoose1)
        
    def Addition(self):
        v1 = int(self.n1.text())
        v2 = int(self.n2.text())
        v3 = v1 + v2
        self.res.setText(str(v3))

    def Substract(self):
        v1 = int(self.n1.text())
        v2 = int(self.n2.text())
        v3 = v1 - v2
        self.res.setText(str(v3))

    def Multiply(self):
        v1 = int(self.n1.text())
        v2 = int(self.n2.text())
        v3 = v1 * v2
        self.res.setText(str(v3))

    def Divide(self):
        v1 = int(self.n1.text())
        try:
            v2 = int(self.n2.text())
            v3 = v1/v2
        except ZeroDivisionError:
            print("Denominator cannot be zero")
        self.res.setText(str(v3))

    def gotochoose1(self):
        choose1 = Choose()
        widget.addWidget(choose1)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QtWidgets.QApplication(sys.argv)    #sys.argv is a list of command line arguments
mainwindow = Choose()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(1100)
widget.show()

try:
    sys.exit(app.exec_())      #exec() call starts the event-loop and will block until the application quits
except:
    print("Exiting")




    
    
