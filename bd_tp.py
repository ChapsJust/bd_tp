# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bd_tp.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 632)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 160, 157))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.btn_creation_utilisateur = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_creation_utilisateur.setFont(font)
        self.btn_creation_utilisateur.setObjectName("btn_creation_utilisateur")
        self.verticalLayout.addWidget(self.btn_creation_utilisateur)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 251, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 60, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(260, 480, 201, 79))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(700, 380, 160, 123))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.comboBox_5 = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout_5.addWidget(self.comboBox_5)
        self.comboBox_10 = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.comboBox_10.setObjectName("comboBox_10")
        self.verticalLayout_5.addWidget(self.comboBox_10)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(490, 60, 229, 193))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_6.addWidget(self.lineEdit_2)
        self.comboBox_11 = QtWidgets.QComboBox(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_11.setFont(font)
        self.comboBox_11.setObjectName("comboBox_11")
        self.verticalLayout_6.addWidget(self.comboBox_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.creersauvgarde = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.creersauvgarde.setFont(font)
        self.creersauvgarde.setObjectName("creersauvgarde")
        self.horizontalLayout_2.addWidget(self.creersauvgarde)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(250, 150, 211, 321))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(520, 410, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(520, 250, 160, 108))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.repas = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.repas.setObjectName("repas")
        self.horizontalLayout.addWidget(self.repas)
        self.repas_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.repas_2.setObjectName("repas_2")
        self.horizontalLayout.addWidget(self.repas_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 250, 171, 242))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        self.comboBox_4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_8.addWidget(self.comboBox_4)
        self.comboBox_6 = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.verticalLayout_8.addWidget(self.comboBox_6)
        self.comboBox_7 = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.verticalLayout_8.addWidget(self.comboBox_7)
        self.comboBox_8 = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setObjectName("comboBox_8")
        self.verticalLayout_8.addWidget(self.comboBox_8)
        self.comboBox_9 = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setObjectName("comboBox_9")
        self.verticalLayout_8.addWidget(self.comboBox_9)
        self.bouton_aller = QtWidgets.QPushButton(self.centralwidget)
        self.bouton_aller.setGeometry(QtCore.QRect(470, 510, 75, 31))
        self.bouton_aller.setObjectName("bouton_aller")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Utilisateur"))
        self.btn_creation_utilisateur.setText(_translate("MainWindow", "Créer"))
        self.label_2.setText(_translate("MainWindow", "Livre de mon Héros"))
        self.label_3.setText(_translate("MainWindow", "Livre"))
        self.label_4.setText(_translate("MainWindow", "Chapitre"))
        self.label_5.setText(_translate("MainWindow", "Arme"))
        self.label_6.setText(_translate("MainWindow", "Sauvegarde"))
        self.creersauvgarde.setText(_translate("MainWindow", "Créer"))
        self.pushButton_2.setText(_translate("MainWindow", "Effacer"))
        self.pushButton_3.setText(_translate("MainWindow", "Choisir"))
        self.label_7.setText(_translate("MainWindow", "Bourse"))
        self.label_8.setText(_translate("MainWindow", "Sac "))
        self.label_9.setText(_translate("MainWindow", "Disiplines"))
        self.bouton_aller.setText(_translate("MainWindow", "Aller"))
