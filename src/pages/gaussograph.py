import numpy

from business.analysis import Spectrum, Peak

from matplotlib.figure import Figure
from matplotlib.backend_bases import MouseEvent, MouseButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import (
    QWidget, QMainWindow, QVBoxLayout, 
    QHBoxLayout, QPushButton, QFrame, QLabel
)


class Ui_Gaussograph(object):
    def setupUi(self, Gaussograph):
        Gaussograph.setObjectName("Gaussograph")
        Gaussograph.resize(1000, 600)
        Gaussograph.setMinimumSize(QSize(1000, 600))
        Gaussograph.setStyleSheet("QPushButton{background-color: rgb(85, 85, 127);color: rgb(255, 255, 255);font: 63 12pt \"Bahnschrift SemiBold\";}QPushButton:pressed{background-color: rgb(55, 55, 97);}")
        self.centralwidget = QWidget(Gaussograph)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.matplotlib_layout = QFrame(self.centralwidget)
        self.matplotlib_layout.setMinimumSize(QSize(700, 0))
        self.matplotlib_layout.setMaximumSize(QSize(2100, 16777215))
        self.matplotlib_layout.setFrameShape(QFrame.StyledPanel)
        self.matplotlib_layout.setFrameShadow(QFrame.Raised)
        self.matplotlib_layout.setObjectName("matplotlib_layout")
        self.horizontalLayout.addWidget(self.matplotlib_layout)
        self.services_layout = QFrame(self.centralwidget)
        self.services_layout.setMinimumSize(QSize(280, 0))
        self.services_layout.setMaximumSize(QSize(840, 16777215))
        self.services_layout.setFrameShape(QFrame.StyledPanel)
        self.services_layout.setFrameShadow(QFrame.Raised)
        self.services_layout.setObjectName("services_layout")
        self.verticalLayout = QVBoxLayout(self.services_layout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_label = QLabel(self.services_layout)
        self.info_label.setStyleSheet("background-color: rgb(85, 85, 127);\nfont: 63 12pt \"Bahnschrift SemiBold\";\ncolor: rgb(255, 255, 255);")
        self.info_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        self.approximate_button = QPushButton(self.services_layout)
        self.approximate_button.setMinimumSize(QSize(0, 70))
        self.approximate_button.setObjectName("approximate_button")
        self.verticalLayout.addWidget(self.approximate_button)
        self.close_button = QPushButton(self.services_layout)
        self.close_button.setMinimumSize(QSize(0, 70))
        self.close_button.setObjectName("close_button")
        self.verticalLayout.addWidget(self.close_button)
        self.horizontalLayout.addWidget(self.services_layout)
        Gaussograph.setCentralWidget(self.centralwidget)

        self.retranslateUi(Gaussograph)
        QMetaObject.connectSlotsByName(Gaussograph)

    def retranslateUi(self, Gaussograph):
        _translate = QCoreApplication.translate
        Gaussograph.setWindowTitle(_translate("Gaussograph", "dSigma — Gaussian Approximating Dialog"))
        self.info_label.setText(_translate("Gaussograph", "Gaussian information"))
        self.approximate_button.setText(_translate("Gaussograph", "Approximate"))
        self.close_button.setText(_translate("Gaussograph", "Close"))


class Gaussograph(QMainWindow, Ui_Gaussograph):
    def __init__(self, spectrum: Spectrum, pointers: tuple[int, int]) -> None:
        # SETUP OF WINDOW
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icon.ico'))

        # DATA
        self.spectrum = spectrum
        self.pointers = pointers
        self.gauss = None

        # MATPLOTLIB INITIALIZING
        layout = QVBoxLayout(self.matplotlib_layout)
        self.view = FigureCanvasQTAgg(Figure(figsize=(16, 9)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self.matplotlib_layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.view)

        # EVENT HANDLING
        self.approximate_button.clicked.connect(self.approximate)
        self.close_button.clicked.connect(self.close)

        self.draw()

    def approximate(self) -> None:
        if self.gauss is None:
            start = min(self.pointers)
            stop = max(self.pointers)

            xs = numpy.arange(start + 1, stop + 1)
            ys = self.spectrum.data[start: stop]

            self.gauss = Peak.describe(xs, ys, ys.argmax())
            self.draw()

    def draw(self) -> None:
        start = min(self.pointers) - int(len(self.spectrum.data) * 0.05)
        stop = max(self.pointers) + int(len(self.spectrum.data) * 0.05)
        height = self.spectrum.data[start: stop].max()

        self.axes.clear()
        for i in range(start, stop):
            self.axes.plot([i + 1, i + 1], [0, self.spectrum.data[i]], color='blue')

        for i in range(len(self.pointers)):
            self.axes.plot([self.pointers[i], self.pointers[i]], [0, height], color='red')

        if self.gauss is not None:
            self.axes.plot(self.gauss.three_sigma(), self.gauss.function(), color='green')

        self.axes.plot(numpy.arange(start + 1, stop + 1), self.spectrum.data[start: stop], color='blue')
        self.view.draw()


if __name__ == "__main__":
    pass