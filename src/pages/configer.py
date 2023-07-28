# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from business.electronics import Telescope, Detector

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExperimentConfig(object):
    def setupUi(self, ExperimentConfig):
        ExperimentConfig.setObjectName("ExperimentConfig")
        ExperimentConfig.resize(670, 500)
        ExperimentConfig.setMinimumSize(QtCore.QSize(670, 500))
        ExperimentConfig.setMaximumSize(QtCore.QSize(670, 500))
        ExperimentConfig.setStyleSheet("QPushButton{\nbackground-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);\n}\nQPushButton:pressed{\nbackground-color: rgb(55, 55, 97);\n}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ExperimentConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.telescope_layout = QtWidgets.QVBoxLayout()
        self.telescope_layout.setObjectName("telescope_layout")
        self.telescope_info = QtWidgets.QLabel(ExperimentConfig)
        self.telescope_info.setMinimumSize(QtCore.QSize(0, 50))
        self.telescope_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.telescope_info.setFont(font)
        self.telescope_info.setAlignment(QtCore.Qt.AlignCenter)
        self.telescope_info.setObjectName("telescope_info")
        self.telescope_layout.addWidget(self.telescope_info)
        self.detector_layout = QtWidgets.QHBoxLayout()
        self.detector_layout.setObjectName("detector_layout")
        self.de_layout = QtWidgets.QVBoxLayout()
        self.de_layout.setObjectName("de_layout")
        self.de_detector_info = QtWidgets.QLabel(ExperimentConfig)
        self.de_detector_info.setMinimumSize(QtCore.QSize(0, 50))
        self.de_detector_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.de_detector_info.setFont(font)
        self.de_detector_info.setAlignment(QtCore.Qt.AlignCenter)
        self.de_detector_info.setObjectName("de_detector_info")
        self.de_layout.addWidget(self.de_detector_info)
        self.de_element_box = QtWidgets.QComboBox(ExperimentConfig)
        self.de_element_box.setMinimumSize(QtCore.QSize(0, 40))
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
        self.de_element_box.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.de_element_box.setFont(font)
        self.de_element_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.de_element_box.setObjectName("de_element_box")
        self.de_element_box.addItem("")
        self.de_element_box.addItem("")
        self.de_element_box.addItem("")
        self.de_layout.addWidget(self.de_element_box)
        self.de_thickness_layout = QtWidgets.QHBoxLayout()
        self.de_thickness_layout.setObjectName("de_thickness_layout")
        self.de_thick_info = QtWidgets.QLabel(ExperimentConfig)
        self.de_thick_info.setMinimumSize(QtCore.QSize(0, 50))
        self.de_thick_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.de_thick_info.setFont(font)
        self.de_thick_info.setObjectName("de_thick_info")
        self.de_thickness_layout.addWidget(self.de_thick_info)
        self.de_thickness_box = QtWidgets.QDoubleSpinBox(ExperimentConfig)
        self.de_thickness_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.de_thickness_box.setFont(font)
        self.de_thickness_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.de_thickness_box.setMaximum(999999999.99)
        self.de_thickness_box.setProperty("value", 50.0)
        self.de_thickness_box.setObjectName("de_thickness_box")
        self.de_thickness_layout.addWidget(self.de_thickness_box)
        self.de_layout.addLayout(self.de_thickness_layout)
        self.de_resolution_layout = QtWidgets.QHBoxLayout()
        self.de_resolution_layout.setObjectName("de_resolution_layout")
        self.de_res_info = QtWidgets.QLabel(ExperimentConfig)
        self.de_res_info.setMinimumSize(QtCore.QSize(0, 50))
        self.de_res_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.de_res_info.setFont(font)
        self.de_res_info.setObjectName("de_res_info")
        self.de_resolution_layout.addWidget(self.de_res_info)
        self.de_resolution_box = QtWidgets.QDoubleSpinBox(ExperimentConfig)
        self.de_resolution_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.de_resolution_box.setFont(font)
        self.de_resolution_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.de_resolution_box.setMaximum(999999999.99)
        self.de_resolution_box.setProperty("value", 1.0)
        self.de_resolution_box.setObjectName("de_resolution_box")
        self.de_resolution_layout.addWidget(self.de_resolution_box)
        self.de_layout.addLayout(self.de_resolution_layout)
        self.detector_layout.addLayout(self.de_layout)
        self.e_layout = QtWidgets.QVBoxLayout()
        self.e_layout.setObjectName("e_layout")
        self.e_detector_info = QtWidgets.QLabel(ExperimentConfig)
        self.e_detector_info.setMinimumSize(QtCore.QSize(0, 50))
        self.e_detector_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.e_detector_info.setFont(font)
        self.e_detector_info.setAlignment(QtCore.Qt.AlignCenter)
        self.e_detector_info.setObjectName("e_detector_info")
        self.e_layout.addWidget(self.e_detector_info)
        self.e_element_box = QtWidgets.QComboBox(ExperimentConfig)
        self.e_element_box.setMinimumSize(QtCore.QSize(0, 40))
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
        self.e_element_box.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.e_element_box.setFont(font)
        self.e_element_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.e_element_box.setObjectName("e_element_box")
        self.e_element_box.addItem("")
        self.e_element_box.addItem("")
        self.e_element_box.addItem("")
        self.e_layout.addWidget(self.e_element_box)
        self.e_thickness_layout = QtWidgets.QHBoxLayout()
        self.e_thickness_layout.setObjectName("e_thickness_layout")
        self.e_thick_info = QtWidgets.QLabel(ExperimentConfig)
        self.e_thick_info.setMinimumSize(QtCore.QSize(0, 50))
        self.e_thick_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.e_thick_info.setFont(font)
        self.e_thick_info.setObjectName("e_thick_info")
        self.e_thickness_layout.addWidget(self.e_thick_info)
        self.e_thickness_box = QtWidgets.QDoubleSpinBox(ExperimentConfig)
        self.e_thickness_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.e_thickness_box.setFont(font)
        self.e_thickness_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.e_thickness_box.setMaximum(999999999.99)
        self.e_thickness_box.setProperty("value", 2000.0)
        self.e_thickness_box.setObjectName("e_thickness_box")
        self.e_thickness_layout.addWidget(self.e_thickness_box)
        self.e_layout.addLayout(self.e_thickness_layout)
        self.e_resolution_layout = QtWidgets.QHBoxLayout()
        self.e_resolution_layout.setObjectName("e_resolution_layout")
        self.e_res_info = QtWidgets.QLabel(ExperimentConfig)
        self.e_res_info.setMinimumSize(QtCore.QSize(0, 50))
        self.e_res_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.e_res_info.setFont(font)
        self.e_res_info.setObjectName("e_res_info")
        self.e_resolution_layout.addWidget(self.e_res_info)
        self.e_resolution_box = QtWidgets.QDoubleSpinBox(ExperimentConfig)
        self.e_resolution_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.e_resolution_box.setFont(font)
        self.e_resolution_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.e_resolution_box.setMaximum(999999999.99)
        self.e_resolution_box.setProperty("value", 1.0)
        self.e_resolution_box.setObjectName("e_resolution_box")
        self.e_resolution_layout.addWidget(self.e_resolution_box)
        self.e_layout.addLayout(self.e_resolution_layout)
        self.detector_layout.addLayout(self.e_layout)
        self.telescope_layout.addLayout(self.detector_layout)
        self.verticalLayout.addLayout(self.telescope_layout)
        self.geometry_layout = QtWidgets.QVBoxLayout()
        self.geometry_layout.setObjectName("geometry_layout")
        self.geom_info = QtWidgets.QLabel(ExperimentConfig)
        self.geom_info.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.geom_info.setFont(font)
        self.geom_info.setAlignment(QtCore.Qt.AlignCenter)
        self.geom_info.setObjectName("geom_info")
        self.geometry_layout.addWidget(self.geom_info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radius_layout = QtWidgets.QVBoxLayout()
        self.radius_layout.setObjectName("radius_layout")
        self.radius_info = QtWidgets.QLabel(ExperimentConfig)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radius_info.setFont(font)
        self.radius_info.setObjectName("radius_info")
        self.radius_layout.addWidget(self.radius_info)
        self.radius_box = QtWidgets.QDoubleSpinBox(ExperimentConfig)
        self.radius_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radius_box.setFont(font)
        self.radius_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.radius_box.setMaximum(999999999.99)
        self.radius_box.setProperty("value", 5.0)
        self.radius_box.setObjectName("de_thickness_box_2")
        self.radius_layout.addWidget(self.radius_box)
        self.horizontalLayout.addLayout(self.radius_layout)
        self.distance_layout = QtWidgets.QVBoxLayout()
        self.distance_layout.setObjectName("distance_layout")
        self.distance_info = QtWidgets.QLabel(ExperimentConfig)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_info.setFont(font)
        self.distance_info.setObjectName("distance_info")
        self.distance_layout.addWidget(self.distance_info)
        self.distance_box = QtWidgets.QDoubleSpinBox(ExperimentConfig)
        self.distance_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.distance_box.setFont(font)
        self.distance_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.distance_box.setMaximum(999999999.99)
        self.distance_box.setProperty("value", 200.0)
        self.distance_box.setObjectName("de_thickness_box_3")
        self.distance_layout.addWidget(self.distance_box)
        self.horizontalLayout.addLayout(self.distance_layout)
        self.geometry_layout.addLayout(self.horizontalLayout)
        self.accept_button = QtWidgets.QPushButton(ExperimentConfig)
        self.accept_button.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.accept_button.setFont(font)
        self.accept_button.setObjectName("accept_button")
        self.geometry_layout.addWidget(self.accept_button)
        self.verticalLayout.addLayout(self.geometry_layout)

        self.retranslateUi(ExperimentConfig)
        QtCore.QMetaObject.connectSlotsByName(ExperimentConfig)

    def retranslateUi(self, ExperimentConfig):
        _translate = QtCore.QCoreApplication.translate
        ExperimentConfig.setWindowTitle(_translate("ExperimentConfig", "dSigma — Experimenthal configuration window"))
        self.telescope_info.setText(_translate("ExperimentConfig", "Telescope"))
        self.de_detector_info.setText(_translate("ExperimentConfig", "dE Detector"))
        self.de_element_box.setItemText(0, _translate("ExperimentConfig", "Si"))
        self.de_element_box.setItemText(1, _translate("ExperimentConfig", "HpGe"))
        self.de_element_box.setItemText(2, _translate("ExperimentConfig", "C3H6"))
        self.de_thick_info.setText(_translate("ExperimentConfig", "Thickness(mkm):"))
        self.de_res_info.setText(_translate("ExperimentConfig", "Resolution (keV):"))
        self.e_detector_info.setText(_translate("ExperimentConfig", "E Detector"))
        self.e_element_box.setItemText(0, _translate("ExperimentConfig", "Si"))
        self.e_element_box.setItemText(1, _translate("ExperimentConfig", "HpGe"))
        self.e_element_box.setItemText(2, _translate("ExperimentConfig", "C3H6"))
        self.e_thick_info.setText(_translate("ExperimentConfig", "Thickness(mkm):"))
        self.e_res_info.setText(_translate("ExperimentConfig", "Resolution (keV):"))
        self.geom_info.setText(_translate("ExperimentConfig", "Geometry"))
        self.radius_info.setText(_translate("ExperimentConfig", "Radius of telescope\'s window (mm)"))
        self.distance_info.setText(_translate("ExperimentConfig", "Distance between target and telescope (mm)"))
        self.accept_button.setText(_translate("ExperimentConfig", "Accept"))


class Configer(QtWidgets.QDialog, Ui_ExperimentConfig):
    def __init__(self) -> None:
        # SETUP WINDOW
        super().__init__()
        self.setupUi(self)

        # EVENT HANDLING
        self.accept_button.clicked.connect(self.end)

    def end(self) -> None:
        self.hide()

    def gather_telescope(self) -> Telescope:
        de = self.de_detector()
        e = self.e_detector()

        radius = self.radius_box.value()
        distance = self.distance_box.value()

        return Telescope(e, de, radius, distance)

    def de_detector(self) -> Detector:
        madeof = self.de_element_box.currentText()
        thickness = self.de_thickness_box.value()
        resolution = self.de_resolution_box.value()

        return Detector(madeof, thickness, resolution)

    def e_detector(self) -> Detector:
        madeof = self.e_element_box.currentText()
        thickness = self.e_thickness_box.value()
        resolution = self.e_resolution_box.value()

        return Detector(madeof, thickness, resolution)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExperimentConfig = Configer()
    ExperimentConfig.show()
    sys.exit(app.exec_())
