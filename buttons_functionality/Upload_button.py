from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout


def upload_image_clicked(self):
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    if file_dialog.exec_():
        selected_image = file_dialog.selectedFiles()[0]
        self.file_path = selected_image
        pixmap = QtGui.QPixmap(selected_image)
        self.image_label.setPixmap(pixmap)
        self.original_image_label.setPixmap(pixmap)
        self.image_list.append(pixmap)
        self.current_image_index = 0
