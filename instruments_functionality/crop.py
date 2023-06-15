from PyQt5 import QtCore, QtGui, QtWidgets
from image_to_list import add_image_to_list


def crop_image(self):
    dialog = CropImageDialog(self.image_label.pixmap())
    if dialog.exec_():
        cropped_image = dialog.get_cropped_image()
        self.image_label.setPixmap(cropped_image)
        add_image_to_list(self)


class CropImageDialog(QtWidgets.QDialog):
    def __init__(self, image):
        super(CropImageDialog, self).__init__()

        self.image = image
        self.crop_rect = QtCore.QRect()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Crop Image")

        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(self.image)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setScaledContents(True)

        self.selection_rect = QtWidgets.QRubberBand(
            QtWidgets.QRubberBand.Rectangle, self
        )
        self.selection_rect.setGeometry(self.crop_rect)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.origin = event.pos()
            self.selection_rect.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.selection_rect.show()

    def mouseMoveEvent(self, event):
        if self.origin:
            self.selection_rect.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized()
            )

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.crop_rect = self.selection_rect.geometry()
            self.selection_rect.hide()
            self.accept()

    def get_cropped_image(self):
        cropped_image = self.image.copy(self.crop_rect)
        return cropped_image
