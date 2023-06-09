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
from sliders_functionality.Contrast_slider import adjust_contrast



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1157)
        MainWindow.setStyleSheet("background-color: rgb(90, 39, 86);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.image_layout = QtWidgets.QHBoxLayout()
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setObjectName("image_label")
        self.image_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)  
        self.image_label.setMaximumSize(800, 800)
        self.image_layout.addWidget(self.image_label)        

        self.original_image_label = QtWidgets.QLabel(self.centralwidget)
        self.original_image_label.setObjectName("original_image_label")
        self.original_image_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  
        self.original_image_label.setAlignment(QtCore.Qt.AlignCenter)  
        self.original_image_label.setMaximumSize(800, 800)
        self.image_layout.addWidget(self.original_image_label)  
             

        self.Brightness = QtWidgets.QSlider(self.centralwidget)
        self.Brightness.setGeometry(QtCore.QRect(30, 240, 191, 22))
        self.Brightness.setAutoFillBackground(False)
        self.Brightness.setStyleSheet("border-right-color: rgb(0, 255, 204);")
        self.Brightness.setProperty("value", 50)
        self.Brightness.setOrientation(QtCore.Qt.Horizontal)
        self.Brightness.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Brightness.setObjectName("Brightness")

        self.Blacknes = QtWidgets.QSlider(self.centralwidget)
        self.Blacknes.setGeometry(QtCore.QRect(30, 280, 191, 22))
        self.Blacknes.setSliderPosition(50)
        self.Blacknes.setOrientation(QtCore.Qt.Horizontal)
        self.Blacknes.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Blacknes.setTickInterval(0)
        self.Blacknes.setObjectName("Blacknes")

        self.Contract = QtWidgets.QSlider(self.centralwidget)
        self.Contract.setGeometry(QtCore.QRect(30, 320, 191, 22))
        self.Contract.setSliderPosition(50)
        self.Contract.setOrientation(QtCore.Qt.Horizontal)
        self.Contract.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Contract.setObjectName("Contract")
        self.Contract.valueChanged.connect(self.adjust_contrast)

        self.Blur = QtWidgets.QSlider(self.centralwidget)
        self.Blur.setGeometry(QtCore.QRect(30, 360, 191, 22))
        self.Blur.setSliderPosition(50)
        self.Blur.setOrientation(QtCore.Qt.Horizontal)
        self.Blur.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Blur.setObjectName("Blur")
        

        

        self.Undo_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Undo_butt.setGeometry(QtCore.QRect(20, 190, 93, 28))
        self.Undo_butt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Yu Gothic\";")
        self.Undo_butt.setObjectName("Undo_butt")

        self.Remove_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Remove_butt.setGeometry(QtCore.QRect(130, 190, 93, 28))
        self.Remove_butt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Yu Gothic\";")
        self.Remove_butt.setObjectName("Remove_butt")

        self.Save_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Save_butt.setGeometry(QtCore.QRect(20, 150, 201, 28))
        self.Save_butt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Yu Gothic\";")
        self.Save_butt.setObjectName("Save_butt")

        self.Saveas_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Saveas_butt.setGeometry(QtCore.QRect(20, 110, 201, 28))
        self.Saveas_butt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Yu Gothic\";")
        self.Saveas_butt.setObjectName("Saveas_butt")

        self.Upload_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Upload_butt.setGeometry(QtCore.QRect(20, 70, 201, 28))
        self.Upload_butt.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 8pt \"Yu Gothic\";")
        self.Upload_butt.setObjectName("Upload_butt")
        self.Upload_butt.clicked.connect(self.upload_image_clicked)

        self.Brightness_label = QtWidgets.QLabel("Brightness", self.centralwidget)
        self.Blacknes_label = QtWidgets.QLabel("Blacknes", self.centralwidget)
        self.Contract_label = QtWidgets.QLabel("Contract", self.centralwidget)
        self.Blur_label = QtWidgets.QLabel("Blur", self.centralwidget)
        

        self.buttons_layout = QHBoxLayout()
        
        self.buttons_layout.addWidget(self.Upload_butt)
        self.buttons_layout.addWidget(self.Undo_butt)
        self.buttons_layout.addWidget(self.Save_butt)
        self.buttons_layout.addWidget(self.Saveas_butt)
        self.buttons_layout.addWidget(self.Remove_butt)
        self.buttons_layout.addWidget(self.Blacknes_label)
        self.buttons_layout.addWidget(self.Blacknes)
        self.buttons_layout.addWidget(self.Brightness_label)
        self.buttons_layout.addWidget(self.Brightness)
        self.buttons_layout.addWidget(self.Contract_label)
        self.buttons_layout.addWidget(self.Contract)
        self.buttons_layout.addWidget(self.Blur_label)
        self.buttons_layout.addWidget(self.Blur)




        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addLayout(self.image_layout)
        
       

        
        MainWindow.setCentralWidget(self.centralwidget)
        
        slider_color = QtGui.QColor(0, 255, 204)
        slider_style = "QSlider::handle:horizontal { background-color: %s; }" % slider_color.name()
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        app.setStyleSheet(slider_style)
        self.image_label.setPixmap(QtGui.QPixmap())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        
    
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
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    