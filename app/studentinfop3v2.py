# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './StudentInformationP3v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_P3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 389)
        self.label_04 = QtWidgets.QLabel(Form)
        self.label_04.setGeometry(QtCore.QRect(63, 144, 26, 21))
        self.label_04.setObjectName("label_04")
        self.label_00 = QtWidgets.QLabel(Form)
        self.label_00.setGeometry(QtCore.QRect(60, 51, 29, 21))
        self.label_00.setObjectName("label_00")
        self.label_07 = QtWidgets.QLabel(Form)
        self.label_07.setGeometry(QtCore.QRect(42, 237, 47, 21))
        self.label_07.setObjectName("label_07")
        self.label_03 = QtWidgets.QLabel(Form)
        self.label_03.setGeometry(QtCore.QRect(62, 113, 27, 21))
        self.label_03.setObjectName("label_03")
        self.alert_file_exists = QtWidgets.QLabel(Form)
        self.alert_file_exists.setEnabled(True)
        self.alert_file_exists.setGeometry(QtCore.QRect(261, 317, 311, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.alert_file_exists.setFont(font)
        self.alert_file_exists.setObjectName("alert_file_exists")
        self.label_06 = QtWidgets.QLabel(Form)
        self.label_06.setGeometry(QtCore.QRect(60, 206, 47, 21))
        self.label_06.setObjectName("label_06")
        self.label_01 = QtWidgets.QLabel(Form)
        self.label_01.setGeometry(QtCore.QRect(59, 82, 30, 21))
        self.label_01.setObjectName("label_01")
        self.label_05 = QtWidgets.QLabel(Form)
        self.label_05.setGeometry(QtCore.QRect(44, 175, 45, 21))
        self.label_05.setObjectName("label_05")
        self.form_title = QtWidgets.QLabel(Form)
        self.form_title.setGeometry(QtCore.QRect(29, 20, 171, 21))
        self.form_title.setObjectName("form_title")
        self.data_browser_0 = QtWidgets.QLabel(Form)
        self.data_browser_0.setEnabled(True)
        self.data_browser_0.setGeometry(QtCore.QRect(100, 51, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_browser_0.setFont(font)
        self.data_browser_0.setObjectName("data_browser_0")
        self.data_browser_1 = QtWidgets.QLabel(Form)
        self.data_browser_1.setEnabled(True)
        self.data_browser_1.setGeometry(QtCore.QRect(100, 82, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_browser_1.setFont(font)
        self.data_browser_1.setObjectName("data_browser_1")
        self.data_browser_3 = QtWidgets.QLabel(Form)
        self.data_browser_3.setEnabled(True)
        self.data_browser_3.setGeometry(QtCore.QRect(100, 113, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_browser_3.setFont(font)
        self.data_browser_3.setObjectName("data_browser_3")
        self.data_browser_4 = QtWidgets.QLabel(Form)
        self.data_browser_4.setEnabled(True)
        self.data_browser_4.setGeometry(QtCore.QRect(100, 144, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_browser_4.setFont(font)
        self.data_browser_4.setObjectName("data_browser_4")
        self.data_browser_5 = QtWidgets.QLabel(Form)
        self.data_browser_5.setEnabled(True)
        self.data_browser_5.setGeometry(QtCore.QRect(100, 175, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_browser_5.setFont(font)
        self.data_browser_5.setObjectName("data_browser_5")
        self.data_browser_6 = QtWidgets.QLabel(Form)
        self.data_browser_6.setEnabled(True)
        self.data_browser_6.setGeometry(QtCore.QRect(100, 206, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_browser_6.setFont(font)
        self.data_browser_6.setObjectName("data_browser_6")
        self.data_browser_7 = QtWidgets.QLabel(Form)
        self.data_browser_7.setEnabled(True)
        self.data_browser_7.setGeometry(QtCore.QRect(100, 237, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_browser_7.setFont(font)
        self.data_browser_7.setObjectName("data_browser_7")
        self.listWidgetP3 = QtWidgets.QListWidget(Form)
        self.listWidgetP3.setGeometry(QtCore.QRect(241, 47, 351, 261))
        self.listWidgetP3.setObjectName("listWidgetP3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 30, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(385, 30, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(473, 30, 31, 16))
        self.label_3.setObjectName("label_3")
        self.editStudentButton = QtWidgets.QToolButton(Form)
        self.editStudentButton.setGeometry(QtCore.QRect(450, 349, 20, 21))
        self.editStudentButton.setText("")
        self.editStudentButton.setObjectName("editStudentButton")
        self.newLogButtonP3 = QtWidgets.QToolButton(Form)
        self.newLogButtonP3.setGeometry(QtCore.QRect(410, 350, 20, 20))
        self.newLogButtonP3.setText("")
        self.newLogButtonP3.setObjectName("newLogButtonP3")
        self.backButtonP3 = QtWidgets.QToolButton(Form)
        self.backButtonP3.setGeometry(QtCore.QRect(370, 350, 20, 20))
        self.backButtonP3.setText("")
        self.backButtonP3.setObjectName("backButtonP3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cougar-Log"))
        self.label_04.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Last:</span></p></body></html>"))
        self.label_00.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Date:</span></p></body></html>"))
        self.label_07.setText(_translate("Form", "Subject:"))
        self.label_03.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">First:</span></p></body></html>"))
        self.alert_file_exists.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_06.setText(_translate("Form", "Tag:"))
        self.label_01.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Time:</span></p></body></html>"))
        self.label_05.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Handle:</span></p></body></html>"))
        self.form_title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Student Information</span></p></body></html>"))
        self.data_browser_0.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.data_browser_1.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.data_browser_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.data_browser_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.data_browser_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.data_browser_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.data_browser_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Form", "Start"))
        self.label_2.setText(_translate("Form", "End"))
        self.label_3.setText(_translate("Form", "Total"))
