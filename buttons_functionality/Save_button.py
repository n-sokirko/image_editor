from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog
from buttons_functionality.Saveas_button import save_image_as


def save_image(self):
    if self.file_path:
        selected_image = self.image_list[-1]
        image = selected_image.toImage()
        image.save(self.file_path)
        pixmap = QtGui.QPixmap(selected_image)
        self.original_image_label.setPixmap(pixmap)
