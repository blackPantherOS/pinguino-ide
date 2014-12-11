# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/Documentos/python/developing/pinguino/pinguino-ide/qtgui/frames/board_config.ui'
#
# Created: Thu Dec 11 16:58:05 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BoardConfig(object):
    def setupUi(self, BoardConfig):
        BoardConfig.setObjectName("BoardConfig")
        BoardConfig.resize(330, 454)
        self.gridLayout_5 = QtGui.QGridLayout(BoardConfig)
        self.gridLayout_5.setVerticalSpacing(14)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_arch = QtGui.QGroupBox(BoardConfig)
        self.groupBox_arch.setAutoFillBackground(False)
        self.groupBox_arch.setObjectName("groupBox_arch")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_arch)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_arch_8 = QtGui.QRadioButton(self.groupBox_arch)
        self.radioButton_arch_8.setChecked(True)
        self.radioButton_arch_8.setObjectName("radioButton_arch_8")
        self.gridLayout.addWidget(self.radioButton_arch_8, 0, 0, 1, 1)
        self.radioButton_arch_32 = QtGui.QRadioButton(self.groupBox_arch)
        self.radioButton_arch_32.setObjectName("radioButton_arch_32")
        self.gridLayout.addWidget(self.radioButton_arch_32, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_arch, 0, 0, 1, 1)
        self.groupBox_mode = QtGui.QGroupBox(BoardConfig)
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_mode)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_mode_icsp = QtGui.QRadioButton(self.groupBox_mode)
        self.radioButton_mode_icsp.setText("ICSP")
        self.radioButton_mode_icsp.setObjectName("radioButton_mode_icsp")
        self.gridLayout_2.addWidget(self.radioButton_mode_icsp, 0, 0, 1, 1)
        self.radioButton_mode_bootloader = QtGui.QRadioButton(self.groupBox_mode)
        self.radioButton_mode_bootloader.setChecked(True)
        self.radioButton_mode_bootloader.setObjectName("radioButton_mode_bootloader")
        self.gridLayout_2.addWidget(self.radioButton_mode_bootloader, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_mode, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(318, 11, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 6, 0, 1, 1)
        self.groupBox_devices_8 = QtGui.QGroupBox(BoardConfig)
        self.groupBox_devices_8.setObjectName("groupBox_devices_8")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_devices_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_device_8 = QtGui.QGridLayout()
        self.gridLayout_device_8.setObjectName("gridLayout_device_8")
        self.gridLayout_4.addLayout(self.gridLayout_device_8, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_devices_8, 3, 0, 1, 1)
        self.groupBox_bootloader = QtGui.QGroupBox(BoardConfig)
        self.groupBox_bootloader.setObjectName("groupBox_bootloader")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_bootloader)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_bootloader_v1_v2 = QtGui.QRadioButton(self.groupBox_bootloader)
        self.radioButton_bootloader_v1_v2.setText("v1.x or v2.x")
        self.radioButton_bootloader_v1_v2.setObjectName("radioButton_bootloader_v1_v2")
        self.gridLayout_3.addWidget(self.radioButton_bootloader_v1_v2, 0, 0, 1, 1)
        self.radioButton_bootloader_v4 = QtGui.QRadioButton(self.groupBox_bootloader)
        self.radioButton_bootloader_v4.setText("v4.x")
        self.radioButton_bootloader_v4.setChecked(True)
        self.radioButton_bootloader_v4.setObjectName("radioButton_bootloader_v4")
        self.gridLayout_3.addWidget(self.radioButton_bootloader_v4, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_bootloader, 2, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_cancel = QtGui.QPushButton(BoardConfig)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_6.addWidget(self.pushButton_cancel, 1, 0, 1, 1)
        self.pushButton_ok = QtGui.QPushButton(BoardConfig)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout_6.addWidget(self.pushButton_ok, 1, 1, 1, 1)
        self.pushButton_advance = QtGui.QPushButton(BoardConfig)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_advance.setFont(font)
        self.pushButton_advance.setObjectName("pushButton_advance")
        self.gridLayout_6.addWidget(self.pushButton_advance, 0, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout_6, 8, 0, 1, 1)
        self.label_warning = QtGui.QLabel(BoardConfig)
        self.label_warning.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_warning.setObjectName("label_warning")
        self.gridLayout_5.addWidget(self.label_warning, 7, 0, 1, 1)
        self.groupBox_devices_32 = QtGui.QGroupBox(BoardConfig)
        self.groupBox_devices_32.setObjectName("groupBox_devices_32")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_devices_32)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_device_32 = QtGui.QGridLayout()
        self.gridLayout_device_32.setObjectName("gridLayout_device_32")
        self.gridLayout_7.addLayout(self.gridLayout_device_32, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_devices_32, 5, 0, 1, 1)

        self.retranslateUi(BoardConfig)
        QtCore.QObject.connect(self.radioButton_arch_32, QtCore.SIGNAL("toggled(bool)"), self.groupBox_devices_32.setVisible)
        QtCore.QObject.connect(self.radioButton_arch_8, QtCore.SIGNAL("toggled(bool)"), self.groupBox_devices_8.setVisible)
        QtCore.QObject.connect(self.groupBox_arch, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setVisible)
        QtCore.QObject.connect(self.radioButton_mode_bootloader, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setVisible)
        QtCore.QObject.connect(self.radioButton_mode_icsp, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setHidden)
        QtCore.QObject.connect(self.radioButton_arch_32, QtCore.SIGNAL("toggled(bool)"), self.groupBox_bootloader.setHidden)
        QtCore.QObject.connect(self.radioButton_arch_32, QtCore.SIGNAL("toggled(bool)"), self.pushButton_advance.setVisible)
        QtCore.QObject.connect(self.radioButton_arch_8, QtCore.SIGNAL("toggled(bool)"), self.pushButton_advance.setHidden)
        QtCore.QMetaObject.connectSlotsByName(BoardConfig)

    def retranslateUi(self, BoardConfig):
        BoardConfig.setWindowTitle(QtGui.QApplication.translate("BoardConfig", "Board Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_arch.setTitle(QtGui.QApplication.translate("BoardConfig", "Architecture", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_arch_8.setText(QtGui.QApplication.translate("BoardConfig", "8-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_arch_32.setText(QtGui.QApplication.translate("BoardConfig", "32-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_mode.setTitle(QtGui.QApplication.translate("BoardConfig", "Programming mode", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_mode_bootloader.setText(QtGui.QApplication.translate("BoardConfig", "Bootloader", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_devices_8.setTitle(QtGui.QApplication.translate("BoardConfig", "Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_bootloader.setTitle(QtGui.QApplication.translate("BoardConfig", "Bootloader", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("BoardConfig", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ok.setText(QtGui.QApplication.translate("BoardConfig", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_advance.setText(QtGui.QApplication.translate("BoardConfig", "Advance options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_warning.setText(QtGui.QApplication.translate("BoardConfig", "warning!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_devices_32.setTitle(QtGui.QApplication.translate("BoardConfig", "Devices", None, QtGui.QApplication.UnicodeUTF8))

