# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout
from buttons_functionality.Upload_button import upload_image_clicked
from buttons_functionality.Undo_button import undo_changes
from sliders_functionality.Contrast_slider import adjust_contrast
from sliders_functionality.Brightness_slider import adjust_brightness
from sliders_functionality.Blackness_slider import adjust_blackness
from image_to_list import add_image_to_list
from instruments_functionality.crop import crop_image
from instruments_functionality.draw import draw_image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1157)
        MainWindow.setStyleSheet("background-color: rgb(90, 39, 86);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # added image list
        self.image_list = []
        self.current_image_index = 0
        self.image_layout = QtWidgets.QHBoxLayout()

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setObjectName("image_label")
        self.image_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        self.image_label.setFixedSize(800, 800)

        self.image_layout.addWidget(self.image_label)

        self.count_label = QtWidgets.QLabel(self.centralwidget)
        self.count_label.setObjectName("count_label")
        self.count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.count_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.count_label.setText("Total Images: 0")
        self.image_layout.addWidget(self.count_label)

        self.original_image_label = QtWidgets.QLabel(self.centralwidget)
        self.original_image_label.setObjectName("original_image_label")
        self.original_image_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.original_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.original_image_label.setFixedSize(800, 800)
        self.image_layout.addWidget(self.original_image_label)

        self.Brightness = QtWidgets.QSlider(self.centralwidget)
        self.Brightness.setGeometry(QtCore.QRect(30, 240, 191, 22))
        self.Brightness.setAutoFillBackground(False)
        self.Brightness.setStyleSheet("border-right-color: rgb(0, 255, 204);")
        self.Brightness.setProperty("value", 50)
        self.Brightness.setOrientation(QtCore.Qt.Horizontal)
        self.Brightness.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Brightness.setObjectName("Brightness")
        self.Brightness.valueChanged.connect(self.adjust_brightness)
        self.Brightness.sliderReleased.connect(self.add_image_to_list)

        self.Contrast = QtWidgets.QSlider(self.centralwidget)
        self.Contrast.setGeometry(QtCore.QRect(30, 320, 191, 22))
        self.Contrast.setSliderPosition(50)
        self.Contrast.setOrientation(QtCore.Qt.Horizontal)
        self.Contrast.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Contrast.setObjectName("Contract")
        self.Contrast.valueChanged.connect(self.adjust_contrast)
        self.Contrast.sliderReleased.connect(self.add_image_to_list)

        self.Blackness = QtWidgets.QSlider(self.centralwidget)
        self.Blackness.setGeometry(QtCore.QRect(30, 320, 191, 22))
        self.Blackness.setSliderPosition(50)
        self.Blackness.setOrientation(QtCore.Qt.Horizontal)
        self.Blackness.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Blackness.setObjectName("Blackness")
        self.Blackness.valueChanged.connect(self.adjust_blackness)
        self.Blackness.sliderReleased.connect(self.add_image_to_list)

        self.Undo_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Undo_butt.setGeometry(QtCore.QRect(20, 190, 93, 28))
        self.Undo_butt.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 8pt "Yu Gothic";'
        )
        self.Undo_butt.setObjectName("Undo_butt")
        self.Undo_butt.clicked.connect(self.undo_changes)

        self.Remove_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Remove_butt.setGeometry(QtCore.QRect(130, 190, 93, 28))
        self.Remove_butt.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 8pt "Yu Gothic";'
        )
        self.Remove_butt.setObjectName("Remove_butt")

        self.Save_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Save_butt.setGeometry(QtCore.QRect(20, 150, 201, 28))
        self.Save_butt.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 8pt "Yu Gothic";'
        )
        self.Save_butt.setObjectName("Save_butt")

        self.Saveas_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Saveas_butt.setGeometry(QtCore.QRect(20, 110, 201, 28))
        self.Saveas_butt.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 8pt "Yu Gothic";'
        )
        self.Saveas_butt.setObjectName("Saveas_butt")

        self.Upload_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Upload_butt.setGeometry(QtCore.QRect(20, 70, 201, 28))
        self.Upload_butt.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 8pt "Yu Gothic";'
        )
        self.Upload_butt.setObjectName("Upload_butt")
        self.Upload_butt.clicked.connect(self.upload_image_clicked)

        self.Brightness_label = QtWidgets.QLabel("Brightness", self.centralwidget)
        self.Contrast_label = QtWidgets.QLabel("Contrast", self.centralwidget)
        self.Blackness_label = QtWidgets.QLabel("Blackness", self.centralwidget)

        self.Instrument_crop = QtWidgets.QPushButton(self.centralwidget)
        self.Instrument_crop.setGeometry(QtCore.QRect(20, 190, 93, 28))
        self.Instrument_crop.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 8pt "Yu Gothic";'
        )
        self.Instrument_crop.setObjectName("crop_butt")
        self.Instrument_crop.clicked.connect(self.crop_image)

        self.Instrument_draw = QtWidgets.QPushButton(self.centralwidget)
        self.Instrument_draw.setGeometry(QtCore.QRect(20, 190, 93, 28))
        self.Instrument_draw.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 8pt "Yu Gothic";'
        )
        self.Instrument_draw.setObjectName("draw_butt")
        self.Instrument_draw.clicked.connect(self.draw_image)

        # buttons layout
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.Upload_butt)
        self.buttons_layout.addWidget(self.Undo_butt)
        self.buttons_layout.addWidget(self.Save_butt)
        self.buttons_layout.addWidget(self.Saveas_butt)
        self.buttons_layout.addWidget(self.Remove_butt)

        # instruments layout
        self.instruments_layout = QHBoxLayout()
        self.instruments_layout.addWidget(self.Instrument_crop)
        self.instruments_layout.addWidget(self.Brightness_label)
        self.instruments_layout.addWidget(self.Brightness)
        self.instruments_layout.addWidget(self.Contrast_label)
        self.instruments_layout.addWidget(self.Contrast)
        self.instruments_layout.addWidget(self.Blackness_label)
        self.instruments_layout.addWidget(self.Blackness)
        self.instruments_layout.addWidget(self.Instrument_draw)

        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addLayout(self.image_layout)
        self.main_layout.addLayout(self.instruments_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        slider_color = QtGui.QColor(0, 255, 204)
        slider_style = (
            "QSlider::handle:horizontal { background-color: %s; }" % slider_color.name()
        )
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        app.setStyleSheet(slider_style)
        self.image_label.setPixmap(QtGui.QPixmap())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def draw_image(self):
        draw_image(self)

    def crop_image(self):
        crop_image(self)

    def add_image_to_list(self):
        add_image_to_list(self)

    def undo_changes(self):
        undo_changes(self)

    def adjust_blackness(self):
        adjust_blackness(self)

    def adjust_brightness(self):
        adjust_brightness(self)

    def upload_image_clicked(self):
        upload_image_clicked(self)

    def adjust_contrast(self):
        adjust_contrast(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Undo_butt.setText(_translate("MainWindow", "Undo"))
        self.Remove_butt.setText(_translate("MainWindow", "Remove"))
        self.Save_butt.setText(_translate("MainWindow", "Save Image"))
        self.Saveas_butt.setText(_translate("MainWindow", "Save As"))
        self.Upload_butt.setText(_translate("MainWindow", "Upload Image"))
        self.Instrument_crop.setText(_translate("Main Window", "Crop"))
        self.Instrument_draw.setText(_translate("Main Window", "Draw"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
