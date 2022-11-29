from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import main
import sign_up
import bcrypt
import sys
import os
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        '''
        Cette fonction permet d'initialiser les diferents object de la classe, ainsi que de parametrer la fenetre : taille, forme, regle de clikage.
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 390, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 310, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 270, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 60, 171, 181))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("GasStation.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 270, 131, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 310, 131, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textus = QtWidgets.QLabel(self.centralwidget)
        self.textus.setGeometry(QtCore.QRect(76, 249, 221, 16))
        self.textus.setText("")
        self.textus.setObjectName("textus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        temp = []
        with open("tempus.txt", "r") as element:
            for ligne in element:
                temp.append(ligne)


    def retranslateUi(self, MainWindow):
        '''
        la fonction permet de donner une action au bouton crée, une fois le bouton crée il est possible de lui attribuer une méthode qui une
        fois clicker lance  une fonction qu'on crée tout commme la fonction setupUI dans la classe UI_MainWindow
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Stationus-login", "Stationus-login"))
        MainWindow.setFixedSize(375,535)
        MainWindow.setWindowIcon(QtGui.QIcon("GasStation.png"))
        '''MainWindow.setStyleSheet("background-color: #b5db9d;")'''
        '''MainWindow.setWindowFlag(Qt.FramelessWindowHint)'''
        self.pushButton.setText(_translate("MainWindow", "Connexion"))
        self.pushButton_2.setText(_translate("MainWindow", "Créer un compte"))
        self.label.setText(_translate("MainWindow", "Mot de passe"))
        self.label_2.setText(_translate("MainWindow", "Pseudo"))
        self.label_3.setText(_translate("MainWindow", "Stationus"))
        self.pushButton.clicked.connect(self.connexion)
        self.pushButton_2.clicked.connect(self.inscription)

    def inscription(self):
        '''
        fonction qui permet de lancer la fenetre de création de compte avec la lib OS
        '''
        os.system("python sign_up.py")

    def connexion(self):
        '''
        fonction permetant de valider une connexion ou non.
        Deux input défini si remplie alors verif la taille et la validité des str contenu dedans
        puis si bon l'ajoute dans une fichier texte avec du sel et un hashage avec la lib Bcrypt
        '''
        text_pseudo = self.lineEdit.text()
        text_mot_de_passe = self.lineEdit_2.text()
        
        if not len(text_pseudo or text_mot_de_passe) < 1:
            
            bdd = open("bdd.txt", "r")
            d = []
            f = []
            for i in bdd:
                a, b = i.split(",")
                b = b.strip()
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
                
            if text_pseudo in data:
                hashh = data[text_pseudo].strip('b')
                hashh = hashh.replace("'", "")
                hashh = hashh.encode('utf-8')
                        
                if bcrypt.checkpw(text_mot_de_passe.encode(), hashh):
                    self.textus.setText("Connexion réussite!")
                    with open("tempus.txt", "w") as f:
                        f.write(text_pseudo+"\n"+text_mot_de_passe)
                    os.system("python main.py")
                                
                else:
                    self.textus.setText("Mot de passe incorrect")
            else:
                self.textus.setText("Pseudo non existant")
        else:
            self.textus.setText("Veuillez réessayer de vous connecter")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())