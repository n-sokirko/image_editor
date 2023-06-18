from PIL import Image
from image_to_list import add_image_to_list
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage


def rotate_image_right(self):
    pixmap = self.image_list[-1].copy()
    image = pixmap.toImage()

    width = image.width()
    height = image.height()
    buffer = image.bits().asstring(width * height * 4)
    pil_image = Image.frombuffer("RGBA", (width, height), buffer, "raw", "RGBA", 0, 1)

    rotated_image = pil_image.rotate(-90, expand=True)

    rotated_pixmap = QPixmap.fromImage(
        QImage(
            rotated_image.tobytes(),
            rotated_image.size[0],
            rotated_image.size[1],
            QImage.Format_RGBA8888,
        )
    )

    self.image_label.setPixmap(rotated_pixmap)
    add_image_to_list(self)
