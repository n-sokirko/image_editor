from PyQt5.QtWidgets import QLabel, QMainWindow, QDialog, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from image_to_list import add_image_to_list
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog


def draw_image(self):
    dialog = MyImageEditorDialog(self.image_label.pixmap())
    if dialog.exec_():
        drawed_image = dialog.get_drawed_image()
        self.image_label.setPixmap(drawed_image)
        add_image_to_list(self)


class MyImageEditorDialog(QDialog):
    def __init__(self, image):
        super(MyImageEditorDialog, self).__init__()

        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, 800, 600)

        self.current_image = QPixmap(image)
        self.temp_image = self.current_image.copy()
        self.painting = False

        self.image_label.setPixmap(self.current_image)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Draw Image")
        self.image_label.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept_and_close)
        layout.addWidget(ok_button)

        color_button = QPushButton("Choose color", self)
        color_button.clicked.connect(self.choose_pen_color)
        layout.addWidget(color_button)

        self.setLayout(layout)

    def choose_pen_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color

    def accept_and_close(self):
        self.accept()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.painting = True
            self.temp_image = self.current_image.copy()

    def mouseMoveEvent(self, event):
        if self.painting:
            painter = QPainter(self.temp_image)
            pen = QPen()
            pen.setColor(self.pen_color)
            pen.setWidth(2)
            painter.setPen(pen)
            painter.drawPoint(event.pos())
            self.image_label.setPixmap(self.temp_image)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.painting:
            self.painting = False
            self.current_image = self.temp_image.copy()
            self.image_label.setPixmap(self.current_image)

    def get_drawed_image(self):
        return self.current_image.copy()
