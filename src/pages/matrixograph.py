# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrixograph.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from filexplorer import Sleuth
from business.matrix import Demo, MatrixAnalyzer

from pages.workbooker import WorkbookRevWindow
from pages.spectrograph import SpectrumRevWindow

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MatrixRev(object):
    def setupUi(self, dSigma):
        dSigma.setObjectName("dSigma")
        dSigma.resize(1300, 900)
        dSigma.setMinimumSize(QtCore.QSize(1300, 900))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        dSigma.setFont(font)
        dSigma.setStyleSheet("QPushButton{\nbackground-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);\n}\nQPushButton:pressed{\nbackground-color: rgb(55, 55, 97);\n}")
        self.centralwidget = QtWidgets.QWidget(dSigma)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.services_layout = QtWidgets.QFrame(self.centralwidget)
        self.services_layout.setMinimumSize(QtCore.QSize(400, 880))
        self.services_layout.setMaximumSize(QtCore.QSize(800, 1760))
        self.services_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.services_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.services_layout.setObjectName("services_layout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.services_layout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.angle_layout = QtWidgets.QVBoxLayout()
        self.angle_layout.setObjectName("angle_layout")
        self.angle_info = QtWidgets.QLabel(self.services_layout)
        self.angle_info.setMinimumSize(QtCore.QSize(0, 70))
        self.angle_info.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.angle_info.setFont(font)
        self.angle_info.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_info.setObjectName("angle_info")
        self.angle_layout.addWidget(self.angle_info)
        self.angles_box = QtWidgets.QComboBox(self.services_layout)
        self.angles_box.setMinimumSize(QtCore.QSize(0, 40))
        self.angles_box.setMaximumSize(QtCore.QSize(16777215, 80))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.angles_box.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.angles_box.setFont(font)
        self.angles_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.angles_box.setObjectName("angles_box")
        self.angle_layout.addWidget(self.angles_box)
        self.verticalLayout_2.addLayout(self.angle_layout)
        self.show_button = QtWidgets.QPushButton(self.services_layout)
        self.show_button.setMinimumSize(QtCore.QSize(50, 80))
        self.show_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.show_button.setFont(font)
        self.show_button.setObjectName("show_button")
        self.verticalLayout_2.addWidget(self.show_button)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.bright_info = QtWidgets.QLabel(self.services_layout)
        self.bright_info.setMinimumSize(QtCore.QSize(0, 70))
        self.bright_info.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bright_info.setFont(font)
        self.bright_info.setObjectName("bright_info")
        self.verticalLayout.addWidget(self.bright_info)
        self.bright_layout = QtWidgets.QHBoxLayout()
        self.bright_layout.setContentsMargins(-1, 10, -1, -1)
        self.bright_layout.setObjectName("bright_layout")
        self.bright_up_button = QtWidgets.QPushButton(self.services_layout)
        self.bright_up_button.setMinimumSize(QtCore.QSize(50, 50))
        self.bright_up_button.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bright_up_button.setFont(font)
        self.bright_up_button.setObjectName("bright_up_button")
        self.bright_layout.addWidget(self.bright_up_button)
        self.bright_down_button = QtWidgets.QPushButton(self.services_layout)
        self.bright_down_button.setMinimumSize(QtCore.QSize(50, 50))
        self.bright_down_button.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bright_down_button.setFont(font)
        self.bright_down_button.setObjectName("bright_down_button")
        self.bright_layout.addWidget(self.bright_down_button)
        self.bright_def_button = QtWidgets.QPushButton(self.services_layout)
        self.bright_def_button.setMinimumSize(QtCore.QSize(50, 50))
        self.bright_def_button.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bright_def_button.setFont(font)
        self.bright_def_button.setObjectName("bright_def_button")
        self.bright_layout.addWidget(self.bright_def_button)
        self.verticalLayout.addLayout(self.bright_layout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.locus_show_button = QtWidgets.QPushButton(self.services_layout)
        self.locus_show_button.setMinimumSize(QtCore.QSize(50, 80))
        self.locus_show_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.locus_show_button.setFont(font)
        self.locus_show_button.setObjectName("locus_show_button")
        self.verticalLayout_2.addWidget(self.locus_show_button)
        self.locus_unshow_button = QtWidgets.QPushButton(self.services_layout)
        self.locus_unshow_button.setMinimumSize(QtCore.QSize(50, 80))
        self.locus_unshow_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.locus_unshow_button.setFont(font)
        self.locus_unshow_button.setObjectName("locus_unshow_button")
        self.verticalLayout_2.addWidget(self.locus_unshow_button)
        self.spectrum_button = QtWidgets.QPushButton(self.services_layout)
        self.spectrum_button.setMinimumSize(QtCore.QSize(50, 80))
        self.spectrum_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.spectrum_button.setFont(font)
        self.spectrum_button.setObjectName("spectrum_button")
        self.verticalLayout_2.addWidget(self.spectrum_button)
        self.report_button = QtWidgets.QPushButton(self.services_layout)
        self.report_button.setMinimumSize(QtCore.QSize(50, 80))
        self.report_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.report_button.setFont(font)
        self.report_button.setObjectName("report_button")
        self.verticalLayout_2.addWidget(self.report_button)
        self.start_button = QtWidgets.QPushButton(self.services_layout)
        self.start_button.setMinimumSize(QtCore.QSize(50, 80))
        self.start_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.verticalLayout_2.addWidget(self.start_button)
        self.label = QtWidgets.QLabel(self.services_layout)
        self.label.setMinimumSize(QtCore.QSize(0, 10))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.services_layout)
        self.matplotlib_layout = QtWidgets.QFrame(self.centralwidget)
        self.matplotlib_layout.setMinimumSize(QtCore.QSize(880, 880))
        self.matplotlib_layout.setStyleSheet("")
        self.matplotlib_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.matplotlib_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.matplotlib_layout.setObjectName("matplotlib_layout")
        self.horizontalLayout.addWidget(self.matplotlib_layout)
        dSigma.setCentralWidget(self.centralwidget)

        self.retranslateUi(dSigma)
        QtCore.QMetaObject.connectSlotsByName(dSigma)

    def retranslateUi(self, dSigma):
        _translate = QtCore.QCoreApplication.translate
        dSigma.setWindowTitle(_translate("dSigma", "dSigma — E-dE matrices view"))
        self.angle_info.setText(_translate("dSigma", "Choose a file:"))
        self.show_button.setText(_translate("dSigma", "Draw Matrix"))
        self.bright_info.setText(_translate("dSigma", "Brightness:"))
        self.bright_up_button.setText(_translate("dSigma", "+"))
        self.bright_down_button.setText(_translate("dSigma", "-"))
        self.bright_def_button.setText(_translate("dSigma", "Default"))
        self.locus_show_button.setText(_translate("dSigma", "Show Locuses"))
        self.locus_unshow_button.setText(_translate("dSigma", "Hide Locuses Cuts"))
        self.spectrum_button.setText(_translate("dSigma", "Spectrums of locuses"))
        self.report_button.setText(_translate("dSigma", "Workbook of experiment file"))
        self.start_button.setText(_translate("dSigma", "Start Processing"))
        self.label.setText(_translate("dSigma", "dSigma — LLENR app for analyzing E-dE matrices."))


class Ui_Matrixograph(object):
    def setupUi(self, dSigma):
        dSigma.setObjectName("dSigma")
        dSigma.resize(1300, 900)
        dSigma.setMinimumSize(QtCore.QSize(1300, 900))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        dSigma.setFont(font)
        dSigma.setStyleSheet("QPushButton{\nbackground-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);\n}\nQPushButton:pressed{\nbackground-color: rgb(55, 55, 97);\n}")
        self.centralwidget = QtWidgets.QWidget(dSigma)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.services_layout = QtWidgets.QFrame(self.centralwidget)
        self.services_layout.setMinimumSize(QtCore.QSize(400, 880))
        self.services_layout.setMaximumSize(QtCore.QSize(800, 1760))
        self.services_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.services_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.services_layout.setObjectName("services_layout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.services_layout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.angle_layout = QtWidgets.QVBoxLayout()
        self.angle_layout.setObjectName("angle_layout")
        self.angle_info = QtWidgets.QLabel(self.services_layout)
        self.angle_info.setMinimumSize(QtCore.QSize(0, 60))
        self.angle_info.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.angle_info.setFont(font)
        self.angle_info.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_info.setObjectName("angle_info")
        self.angle_layout.addWidget(self.angle_info)
        self.angles_box = QtWidgets.QComboBox(self.services_layout)
        self.angles_box.setMinimumSize(QtCore.QSize(0, 40))
        self.angles_box.setMaximumSize(QtCore.QSize(16777215, 80))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.angles_box.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.angles_box.setFont(font)
        self.angles_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.angles_box.setObjectName("angles_box")
        self.angle_layout.addWidget(self.angles_box)
        self.verticalLayout_2.addLayout(self.angle_layout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bright_info = QtWidgets.QLabel(self.services_layout)
        self.bright_info.setMinimumSize(QtCore.QSize(100, 70))
        self.bright_info.setMaximumSize(QtCore.QSize(100, 140))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bright_info.setFont(font)
        self.bright_info.setObjectName("bright_info")
        self.horizontalLayout_2.addWidget(self.bright_info)
        self.bright_layout = QtWidgets.QHBoxLayout()
        self.bright_layout.setContentsMargins(-1, 10, -1, -1)
        self.bright_layout.setObjectName("bright_layout")
        self.bright_up_button = QtWidgets.QPushButton(self.services_layout)
        self.bright_up_button.setMinimumSize(QtCore.QSize(50, 50))
        self.bright_up_button.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bright_up_button.setFont(font)
        self.bright_up_button.setObjectName("bright_up_button")
        self.bright_layout.addWidget(self.bright_up_button)
        self.bright_down_button = QtWidgets.QPushButton(self.services_layout)
        self.bright_down_button.setMinimumSize(QtCore.QSize(50, 50))
        self.bright_down_button.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bright_down_button.setFont(font)
        self.bright_down_button.setObjectName("bright_down_button")
        self.bright_layout.addWidget(self.bright_down_button)
        self.bright_def_button = QtWidgets.QPushButton(self.services_layout)
        self.bright_def_button.setMinimumSize(QtCore.QSize(50, 50))
        self.bright_def_button.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bright_def_button.setFont(font)
        self.bright_def_button.setObjectName("bright_def_button")
        self.bright_layout.addWidget(self.bright_def_button)
        self.horizontalLayout_2.addLayout(self.bright_layout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.locus_draw_button = QtWidgets.QPushButton(self.services_layout)
        self.locus_draw_button.setMinimumSize(QtCore.QSize(50, 80))
        self.locus_draw_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.locus_draw_button.setFont(font)
        self.locus_draw_button.setObjectName("locus_draw_button")
        self.verticalLayout_2.addWidget(self.locus_draw_button)
        self.locus_show_button = QtWidgets.QPushButton(self.services_layout)
        self.locus_show_button.setMinimumSize(QtCore.QSize(50, 80))
        self.locus_show_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.locus_show_button.setFont(font)
        self.locus_show_button.setObjectName("locus_show_button")
        self.verticalLayout_2.addWidget(self.locus_show_button)
        self.locus_unshow_button = QtWidgets.QPushButton(self.services_layout)
        self.locus_unshow_button.setMinimumSize(QtCore.QSize(50, 80))
        self.locus_unshow_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.locus_unshow_button.setFont(font)
        self.locus_unshow_button.setObjectName("locus_unshow_button")
        self.verticalLayout_2.addWidget(self.locus_unshow_button)
        self.spectrum_button = QtWidgets.QPushButton(self.services_layout)
        self.spectrum_button.setMinimumSize(QtCore.QSize(50, 80))
        self.spectrum_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.spectrum_button.setFont(font)
        self.spectrum_button.setObjectName("spectrum_button")
        self.verticalLayout_2.addWidget(self.spectrum_button)
        self.report_button = QtWidgets.QPushButton(self.services_layout)
        self.report_button.setMinimumSize(QtCore.QSize(50, 80))
        self.report_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.report_button.setFont(font)
        self.report_button.setObjectName("report_button")
        self.verticalLayout_2.addWidget(self.report_button)
        self.save_button = QtWidgets.QPushButton(self.services_layout)
        self.save_button.setMinimumSize(QtCore.QSize(50, 80))
        self.save_button.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_2.addWidget(self.save_button)
        self.label = QtWidgets.QLabel(self.services_layout)
        self.label.setMinimumSize(QtCore.QSize(0, 10))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.services_layout)
        self.matplotlib_layout = QtWidgets.QFrame(self.centralwidget)
        self.matplotlib_layout.setMinimumSize(QtCore.QSize(880, 880))
        self.matplotlib_layout.setStyleSheet("")
        self.matplotlib_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.matplotlib_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.matplotlib_layout.setObjectName("matplotlib_layout")
        self.horizontalLayout.addWidget(self.matplotlib_layout)
        dSigma.setCentralWidget(self.centralwidget)

        self.retranslateUi(dSigma)
        QtCore.QMetaObject.connectSlotsByName(dSigma)

    def retranslateUi(self, dSigma):
        _translate = QtCore.QCoreApplication.translate
        dSigma.setWindowTitle(_translate("dSigma", "dSigma — E-dE matrices view"))
        self.angle_info.setText(_translate("dSigma", "Choose an angle:"))
        self.bright_info.setText(_translate("dSigma", "Brightness:"))
        self.bright_up_button.setText(_translate("dSigma", "+"))
        self.bright_down_button.setText(_translate("dSigma", "-"))
        self.bright_def_button.setText(_translate("dSigma", "Default"))
        self.locus_draw_button.setText(_translate("dSigma", "Locus Draw Dialog"))
        self.locus_show_button.setText(_translate("dSigma", "Show Locuses"))
        self.locus_unshow_button.setText(_translate("dSigma", "Hide Locuses Cuts"))
        self.spectrum_button.setText(_translate("dSigma", "Spectrums of locuses"))
        self.report_button.setText(_translate("dSigma", "Workbook of experiment file"))
        self.save_button.setText(_translate("dSigma", "Save Analysis"))
        self.label.setText(_translate("dSigma", "dSigma — LLENR app for analyzing E-dE matrices."))


class MatrixRevWindow(QtWidgets.QMainWindow, Ui_MatrixRev):
    def __init__(self, directory: str) -> None:
        # SETUP OF WINDOW
        super().__init__()
        self.setupUi(self)

        self.sleuth = Sleuth(directory)

        # COLLECTING DATA AND PREPARING TO SHOW
        self.usbs = self.sleuth.usb_names()
        self.parsers = self.sleuth.all_parsers()
        self.demo: Demo = None
        self.matrix = None
        self.luminiosity = 0

        # MATPLOTLIB INITIALIZING
        layout = QtWidgets.QVBoxLayout(self.matplotlib_layout)
        self.view = FigureCanvasQTAgg(Figure(figsize=(16, 9)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self.matplotlib_layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.view)

        self.angles_box.currentTextChanged.connect(self.open_usb)
        self.angles_box.addItems(self.usbs)

        # EVENT HANDLING
        self.show_button.clicked.connect(self.draw_matrix)
        self.bright_up_button.clicked.connect(self.bright_up)
        self.bright_down_button.clicked.connect(self.bright_down)
        self.bright_def_button.clicked.connect(self.bright_default)
        self.locus_show_button.clicked.connect(self.draw_locuses)
        self.locus_unshow_button.clicked.connect(self.undraw_locuses)
        self.spectrum_button.clicked.connect(self.open_spectrums)
        self.report_button.clicked.connect(self.open_workbook)
        self.start_button.clicked.connect(self.start_analysis)

    def start_analysis(self) -> None:
        pass

    def open_usb(self) -> None:
        self.demo = Demo(self.parsers[self.angles_box.currentIndex()])
        self.matrix = self.demo.numbers
        self.luminiosity = self.matrix.mean() * 2

    def open_workbook(self) -> None:
        self.window = WorkbookRevWindow(self.demo.to_workbook())
        self.window.show()

    def bright_up(self) -> None:
        if self.luminiosity > 20:
            self.luminiosity -= 10
            self.draw_matrix()

    def bright_down(self) -> None:
        self.luminiosity += 10
        self.draw_matrix()

    def bright_default(self) -> None:
        self.luminiosity = self.matrix.mean() * 2
        self.draw_matrix()

    def draw_locuses(self) -> None:
        colors = ['blue', 'red', 'green', 'yellow', 'white']
        locuses = self.demo.locuses()
        for i in range(len(locuses)):
            xs = [locuses[i].points[j][0] for j in range(len(locuses[i].points))]
            ys = [locuses[i].points[j][1] for j in range(len(locuses[i].points))]

            self.axes.plot(xs, ys, colors[i])

        self.view.draw()

    def undraw_locuses(self) -> None:
        self.axes.clear()
        self.draw_matrix()
        self.view.draw()

    def open_spectrums(self) -> None:
        locuses = self.demo.locuses()
        spectres = []
        for locus in locuses:
            spectres.append(locus.to_spectrum())

        self.window = SpectrumRevWindow(spectres)
        self.window.show()

    def draw_matrix(self) -> None:
        self.axes.clear()
        self.axes.pcolor(self.matrix, vmin=-self.luminiosity / 2, vmax=self.luminiosity / 2, cmap='bone_r')
        self.view.draw()


class Matrixograph(QtWidgets.QMainWindow, Ui_Matrixograph):
    def __init__(self) -> None:
        # SETUP OF WINDOW
        super().__init__()
        self.setupUi(self)

        # MATPLOTLIB INITIALIZING
        layout = QtWidgets.QVBoxLayout(self.matplotlib_layout)
        self.view = FigureCanvasQTAgg(Figure(figsize=(16, 9)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self.matplotlib_layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.view)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dSigma = Matrixograph()
    dSigma.show()
    sys.exit(app.exec_())
