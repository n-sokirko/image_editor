
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout

def upload_image_clicked(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            pixmap = QtGui.QPixmap(selected_file)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio))
            self.original_image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio))  