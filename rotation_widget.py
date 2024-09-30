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
        #Установка стартовых значений
        self.polygon = [QPointF(100, 100), QPointF(150, 100), QPointF(125, 150)]  # Пример многоугольника (треугольник)
        self.rotation_point = QPointF(100, 100)  # Точка вращения
        self.angle = 0  # Угол поворота
        self.is_clockwise = True # По часовой
        self.setMinimumSize(400, 400)
        self.setMinimumSize(400, 400)

    @override
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.polygon = [QPointF(self.rotation_point.x(), self.rotation_point.y()),
                        QPointF(self.rotation_point.x() + 50, self.rotation_point.y()),
                        QPointF(self.rotation_point.x() + 25,
                                self.rotation_point.y() + 50)]  # Пример многоугольника (треугольник)

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

    # Функция для поворота точки относительно центра на заданный угол
    def rotate_point(self, point, angle, center):
        #Переводим угол в радианы
        rad = math.radians(angle)

        #Вычисляем по формуле
        coord = np.array([[point.x() - center.x(), point.y() - center.y()]])
        rotation_matrix = np.array([[math.cos(rad), math.sin(rad)], [-math.sin(rad), math.cos(rad)]])
        result = np.dot(coord, rotation_matrix)

        #Возвращае новые координаты точки
        return QPointF(result[0, 0] + center.x(), result[0, 1] + center.y())

    def rotate_polygon(self):
        #Функция для поворота всего многоугольника
        #Берем каждую точку и на ней выполняем метод rotate_point()
        return [self.rotate_point(p, self.angle, self.rotation_point) for p in self.polygon]