from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog


def show_original_image(self):
    if self.original_image_label.isHidden():
        self.original_image_label.show()
    else:
        self.original_image_label.hide()
