# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogueWindow(object):
    def setupUi(self, dialogueWindow):
        dialogueWindow.setObjectName("dialogueWindow")
        dialogueWindow.resize(626, 478)
        self.centralwidget = QtWidgets.QWidget(dialogueWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.dialogueName = QtWidgets.QLineEdit(self.groupBox_3)
        self.dialogueName.setObjectName("dialogueName")
        self.horizontalLayout_3.addWidget(self.dialogueName)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.dialogueDText = QtWidgets.QLineEdit(self.groupBox_3)
        self.dialogueDText.setObjectName("dialogueDText")
        self.horizontalLayout_4.addWidget(self.dialogueDText)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.dialogueChance = QtWidgets.QSpinBox(self.groupBox_2)
        self.dialogueChance.setEnabled(True)
        self.dialogueChance.setMaximum(100)
        self.dialogueChance.setProperty("value", 100)
        self.dialogueChance.setObjectName("dialogueChance")
        self.horizontalLayout_5.addWidget(self.dialogueChance)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setEnabled(True)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.dialogueFail = QtWidgets.QLineEdit(self.groupBox_2)
        self.dialogueFail.setEnabled(True)
        self.dialogueFail.setObjectName("dialogueFail")
        self.horizontalLayout_6.addWidget(self.dialogueFail)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dialogueBody = QtWidgets.QTextEdit(self.groupBox)
        self.dialogueBody.setObjectName("dialogueBody")
        self.horizontalLayout.addWidget(self.dialogueBody)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.actionList = QtWidgets.QListWidget(self.centralwidget)
        self.actionList.setObjectName("actionList")
        self.verticalLayout.addWidget(self.actionList)
        self.newAction = QtWidgets.QPushButton(self.centralwidget)
        self.newAction.setObjectName("newAction")
        self.verticalLayout.addWidget(self.newAction)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.conditionList = QtWidgets.QListWidget(self.centralwidget)
        self.conditionList.setObjectName("conditionList")
        self.verticalLayout_2.addWidget(self.conditionList)
        self.newCondition = QtWidgets.QPushButton(self.centralwidget)
        self.newCondition.setObjectName("newCondition")
        self.verticalLayout_2.addWidget(self.newCondition)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.choiceList = QtWidgets.QListWidget(self.centralwidget)
        self.choiceList.setObjectName("choiceList")
        self.verticalLayout_6.addWidget(self.choiceList)
        self.newChoice = QtWidgets.QPushButton(self.centralwidget)
        self.newChoice.setObjectName("newChoice")
        self.verticalLayout_6.addWidget(self.newChoice)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout_8.addWidget(self.createButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_8.addWidget(self.cancelButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        dialogueWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(dialogueWindow)
        QtCore.QMetaObject.connectSlotsByName(dialogueWindow)
        dialogueWindow.setTabOrder(self.dialogueName, self.dialogueDText)
        dialogueWindow.setTabOrder(self.dialogueDText, self.dialogueBody)
        dialogueWindow.setTabOrder(self.dialogueBody, self.dialogueChance)
        dialogueWindow.setTabOrder(self.dialogueChance, self.dialogueFail)
        dialogueWindow.setTabOrder(self.dialogueFail, self.actionList)
        dialogueWindow.setTabOrder(self.actionList, self.newAction)
        dialogueWindow.setTabOrder(self.newAction, self.conditionList)
        dialogueWindow.setTabOrder(self.conditionList, self.newCondition)
        dialogueWindow.setTabOrder(self.newCondition, self.choiceList)
        dialogueWindow.setTabOrder(self.choiceList, self.newChoice)
        dialogueWindow.setTabOrder(self.newChoice, self.createButton)
        dialogueWindow.setTabOrder(self.createButton, self.cancelButton)

    def retranslateUi(self, dialogueWindow):
        _translate = QtCore.QCoreApplication.translate
        dialogueWindow.setWindowTitle(_translate("dialogueWindow", "Add New Dialogue..."))
        self.groupBox_3.setTitle(_translate("dialogueWindow", "Dialogue"))
        self.label.setText(_translate("dialogueWindow", "Name"))
        self.label_2.setText(_translate("dialogueWindow", "Choice Text"))
        self.groupBox_2.setTitle(_translate("dialogueWindow", "Failure"))
        self.label_3.setText(_translate("dialogueWindow", "Chance"))
        self.label_4.setToolTip(_translate("dialogueWindow", "<html><head/><body><p>Name of the dialogue if this dialogue fails</p></body></html>"))
        self.label_4.setText(_translate("dialogueWindow", "Dialogue"))
        self.groupBox.setTitle(_translate("dialogueWindow", "Body"))
        self.newAction.setText(_translate("dialogueWindow", "Add New Action..."))
        self.newCondition.setText(_translate("dialogueWindow", "Add New Condition..."))
        self.newChoice.setText(_translate("dialogueWindow", "Add New Choice..."))
        self.createButton.setText(_translate("dialogueWindow", "OK"))
        self.cancelButton.setText(_translate("dialogueWindow", "Cancel"))
