# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automouse.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 253)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("amak.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setMidLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_10.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_10.addWidget(self.label_21)
        self.gridLayout.addLayout(self.verticalLayout_10, 4, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout_8, 4, 1, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.gridLayout.addLayout(self.verticalLayout_9, 4, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_22)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton_2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_9)
        self.horizontalLayout.addLayout(self.formLayout)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMAK"))
        self.label_20.setText(_translate("MainWindow", "X"))
        self.label_21.setText(_translate("MainWindow", "Y"))
        self.label_4.setText(_translate("MainWindow", "D"))
        self.label_7.setText(_translate("MainWindow", "(Right)"))
        self.label.setText(_translate("MainWindow", "W"))
        self.label_8.setText(_translate("MainWindow", "(Run)"))
        self.label_3.setText(_translate("MainWindow", "S"))
        self.label_6.setText(_translate("MainWindow", "(Stop)"))
        self.label_2.setText(_translate("MainWindow", "A"))
        self.label_5.setText(_translate("MainWindow", "(Left)"))
        self.label_11.setText(_translate("MainWindow", "<-- X -->"))
        self.label_12.setText(_translate("MainWindow", "<-- Y -->"))
        self.label_13.setText(_translate("MainWindow", "X"))
        self.label_14.setText(_translate("MainWindow", "Y"))
        self.label_15.setText(_translate("MainWindow", "Time Interval(s): "))
        self.label_22.setText(_translate("MainWindow", "____________________________________________"))
        self.label_16.setText(_translate("MainWindow", "Current X: "))
        self.label_18.setText(_translate("MainWindow", "Current Y: "))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.label_9.setText(_translate("MainWindow", "(Press STOP button to reset time interval.)"))
