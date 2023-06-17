from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog


def save_image_as(self):
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
    file_dialog.setAcceptMode(QFileDialog.AcceptSave)
    if file_dialog.exec_():
        selected_file = file_dialog.selectedFiles()[0]
        pixmap = self.image_list[-1]
        image = pixmap.toImage()
        image.save(selected_file)
