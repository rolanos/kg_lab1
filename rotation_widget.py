import sys
import math
import numpy as np

from typing import override

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPointF

class RotationWidget(QWidget):

    @override
    def __init__(self):
        super().__init__()
        self.polygon = [QPointF(100, 100), QPointF(150, 100), QPointF(125, 150)]  # Пример многоугольника (треугольник)
        self.rotation_point = QPointF(100, 100)  # Точка вращения
        self.angle = 0  # Угол поворота
        self.init_ui()

    @override
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Рисуем исходный многоугольник
        painter.setPen(QPen(Qt.blue, 2))
        painter.drawPolygon(*self.polygon)

        # Рисуем точку вращения
        painter.setPen(QPen(Qt.red, 6))
        painter.drawPoint(self.rotation_point)

        # Рисуем повернутый многоугольник
        painter.setPen(QPen(Qt.green, 2))
        rotated_polygon = self.rotate_polygon()
        painter.drawPolygon(*rotated_polygon)

    def init_ui(self):
        self.setMinimumSize(400, 400)

    def rotate_point(self, point, angle, center):
        #Функция для поворота точки относительно центра на заданный угол
        rad = math.radians(angle)
        coord = np.array([[point.x() - center.x(), point.y() - center.y()]])
        rotation_matrix = np.array([[math.cos(rad), math.sin(rad)], [-math.sin(rad), math.cos(rad)]])
        result = np.dot(coord, rotation_matrix)
        x_new = result[0, 0] + center.x()
        y_new = result[0, 1] + center.y()

        return QPointF(x_new, y_new)

    def rotate_polygon(self):
        #Функция для поворота всего многоугольника
        return [self.rotate_point(p, self.angle, self.rotation_point) for p in self.polygon]