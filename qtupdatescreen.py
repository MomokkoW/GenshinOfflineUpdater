# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatescreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1225, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1225, 700))
        Form.setMaximumSize(QtCore.QSize(1225, 700))
        font = QtGui.QFont()
        font.setFamily("SDK_SC_Web")
        Form.setFont(font)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1225, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("border-image: url(:/background/image2.png);")
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.logview = QtWidgets.QLabel(Form)
        self.logview.setGeometry(QtCore.QRect(20, 665, 1191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logview.setFont(font)
        self.logview.setStyleSheet("color: rgb(255, 255, 255);")
        self.logview.setObjectName("logview")
        self.progress = QtWidgets.QGraphicsView(Form)
        self.progress.setGeometry(QtCore.QRect(20, 590, 425, 52))
        self.progress.setStyleSheet("border-image: url(:/progress/element1.png);")
        self.progress.setObjectName("progress")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Updating... - GenshinOfflineUpdater"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Updating...</span></p><p><span style=\" font-size:14pt; color:#ffffff;\">Please sit back and relax.</span></p></body></html>"))
        self.logview.setText(_translate("Form", "Content"))
import mhygsuibase_rc
