from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import os
import pandas as p
       
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.Deconnexion = QtWidgets.QPushButton(self.centralwidget)
                self.Deconnexion.setGeometry(QtCore.QRect(680, 20, 75, 23))
                self.Deconnexion.setStyleSheet("background-color: rgb(133, 199, 199);")
                self.Deconnexion.setObjectName("Deconnexion")
                self.Compte = QtWidgets.QPushButton(self.centralwidget)
                self.Compte.setGeometry(QtCore.QRect(590, 20, 75, 23))
                self.Compte.setStyleSheet("background-color: rgb(133, 199, 199);")
                self.Compte.setObjectName("Compte")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(20, 20, 531, 381))
                self.label.setText("")
                self.label.setTextFormat(QtCore.Qt.RichText)
                self.label.setPixmap(QtGui.QPixmap("carte_aude.gif"))
                self.label.setScaledContents(True)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setWordWrap(False)
                self.label.setIndent(0)
                self.label.setObjectName("label")
                self.Limoux = QtWidgets.QPushButton(self.centralwidget)
                self.Limoux.setGeometry(QtCore.QRect(190, 240, 31, 31))
                self.Limoux.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.Limoux.setAutoFillBackground(False)
                self.Limoux.setStyleSheet("background-color: rgba(0, 170, 255, 0.5);")
                self.Limoux.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("GasStation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Limoux.setIcon(icon)
                self.Limoux.setObjectName("Limoux")
                self.Narbonne = QtWidgets.QPushButton(self.centralwidget)
                self.Narbonne.setGeometry(QtCore.QRect(470, 170, 31, 31))
                self.Narbonne.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.Narbonne.setAutoFillBackground(False)
                self.Narbonne.setStyleSheet("background-color: rgba(0, 170, 255, 0.5);")
                self.Narbonne.setText("")
                self.Narbonne.setIcon(icon)
                self.Narbonne.setObjectName("Narbonne")
                self.Lezignan = QtWidgets.QPushButton(self.centralwidget)
                self.Lezignan.setGeometry(QtCore.QRect(360, 150, 31, 31))
                self.Lezignan.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.Lezignan.setAutoFillBackground(False)
                self.Lezignan.setStyleSheet("background-color: rgba(0, 170, 255, 0.5);")
                self.Lezignan.setText("")
                self.Lezignan.setIcon(icon)
                self.Lezignan.setObjectName("Lezignan")
                self.Carcassonne = QtWidgets.QPushButton(self.centralwidget)
                self.Carcassonne.setGeometry(QtCore.QRect(230, 110, 31, 31))
                self.Carcassonne.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.Carcassonne.setAutoFillBackground(False)
                self.Carcassonne.setStyleSheet("background-color: rgba(0, 170, 255, 0.5);")
                self.Carcassonne.setText("")
                self.Carcassonne.setIcon(icon)
                self.Carcassonne.setObjectName("Carcassonne")
                self.Castelnaudary = QtWidgets.QPushButton(self.centralwidget)
                self.Castelnaudary.setGeometry(QtCore.QRect(100, 90, 31, 31))
                self.Castelnaudary.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.Castelnaudary.setAutoFillBackground(False)
                self.Castelnaudary.setStyleSheet("background-color: rgba(0, 170, 255, 0.5);")
                self.Castelnaudary.setText("")
                self.Castelnaudary.setIcon(icon)
                self.Castelnaudary.setObjectName("Castelnaudary")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(720, 60, 61, 31))
                self.pushButton.setStyleSheet("background-color: rgb(133, 199, 199);\n"
        "\n"
        "")
                self.pushButton.setObjectName("pushButton")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(572, 59, 141, 31))
                self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit.setObjectName("lineEdit")
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(569, 99, 221, 451))
                self.widget.setObjectName("widget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.scrollArea = QtWidgets.QScrollArea(self.widget)
                self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 184, 1551))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_2.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_2.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_2.setIcon(icon)
                self.pushButton_2.setObjectName("pushButton_2")
                self.verticalLayout_2.addWidget(self.pushButton_2)
                self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_3.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_3.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_3.setIcon(icon)
                self.pushButton_3.setObjectName("pushButton_3")
                self.verticalLayout_2.addWidget(self.pushButton_3)
                self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_4.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_4.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_4.setIcon(icon)
                self.pushButton_4.setObjectName("pushButton_4")
                self.verticalLayout_2.addWidget(self.pushButton_4)
                self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_5.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_5.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_5.setIcon(icon)
                self.pushButton_5.setObjectName("pushButton_5")
                self.verticalLayout_2.addWidget(self.pushButton_5)
                self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_6.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_6.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_6.setIcon(icon)
                self.pushButton_6.setObjectName("pushButton_6")
                self.verticalLayout_2.addWidget(self.pushButton_6)
                self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_8.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_8.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_8.setIcon(icon)
                self.pushButton_8.setObjectName("pushButton_8")
                self.verticalLayout_2.addWidget(self.pushButton_8)
                self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_7.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_7.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_7.setIcon(icon)
                self.pushButton_7.setObjectName("pushButton_7")
                self.verticalLayout_2.addWidget(self.pushButton_7)
                self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_9.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_9.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_9.setIcon(icon)
                self.pushButton_9.setObjectName("pushButton_9")
                self.verticalLayout_2.addWidget(self.pushButton_9)
                self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_11.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_11.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_11.setIcon(icon)
                self.pushButton_11.setObjectName("pushButton_11")
                self.verticalLayout_2.addWidget(self.pushButton_11)
                self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_10.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_10.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_10.setIcon(icon)
                self.pushButton_10.setObjectName("pushButton_10")
                self.verticalLayout_2.addWidget(self.pushButton_10)
                self.pushButton_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_20.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_20.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_20.setIcon(icon)
                self.pushButton_20.setObjectName("pushButton_20")
                self.verticalLayout_2.addWidget(self.pushButton_20)
                self.pushButton_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_19.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_19.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_19.setIcon(icon)
                self.pushButton_19.setObjectName("pushButton_19")
                self.verticalLayout_2.addWidget(self.pushButton_19)
                self.pushButton_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_18.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_18.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_18.setIcon(icon)
                self.pushButton_18.setObjectName("pushButton_18")
                self.verticalLayout_2.addWidget(self.pushButton_18)
                self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_17.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_17.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_17.setIcon(icon)
                self.pushButton_17.setObjectName("pushButton_17")
                self.verticalLayout_2.addWidget(self.pushButton_17)
                self.pushButton_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_16.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_16.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_16.setIcon(icon)
                self.pushButton_16.setObjectName("pushButton_16")
                self.verticalLayout_2.addWidget(self.pushButton_16)
                self.pushButton_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_15.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_15.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_15.setIcon(icon)
                self.pushButton_15.setObjectName("pushButton_15")
                self.verticalLayout_2.addWidget(self.pushButton_15)
                self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_14.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_14.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_14.setIcon(icon)
                self.pushButton_14.setObjectName("pushButton_14")
                self.verticalLayout_2.addWidget(self.pushButton_14)
                self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_13.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_13.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_13.setIcon(icon)
                self.pushButton_13.setObjectName("pushButton_13")
                self.verticalLayout_2.addWidget(self.pushButton_13)
                self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.pushButton_12.setMinimumSize(QtCore.QSize(0, 75))
                self.pushButton_12.setStyleSheet("background-color: rgb(231, 231, 231);")
                self.pushButton_12.setIcon(icon)
                self.pushButton_12.setObjectName("pushButton_12")
                self.verticalLayout_2.addWidget(self.pushButton_12)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.verticalLayout.addWidget(self.scrollArea)
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(26, 420, 121, 111))
                self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(160, 420, 121, 31))
                self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_3.setText("")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(290, 420, 121, 31))
                self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_4.setText("")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(420, 420, 121, 31))
                self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_5.setText("")
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(160, 460, 121, 71))
                self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_6.setText("")
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(290, 460, 121, 71))
                self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_7.setText("")
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(420, 460, 121, 71))
                self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_8.setText("")
                self.label_8.setObjectName("label_8")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("Stationus", "Stationus"))
                MainWindow.setObjectName("Stationus")
                MainWindow.setWindowIcon(QtGui.QIcon("GasStation.png"))
                MainWindow.resize(800, 600)
                MainWindow.setFixedSize(800,600)
                '''MainWindow.setStyleSheet("background-color: #b5db9d;")'''
                self.Deconnexion.setText(_translate("MainWindow", "Déconnexion"))
                self.Compte.setText(_translate("MainWindow", "Compte"))
                self.pushButton.setText(_translate("MainWindow", "Recherche"))
                self.pushButton_2.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_3.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_4.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_5.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_6.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_8.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_7.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_9.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_11.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_10.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_20.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_19.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_18.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_17.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_16.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_15.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_14.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_13.setText(_translate("MainWindow", "Nom des stations"))
                self.pushButton_12.setText(_translate("MainWindow", "Nom des stations"))
                self.label_3.setText(_translate("MainWindow", "Prix essence"))
                self.label_4.setText(_translate("MainWindow", ""))
                self.label_5.setText(_translate("MainWindow", ""))
                self.Deconnexion.clicked.connect(self.deconnexion)
                self.Compte.clicked.connect(self.compte)
                self.pushButton.clicked.connect(self.rechercher)
                self.Castelnaudary.clicked.connect(self.Castel)
                self.Lezignan.clicked.connect(self.Lezigan_)
                self.Limoux.clicked.connect(self.Limoux_)
                self.Narbonne.clicked.connect(self.Narbonne_)
                self.Carcassonne.clicked.connect(self.Carcassonne_)
                self.pushButton_2.clicked.connect(self.afficher_info)
                self.pushButton_3.clicked.connect(self.afficher_info)
                self.pushButton_4.clicked.connect(self.afficher_info)
                self.pushButton_5.clicked.connect(self.afficher_info)
                self.pushButton_6.clicked.connect(self.afficher_info)
                self.pushButton_7.clicked.connect(self.afficher_info)
                self.pushButton_8.clicked.connect(self.afficher_info)
                self.pushButton_9.clicked.connect(self.afficher_info)
                self.pushButton_10.clicked.connect(self.afficher_info)
                self.pushButton_11.clicked.connect(self.afficher_info)
                self.pushButton_12.clicked.connect(self.afficher_info)
                self.pushButton_13.clicked.connect(self.afficher_info)
                self.pushButton_14.clicked.connect(self.afficher_info)
                self.pushButton_15.clicked.connect(self.afficher_info)
                self.pushButton_16.clicked.connect(self.afficher_info)
                self.pushButton_17.clicked.connect(self.afficher_info)
                self.pushButton_18.clicked.connect(self.afficher_info)
                self.pushButton_19.clicked.connect(self.afficher_info)
                self.pushButton_20.clicked.connect(self.afficher_info)
                
                prix_valeur = []
                with open("prix_valeur.txt", "r") as element:
                        for ligne in element:
                                prix_valeur.append(ligne)

                adresse = []
                with open("adresse.txt", "r") as element:
                        for ligne in element:
                                adresse.append(ligne)
                print(len(adresse), len(prix_valeur))


                if self.pushButton_2.clicked:
                        self.label_2.setText(adresse[1])
                        self.label_6.setText(prix_valeur[2])

                if self.pushButton_3.clicked:
                        self.label_2.setText(adresse[2])
                        self.label_6.setText(prix_valeur[3])

                if self.pushButton_4.clicked:
                        self.label_2.setText(adresse[3])
                        self.label_6.setText(prix_valeur[4])

                if self.pushButton_5.clicked:
                        self.label_2.setText(adresse[4])
                        self.label_6.setText(prix_valeur[5])

                if self.pushButton_6.clicked:
                        self.label_2.setText(adresse[5])
                        self.label_6.setText(prix_valeur[6])

                if self.pushButton_7.clicked:
                        self.label_2.setText(adresse[6])
                        self.label_6.setText(prix_valeur[7])

                if self.pushButton_8.clicked:
                        self.label_2.setText(adresse[7])
                        self.label_6.setText(prix_valeur[8])

                if self.pushButton_9.clicked:
                        self.label_2.setText(adresse[8])
                        self.label_6.setText(prix_valeur[9])

                if self.pushButton_10.clicked:
                        self.label_2.setText(adresse[9])
                        self.label_6.setText(prix_valeur[10])

                if self.pushButton_11.clicked:
                        self.label_2.setText(adresse[10])
                        self.label_6.setText(prix_valeur[11])

                if self.pushButton_12.clicked:
                        self.label_2.setText(adresse[11])
                        self.label_6.setText(prix_valeur[12])

                if self.pushButton_13.clicked:
                        self.label_2.setText(adresse[12])
                        self.label_6.setText(prix_valeur[13])

                if self.pushButton_14.clicked:
                        self.label_2.setText(adresse[13])
                        self.label_6.setText(prix_valeur[14])

                if self.pushButton_15.clicked:
                        self.label_2.setText(adresse[14])
                        self.label_6.setText(prix_valeur[15])

                if self.Castelnaudary.clicked:
                        self.search("11400")

        def afficher_info(self):
                rechercher = self.lineEdit.text()
                prix_valeur = []
                with open("prix_valeur.txt", "r") as element:
                        for ligne in element:
                                prix_valeur.append(ligne)

                adresse = []
                with open("adresse.txt", "r") as element:
                        for ligne in element:
                                adresse.append(ligne)
                print(len(adresse), len(prix_valeur))

                if rechercher == "" :
                        self.label_2.setText("")
                        self.label_6.setText("")
                        self.label_7.setText("")
                        self.label_8.setText("")


                if self.Lezignan.clicked:
                        self.search("11200")
                        prix_valeur = []
                        with open("prix_valeur.txt", "r") as element:
                                for ligne in element:
                                        prix_valeur.append(ligne)

                        adresse = []
                        with open("adresse.txt", "r") as element:
                                for ligne in element:
                                        adresse.append(ligne)
                        
                        if self.pushButton_2.clicked:
                                self.label_2.setText(adresse[1])
                                self.label_6.setText(prix_valeur[2])

                        if self.pushButton_3.clicked:
                                self.label_2.setText(adresse[2])
                                self.label_6.setText(prix_valeur[3])

                        if self.pushButton_4.clicked:
                                self.label_2.setText(adresse[3])
                                self.label_6.setText(prix_valeur[4])

                        if self.pushButton_5.clicked:
                                self.label_2.setText(adresse[4])
                                self.label_6.setText(prix_valeur[5])

                        if self.pushButton_6.clicked:
                                self.label_2.setText(adresse[5])
                                self.label_6.setText(prix_valeur[6])

                        if self.pushButton_7.clicked:
                                self.label_2.setText(adresse[6])
                                self.label_6.setText(prix_valeur[7])

                        if self.pushButton_8.clicked:
                                self.label_2.setText(adresse[7])
                                self.label_6.setText(prix_valeur[8])

                        if self.pushButton_9.clicked:
                                self.label_2.setText(adresse[8])
                                self.label_6.setText(prix_valeur[9])

                        if self.pushButton_10.clicked:
                                self.label_2.setText(adresse[9])
                                self.label_6.setText(prix_valeur[10])

                        if self.pushButton_11.clicked:
                                self.label_2.setText(adresse[10])
                                self.label_6.setText(prix_valeur[11])

                        if self.pushButton_12.clicked:
                                self.label_2.setText(adresse[11])
                                self.label_6.setText(prix_valeur[12])

                        if self.pushButton_13.clicked:
                                self.label_2.setText(adresse[12])
                                self.label_6.setText(prix_valeur[13])

                        if self.pushButton_14.clicked:
                                self.label_2.setText(adresse[13])
                                self.label_6.setText(prix_valeur[14])

                        if self.pushButton_15.clicked:
                                self.label_2.setText(adresse[14])
                                self.label_6.setText(prix_valeur[15])

                        if self.pushButton_16.clicked:
                                self.label_2.setText(adresse[15])
                                self.label_6.setText(prix_valeur[16])
                        
                        if self.pushButton_17.clicked:
                                self.label_2.setText(adresse[16])
                                self.label_6.setText(prix_valeur[17])

                        if self.pushButton_18.clicked:
                                self.label_2.setText(adresse[17])
                                self.label_6.setText(prix_valeur[18])

                if self.Limoux.clicked:
                        prix_valeur = []
                        with open("prix_valeur.txt", "r") as element:
                                for ligne in element:
                                        prix_valeur.append(ligne)

                        adresse = []
                        with open("adresse.txt", "r") as element:
                                for ligne in element:
                                        adresse.append(ligne)

                        if self.pushButton_2.clicked:
                                self.label_2.setText(adresse[1])
                                self.label_6.setText(prix_valeur[2])

                        if self.pushButton_3.clicked:
                                self.label_2.setText(adresse[2])
                                self.label_6.setText(prix_valeur[3])

                        if self.pushButton_4.clicked:
                                self.label_2.setText(adresse[3])
                                self.label_6.setText(prix_valeur[4])

                        if self.pushButton_5.clicked:
                                self.label_2.setText(adresse[4])
                                self.label_6.setText(prix_valeur[5])

                        if self.pushButton_6.clicked:
                                self.label_2.setText(adresse[5])
                                self.label_6.setText(prix_valeur[6])

                        if self.pushButton_7.clicked:
                                self.label_2.setText(adresse[6])
                                self.label_6.setText(prix_valeur[7])

                        if self.pushButton_8.clicked:
                                self.label_2.setText(adresse[7])
                                self.label_6.setText(prix_valeur[8])

                        if self.pushButton_9.clicked:
                                self.label_2.setText(adresse[8])
                                self.label_6.setText(prix_valeur[9])

                        if self.pushButton_10.clicked:
                                self.label_2.setText(adresse[9])
                                self.label_6.setText(prix_valeur[10])

                        if self.pushButton_11.clicked:
                                self.label_2.setText(adresse[10])
                                self.label_6.setText(prix_valeur[11])

                        if self.pushButton_12.clicked:
                                self.label_2.setText(adresse[11])
                                self.label_6.setText(prix_valeur[12])

                        if self.pushButton_13.clicked:
                                self.label_2.setText(adresse[12])
                                self.label_6.setText(prix_valeur[13])

                        if self.pushButton_14.clicked:
                                self.label_2.setText(adresse[13])
                                self.label_6.setText(prix_valeur[14])

                        if self.pushButton_15.clicked:
                                self.label_2.setText(adresse[14])
                                self.label_6.setText(prix_valeur[15])

                        if self.pushButton_16.clicked:
                                self.label_2.setText(adresse[15])
                                self.label_6.setText(prix_valeur[16])
                        
                        if self.pushButton_17.clicked:
                                self.label_2.setText(adresse[16])
                                self.label_6.setText(prix_valeur[17])

                        if self.pushButton_18.clicked:
                                self.label_2.setText(adresse[17])
                                self.label_6.setText(prix_valeur[18])

                if self.Narbonne.clicked:
                        prix_valeur = []
                        with open("prix_valeur.txt", "r") as element:
                                for ligne in element:
                                        prix_valeur.append(ligne)

                        adresse = []
                        with open("adresse.txt", "r") as element:
                                for ligne in element:
                                        adresse.append(ligne)
                
                        if self.pushButton_2.clicked:
                                self.label_2.setText(adresse[1])
                                self.label_6.setText(prix_valeur[2])

                        if self.pushButton_3.clicked:
                                self.label_2.setText(adresse[2])
                                self.label_6.setText(prix_valeur[3])

                        if self.pushButton_4.clicked:
                                self.label_2.setText(adresse[3])
                                self.label_6.setText(prix_valeur[4])

                        if self.pushButton_5.clicked:
                                self.label_2.setText(adresse[4])
                                self.label_6.setText(prix_valeur[5])

                        if self.pushButton_6.clicked:
                                self.label_2.setText(adresse[5])
                                self.label_6.setText(prix_valeur[6])

                        if self.pushButton_7.clicked:
                                self.label_2.setText(adresse[6])
                                self.label_6.setText(prix_valeur[7])

                        if self.pushButton_8.clicked:
                                self.label_2.setText(adresse[7])
                                self.label_6.setText(prix_valeur[8])

                        if self.pushButton_9.clicked:
                                self.label_2.setText(adresse[8])
                                self.label_6.setText(prix_valeur[9])

                        if self.pushButton_10.clicked:
                                self.label_2.setText(adresse[9])
                                self.label_6.setText(prix_valeur[10])

                        if self.pushButton_11.clicked:
                                self.label_2.setText(adresse[10])
                                self.label_6.setText(prix_valeur[11])

                        if self.pushButton_12.clicked:
                                self.label_2.setText(adresse[11])
                                self.label_6.setText(prix_valeur[12])

                        if self.pushButton_13.clicked:
                                self.label_2.setText(adresse[12])
                                self.label_6.setText(prix_valeur[13])

                        if self.pushButton_14.clicked:
                                self.label_2.setText(adresse[13])
                                self.label_6.setText(prix_valeur[14])

                        if self.pushButton_15.clicked:
                                self.label_2.setText(adresse[14])
                                self.label_6.setText(prix_valeur[15])

                        if self.pushButton_16.clicked:
                                self.label_2.setText(adresse[15])
                                self.label_6.setText(prix_valeur[16])
                        
                        if self.pushButton_17.clicked:
                                self.label_2.setText(adresse[16])
                                self.label_6.setText(prix_valeur[17])

                        if self.pushButton_18.clicked:
                                self.label_2.setText(adresse[17])
                                self.label_6.setText(prix_valeur[18])

                if self.Carcassonne.clicked:
                        self.rechercher("amknreejlmar")
                        prix_valeur = []
                        with open("prix_valeur.txt", "r") as element:
                                for ligne in element:
                                        prix_valeur.append(ligne)

                        adresse = []
                        with open("adresse.txt", "r") as element:
                                for ligne in element:
                                        adresse.append(ligne)
                        if self.pushButton_2.clicked:
                                self.label_2.setText(adresse[1])
                                self.label_6.setText(prix_valeur[2])

                        if self.pushButton_3.clicked:
                                self.label_2.setText(adresse[2])
                                self.label_6.setText(prix_valeur[3])

                        if self.pushButton_4.clicked:
                                self.label_2.setText(adresse[3])
                                self.label_6.setText(prix_valeur[4])

                        if self.pushButton_5.clicked:
                                self.label_2.setText(adresse[4])
                                self.label_6.setText(prix_valeur[5])

                        if self.pushButton_6.clicked:
                                self.label_2.setText(adresse[5])
                                self.label_6.setText(prix_valeur[6])

                        if self.pushButton_7.clicked:
                                self.label_2.setText(adresse[6])
                                self.label_6.setText(prix_valeur[7])

                        if self.pushButton_8.clicked:
                                self.label_2.setText(adresse[7])
                                self.label_6.setText(prix_valeur[8])

                        if self.pushButton_9.clicked:
                                self.label_2.setText(adresse[8])
                                self.label_6.setText(prix_valeur[9])

                        if self.pushButton_10.clicked:
                                self.label_2.setText(adresse[9])
                                self.label_6.setText(prix_valeur[10])

                        if self.pushButton_11.clicked:
                                self.label_2.setText(adresse[10])
                                self.label_6.setText(prix_valeur[11])

                        if self.pushButton_12.clicked:
                                self.label_2.setText(adresse[11])
                                self.label_6.setText(prix_valeur[12])

                        if self.pushButton_13.clicked:
                                self.label_2.setText(adresse[12])
                                self.label_6.setText(prix_valeur[13])

                        if self.pushButton_14.clicked:
                                self.label_2.setText(adresse[13])
                                self.label_6.setText(prix_valeur[14])

                        if self.pushButton_15.clicked:
                                self.label_2.setText(adresse[14])
                                self.label_6.setText(prix_valeur[15])

                        if self.pushButton_16.clicked:
                                self.label_2.setText(adresse[15])
                                self.label_6.setText(prix_valeur[16])
                        
                        if self.pushButton_17.clicked:
                                self.label_2.setText(adresse[16])
                                self.label_6.setText(prix_valeur[17])

                        if self.pushButton_18.clicked:
                                self.label_2.setText(adresse[17])
                                self.label_6.setText(prix_valeur[18])

                if self.pushButton.clicked:
                        recherche = self.lineEdit.text()
                        self.rechercher(recherche)

        def rechercher(self,recherche):
                if recherche == False:
                        self.pushButton_2.setText("None")
                        self.pushButton_3.setText("None")
                        self.pushButton_4.setText("None")
                        self.pushButton_5.setText("None")
                        self.pushButton_6.setText("None")
                        self.pushButton_7.setText("None")
                        self.pushButton_8.setText("None")
                        self.pushButton_9.setText("None")
                        self.pushButton_10.setText("None")
                        self.pushButton_11.setText("None")
                        self.pushButton_12.setText("None")
                        self.pushButton_13.setText("None")
                        self.pushButton_14.setText("None")
                        self.pushButton_15.setText("None")
                        self.pushButton_16.setText("None")
                        self.pushButton_17.setText("None")
                        self.pushButton_18.setText("None")
                        self.pushButton_19.setText("None")
                        self.pushButton_20.setText("None")

                if self.Castelnaudary.clicked:
                        f = p.read_csv("sus.csv", delimiter=";", keep_default_na=False)
                        tri = f.sort_values(by=["cp"])
                        aude = tri[(tri["cp"] >= 11000) & (tri["cp"] < 12000)]
                        v_recherche = str(11400)
                        if len(v_recherche) > 0:
                                cp_int = int(v_recherche)
                                df = aude[aude["cp"].isin([cp_int])]
                
                                if df.size != 0:
                                        df["prix_valeur"].to_csv('prix_valeur.txt', sep=' ', index=False)
                if self.Lezignan.clicked:
                        f = p.read_csv("sus.csv", delimiter=";", keep_default_na=False)
                        tri = f.sort_values(by=["cp"])
                        aude = tri[(tri["cp"] >= 11000) & (tri["cp"] < 12000)]
                        v_recherche = str(11200)
                        if len(v_recherche) > 0:
                                cp_int = int(v_recherche)
                                df = aude[aude["cp"].isin([cp_int])]
                
                                if df.size != 0:
                                        df["prix_valeur"].to_csv('prix_valeur.txt', sep=' ', index=False)
                if self.Limoux.clicked:
                        f = p.read_csv("sus.csv", delimiter=";", keep_default_na=False)
                        tri = f.sort_values(by=["cp"])
                        aude = tri[(tri["cp"] >= 11000) & (tri["cp"] < 12000)]
                        v_recherche = str(11300)
                        if len(v_recherche) > 0:
                                cp_int = int(v_recherche)
                                df = aude[aude["cp"].isin([cp_int])]
                
                                if df.size != 0:
                                        df["prix_valeur"].to_csv('prix_valeur.txt', sep=' ', index=False)
                if self.Narbonne.clicked:
                        f = p.read_csv("sus.csv", delimiter=";", keep_default_na=False)
                        tri = f.sort_values(by=["cp"])
                        aude = tri[(tri["cp"] >= 11000) & (tri["cp"] < 12000)]
                        v_recherche = str(11100)
                        if len(v_recherche) > 0:
                                cp_int = int(v_recherche)
                                df = aude[aude["cp"].isin([cp_int])]
                
                                if df.size != 0:
                                        df["prix_valeur"].to_csv('prix_valeur.txt', sep=' ', index=False)
                if self.Carcassonne.clicked:
                        f = p.read_csv("sus.csv", delimiter=";", keep_default_na=False)
                        tri = f.sort_values(by=["cp"])
                        aude = tri[(tri["cp"] >= 11000) & (tri["cp"] < 12000)]
                        v_recherche = str(11000)
                        if len(v_recherche) > 0:
                                cp_int = int(v_recherche)
                                df = aude[aude["cp"].isin([cp_int])]
                
                                if df.size != 0:
                                        df["prix_valeur"].to_csv('prix_valeur.txt', sep=' ', index=False)


        def search(self,a):
                f = p.read_csv("sus.csv", delimiter=";", keep_default_na=False)
                tri = f.sort_values(by=["cp"])
                aude = tri[(tri["cp"] >= 11000) & (tri["cp"] < 12000)]
                v_recherche = str(a)
                if len(v_recherche) > 0:
                        cp_int = int(v_recherche)
                        df = aude[aude["cp"].isin([cp_int])]
        
                        if df.size != 0:
                                df["adresse"].to_csv('adresse.txt', sep=' ', index=False)
                                df["prix_nom"].to_csv('prix_nom.txt', sep=' ', index=False)

                        else:
                                print("Ce code postal n'est pas audois ou ne possède pas de station.")
    
                else:
                        print("Veuillez entrer une valeur.")
                

        def Castel(self):
                self.search("11400")
                adresse = []
                with open("adresse.txt", "r") as element:
                        for ligne in element:
                                adresse.append(ligne)

                prix_nom = []
                with open("prix_nom.txt", "r") as element:
                        for ligne in element:
                                prix_nom.append(ligne)
                
                self.pushButton_2.setText(adresse[1] + prix_nom[2])
                self.pushButton_3.setText(adresse[2]+ prix_nom[3])
                self.pushButton_4.setText(adresse[3]+ prix_nom[4])
                self.pushButton_5.setText(adresse[4]+ prix_nom[5])
                self.pushButton_6.setText(adresse[5]+ prix_nom[6])
                self.pushButton_7.setText(adresse[6]+ prix_nom[7])
                self.pushButton_8.setText(adresse[7]+ prix_nom[8])
                self.pushButton_9.setText(adresse[8]+ prix_nom[9])
                self.pushButton_10.setText(adresse[9]+ prix_nom[10])
                self.pushButton_11.setText(adresse[10]+ prix_nom[11])
                self.pushButton_12.setText(adresse[11]+ prix_nom[12])
                self.pushButton_13.setText(adresse[12]+ prix_nom[13])
                self.pushButton_14.setText(adresse[13]+ prix_nom[14])
                self.pushButton_15.setText(adresse[14]+ prix_nom[15])
                self.pushButton_16.setText(adresse[15]+ prix_nom[16])
                self.pushButton_17.setText(adresse[16]+ prix_nom[17])
        
        def Carcassonne_(self):
                self.search("11000")
                adresse = []
                with open("adresse.txt", "r") as element:
                        for ligne in element:
                                adresse.append(ligne)
                
                prix_nom = []
                with open("prix_nom.txt", "r") as element:
                        for ligne in element:
                                prix_nom.append(ligne)
                self.pushButton_2.setText(adresse[1] + prix_nom[2])
                self.pushButton_3.setText(adresse[2]+ prix_nom[3])
                self.pushButton_4.setText(adresse[3]+ prix_nom[4])
                self.pushButton_5.setText(adresse[4]+ prix_nom[5])
                self.pushButton_6.setText(adresse[5]+ prix_nom[6])
                self.pushButton_7.setText(adresse[6]+ prix_nom[7])
                self.pushButton_8.setText(adresse[7]+ prix_nom[8])
                self.pushButton_9.setText(adresse[8]+ prix_nom[9])
                self.pushButton_10.setText(adresse[9]+ prix_nom[10])
                self.pushButton_11.setText(adresse[10]+ prix_nom[11])
                self.pushButton_12.setText(adresse[11]+ prix_nom[12])
                self.pushButton_13.setText(adresse[12]+ prix_nom[13])
                self.pushButton_14.setText(adresse[13]+ prix_nom[14])
                self.pushButton_15.setText(adresse[14]+ prix_nom[15])
                self.pushButton_16.setText(adresse[15]+ prix_nom[16])
                self.pushButton_17.setText(adresse[16]+ prix_nom[17])
                self.pushButton_18.setText(adresse[17]+ prix_nom[18])

        def Lezigan_(self):
                self.search("11200")
                adresse = []
                with open("adresse.txt", "r") as element:
                        for ligne in element:
                                adresse.append(ligne)
                
                prix_nom = []
                with open("prix_nom.txt", "r") as element:
                        for ligne in element:
                                prix_nom.append(ligne)
                self.pushButton_2.setText(adresse[1] + prix_nom[2])
                self.pushButton_3.setText(adresse[2]+ prix_nom[3])
                self.pushButton_4.setText(adresse[3]+ prix_nom[4])
                self.pushButton_5.setText(adresse[4]+ prix_nom[5])
                self.pushButton_6.setText(adresse[5]+ prix_nom[6])
                self.pushButton_7.setText(adresse[6]+ prix_nom[7])
                self.pushButton_8.setText(adresse[7]+ prix_nom[8])
                self.pushButton_9.setText(adresse[8]+ prix_nom[9])
                self.pushButton_10.setText(adresse[9]+ prix_nom[10])
                self.pushButton_11.setText(adresse[10]+ prix_nom[11])
                self.pushButton_12.setText(adresse[11]+ prix_nom[12])
                self.pushButton_13.setText(adresse[12]+ prix_nom[13])
                self.pushButton_14.setText(adresse[13]+ prix_nom[14])
                self.pushButton_15.setText(adresse[14]+ prix_nom[15])
                self.pushButton_16.setText(adresse[15]+ prix_nom[16])
                self.pushButton_17.setText(adresse[16]+ prix_nom[17])
                self.pushButton_18.setText(adresse[17]+ prix_nom[18])

        def Narbonne_(self):
                self.search("11100")
                adresse = []
                with open("adresse.txt", "r") as element:
                        for ligne in element:
                                adresse.append(ligne)
                
                prix_nom = []
                with open("prix_nom.txt", "r") as element:
                        for ligne in element:
                                prix_nom.append(ligne)
                self.pushButton_2.setText(adresse[1] + prix_nom[2])
                self.pushButton_3.setText(adresse[2]+ prix_nom[3])
                self.pushButton_4.setText(adresse[3]+ prix_nom[4])
                self.pushButton_5.setText(adresse[4]+ prix_nom[5])
                self.pushButton_6.setText(adresse[5]+ prix_nom[6])
                self.pushButton_7.setText(adresse[6]+ prix_nom[7])
                self.pushButton_8.setText(adresse[7]+ prix_nom[8])
                self.pushButton_9.setText(adresse[8]+ prix_nom[9])
                self.pushButton_10.setText(adresse[9]+ prix_nom[10])
                self.pushButton_11.setText(adresse[10]+ prix_nom[11])
                self.pushButton_12.setText(adresse[11]+ prix_nom[12])
                self.pushButton_13.setText(adresse[12]+ prix_nom[13])
                self.pushButton_14.setText(adresse[13]+ prix_nom[14])
                self.pushButton_15.setText(adresse[14]+ prix_nom[15])
                self.pushButton_16.setText(adresse[15]+ prix_nom[16])
                self.pushButton_17.setText(adresse[16]+ prix_nom[17])
                self.pushButton_18.setText(adresse[17]+ prix_nom[18])

        def Limoux_(self):
                self.search("11300")
                adresse = []
                with open("adresse.txt", "r") as element:
                        for ligne in element:
                                adresse.append(ligne)
                
                prix_nom = []
                with open("prix_nom.txt", "r") as element:
                        for ligne in element:
                                prix_nom.append(ligne)
                self.pushButton_2.setText(adresse[1] + prix_nom[2])
                self.pushButton_3.setText(adresse[2]+ prix_nom[3])
                self.pushButton_4.setText(adresse[3]+ prix_nom[4])
                self.pushButton_5.setText(adresse[4]+ prix_nom[5])
                self.pushButton_6.setText(adresse[5]+ prix_nom[6])
                self.pushButton_7.setText(adresse[6]+ prix_nom[7])
                self.pushButton_8.setText(adresse[7]+ prix_nom[8])
                self.pushButton_9.setText(adresse[8]+ prix_nom[9])
                self.pushButton_10.setText(adresse[9]+ prix_nom[10])
                self.pushButton_11.setText(adresse[10]+ prix_nom[11])
                self.pushButton_12.setText(adresse[11]+ prix_nom[12])
                self.pushButton_13.setText(adresse[12]+ prix_nom[13])
                self.pushButton_14.setText(adresse[13]+ prix_nom[14])

        def compte(self):
                os.system("python compte.py")

        def deconnexion(self):
                with open("ville.txt", "w") as f:
                        f.write("")
                os.system("python login.py")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())