import bcrypt
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Stationus-sign_up")
        Form.resize(389, 320)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 230, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 80, 161, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 150, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 190, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 110, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(106, 110, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Stationus-sign_up", "Stationus-sign_up"))
        Form.setFixedSize(389, 320)
        Form.setWindowIcon(QtGui.QIcon("GasStation.png"))
        self.pushButton.setText(_translate("Form", "Crée"))
        self.pushButton_2.setText(_translate("Form", "Connexion"))
        self.label_2.setText(_translate("Form", "Pseudo"))
        self.label_3.setText(_translate("Form", "Mot de passe"))
        self.label_4.setText(_translate("Form", "Confirmation  mot de passe"))
        self.label_5.setText(_translate("Form", "Création de comptus"))
        self.pushButton.clicked.connect(self.inscription)
        self.pushButton_2.clicked.connect(self.connexion)
    
    def connexion(self):
        os.system("python login.py")

    def inscription(self):
        pseudo = self.lineEdit_3.text()
        mdp1 = self.lineEdit.text()
        mdp2 = self.lineEdit_2.text()
        bdd = open("bdd.txt", "r")
        d = []

        for i in bdd:
            a,b = i.split(",")
            b = b.strip()
            d.append(a)

        if not len(mdp1)<=8:
            bdd = open("bdd.txt", "r")
            if len(pseudo) <1:
                self.label.setText("Veulliez entrer un pseudo")
            elif pseudo in d:
                self.label.setText("Pseudo déja utilisé")
            else:
                if mdp1 == mdp2:
                    mdp1 = mdp1.encode('utf-8')
                    mdp1 = bcrypt.hashpw(mdp1, bcrypt.gensalt())              
                    bdd = open("bdd.txt", "a")
                    bdd.write(pseudo+", "+str(mdp1)+"\n")
                    self.label.setText("Nouvel utilisateur crée")
                    self.label.setText("Veuillez vous connecter pour continuer")
                else:
                    self.label.setText("Les mots de passe ne correspondent pas")
        else:
            self.label.setText("Mot de passe trop court minimum 8 caractères")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())