# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/Documentos/Desarrollo/Pinguino/GitHub/pinguino-ide/pinguino/qtgui/frames/about.ui'
#
# Created: Wed Mar 16 13:19:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(656, 507)
        self.gridLayout_2 = QtGui.QGridLayout(About)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtGui.QStackedWidget(About)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtGui.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(620, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(620, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 3)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_credits = QtGui.QPushButton(self.page)
        self.pushButton_credits.setDefault(True)
        self.pushButton_credits.setObjectName("pushButton_credits")
        self.gridLayout_4.addWidget(self.pushButton_credits, 0, 0, 1, 1)
        self.pushButton_close = QtGui.QPushButton(self.page)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_4.addWidget(self.pushButton_close, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 6, 0, 1, 3)
        self.label = QtGui.QLabel(self.page)
        self.label.setMinimumSize(QtCore.QSize(256, 0))
        self.label.setMaximumSize(QtCore.QSize(256, 16777215))
        self.label.setPixmap(QtGui.QPixmap(":/logo/art/pinguino11.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.page)
        self.label_10.setText("<html><head/><body><p><a href=\"http://pinguino.cc/\"><span style=\" text-decoration: underline; color:#6299e1;\">http://pinguino.cc/</span></a></p></body></html>")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.label_name = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setWeight(75)
        font.setBold(True)
        self.label_name.setFont(font)
        self.label_name.setText("Pinguino 11.0")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_7 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtGui.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.page_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtGui.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setText("<html><head/><body><p align=\"center\">Jean-Pierre Mandon</p><p align=\"center\">Régis Blanchot</p><p align=\"center\">Marcus Fazzi</p><p align=\"center\">Jesus Carmona Esteban</p><p align=\"center\">Alfred Broda</p><p align=\"center\">Yeison Cardona</p><p align=\"center\">Henk Van Beek</p><p align=\"center\">Björn Pfeiffer</p><p align=\"center\">Alexis Sánchez</p></body></html>")
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setText("<html><head/><body><p align=\"center\">Benoit Espinola</p><p align=\"center\">Sebastien Koechlin</p><p align=\"center\">Ivan Ricondo</p><p align=\"center\">Jesus Carmona Esteban</p><p align=\"center\">Marcus Fazzi</p><p align=\"center\">Régis Blanchot</p></body></html>")
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setText("<html><head/><body><p align=\"center\">Joan Espinoza</p><p align=\"center\">Alexis Sánchez</p><p align=\"center\">Régis Blanchot</p><p align=\"center\">Moreno Manzini </p><p align=\"center\">Yeison Cardona</p><p align=\"center\">&quot;Avrin&quot;<br/></p></body></html>")
        self.label_6.setObjectName("label_6")
        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setText("<html><head/><body><p align=\"center\">France Cadet</p><p align=\"center\">Laurent Costes</p><p align=\"center\">Daniel Rodrí­guez</p></body></html>")
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_7.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_license = QtGui.QPushButton(self.page_2)
        self.pushButton_license.setDefault(True)
        self.pushButton_license.setObjectName("pushButton_license")
        self.gridLayout_6.addWidget(self.pushButton_license, 0, 0, 1, 1)
        self.pushButton_close_2 = QtGui.QPushButton(self.page_2)
        self.pushButton_close_2.setObjectName("pushButton_close_2")
        self.gridLayout_6.addWidget(self.pushButton_close_2, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_13 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton_close_3 = QtGui.QPushButton(self.page_3)
        self.pushButton_close_3.setObjectName("pushButton_close_3")
        self.gridLayout_12.addWidget(self.pushButton_close_3, 0, 1, 1, 1)
        self.pushButton_about = QtGui.QPushButton(self.page_3)
        self.pushButton_about.setDefault(True)
        self.pushButton_about.setObjectName("pushButton_about")
        self.gridLayout_12.addWidget(self.pushButton_about, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 4, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem4, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.page_3)
        self.plainTextEdit.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("Pinguino is free software; you can redistribute it and/or modify it\n"
"under the terms of the GNU General Public License as published by the Free Software Foundation;\n"
"either version 2 of the License, or (at your option) any later version.\n"
"\n"
"Pinguino is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;\n"
"without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n"
"See the GNU General Public License for more details. You should have received a copy of\n"
"the GNU General Public License along with File Hunter; if not, write to\n"
"the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_13.addWidget(self.plainTextEdit, 2, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem5, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(About)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("About", "<html><head/><body><p align=\"center\">Pinguino is an Open Software and Open Hardware<br>Arduino-like project. Boards are based on 8 or 32-bit USB built-in<br>Microchip microcontrollers. The main goal is to build a real<br>USB system without USB to serial converter.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_credits.setText(QtGui.QApplication.translate("About", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("About", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("About", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("About", "Write by", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("About", "Docummented by", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("About", "Translated by", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("About", "Art by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_license.setText(QtGui.QApplication.translate("About", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close_2.setText(QtGui.QApplication.translate("About", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close_3.setText(QtGui.QApplication.translate("About", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_about.setText(QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("About", "License", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
