from PIL import Image, ImageEnhance
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout


def adjust_contrast(self):
        value= self.Contract.value()
        pixmap = self.original_image_label.pixmap()
        if pixmap is not None:
            image = pixmap.toImage()
            image = image.convertToFormat(QtGui.QImage.Format_RGB888)
            width = image.width()
            height = image.height()
            data = image.bits().asstring(image.byteCount())

            img = Image.frombytes("RGB", (width, height), data)
            enhancer = ImageEnhance.Contrast(img)
            factor = value / 50.0
            enhanced_img = enhancer.enhance(factor)

            qimage = QtGui.QImage(enhanced_img.tobytes(), width, height, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qimage)

            self.image_label.setPixmap(pixmap)