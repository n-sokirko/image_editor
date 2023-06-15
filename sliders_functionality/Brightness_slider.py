from PIL import Image, ImageEnhance
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory, QFileDialog, QHBoxLayout


def adjust_brightness(self):
    value = self.Brightness.value()

    pixmap = self.image_list[-1].copy()
    if pixmap is not None:
        image = pixmap.toImage()
        if not image.isNull():
            image = image.convertToFormat(QtGui.QImage.Format_RGB888)
            width = image.width()
            height = image.height()
            data = image.bits().asstring(image.byteCount())

            img = Image.frombytes("RGB", (width, height), data)
            enhancer = ImageEnhance.Brightness(img)
            factor = value / 50.0
            enhanced_img = enhancer.enhance(factor)

            qimage = QtGui.QImage(
                enhanced_img.tobytes(), width, height, QtGui.QImage.Format_RGB888
            )
            pixmap = QtGui.QPixmap.fromImage(qimage)

            original_pixmap = self.image_list[0]
            width = original_pixmap.width()
            height = original_pixmap.height()
            scaled_pixmap = pixmap.scaled(
                width, height, QtCore.Qt.AspectRatioMode.KeepAspectRatio
            )

            self.image_label.setPixmap(scaled_pixmap)
