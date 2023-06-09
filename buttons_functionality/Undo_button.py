from PIL import Image, ImageEnhance
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout




def undo_changes(self):
    #TO DO MAKE SECURITI
    if self.image_list:
        self.image_list.pop()
        self.current_image_index-=1   
        self.count_label.setText(f"Total Images: {self.current_image_index}")
        if self.image_list:
            pixmap = self.image_list[-1]
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.clear()
            self.Brightness.setValue(50)
            self.Blacknes.setValue(50)
            self.Contract.setValue(50)
            self.Blur.setValue(50)
            self.Undo_butt.setEnabled(False)  # Отключаем кнопку "Undo"
