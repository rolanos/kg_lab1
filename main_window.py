from PyQt5.QtWidgets import QCheckBox, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout

from rotation_widget import RotationWidget

from PyQt5.QtCore import QPointF


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Поворот плоского объекта. Будило Зашляхтин Костенко.')
        self.setGeometry(100, 100, 500, 500)

        self.rotation_widget = RotationWidget()

        # Поля для ввода координат точки вращения
        self.x_input = QLineEdit(self)
        self.x_input.setText('100')

        self.y_input = QLineEdit(self)
        self.y_input.setText('100')

        self.angle_input = QLineEdit(self)
        self.angle_input.setText('0')

        self.x_input.setPlaceholderText("OX")
        self.y_input.setPlaceholderText("OY")
        self.angle_input.setPlaceholderText("Угол поворота")

        # Чекбокс для направления поворота (против часовой стрелки)
        self.ccw_checkbox = QCheckBox("Против часовой стрелки", self)

        # Кнопка для применения изменений
        self.apply_button = QPushButton('Применить', self)
        self.apply_button.clicked.connect(self.apply_rotation)

        self.error = QLabel('', self)

        # Создаем горизонтальные макеты для координат OX и OY
        coord_layout = QHBoxLayout()
        coord_layout.addWidget(QLabel("OX:"))
        coord_layout.addWidget(self.x_input)
        coord_layout.addWidget(QLabel("OY:"))
        coord_layout.addWidget(self.y_input)

        # Создаем горизонтальный макет для угла и чекбокса
        angle_layout = QHBoxLayout()
        angle_layout.addWidget(QLabel("Угол:"))
        angle_layout.addWidget(self.angle_input)
        angle_layout.addWidget(self.ccw_checkbox)

        # Основной вертикальный макет
        layout = QVBoxLayout()
        layout.addLayout(coord_layout)  # Добавляем строку с координатами
        layout.addLayout(angle_layout)  # Добавляем строку с углом и чекбоксом
        layout.addWidget(self.apply_button)  # Кнопка применения
        layout.addWidget(self.error) #Текст ошибки
        layout.addWidget(self.rotation_widget)  # Виджет для отображения вращения

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def apply_rotation(self):
        #Применяем изменения при нажатии кнопки
        try:
            #Считываем координаты
            x = float(self.x_input.text())
            y = float(self.y_input.text())
            #Считываем угол
            angle = float(self.angle_input.text())
            #Инициализируем точку вращения
            self.rotation_widget.rotation_point = QPointF(x, y)
            #Считываем настройку вращения - по часовой или против
            self.rotation_widget.is_clockwise = not self.ccw_checkbox.isChecked()
            #Высчитываем конечный угол поворота
            if self.rotation_widget.is_clockwise:
                self.rotation_widget.angle += angle
            else:
                self.rotation_widget.angle -= angle
            self.rotation_widget.update()  # Перерисовываем виджет
        except ValueError:
            self.error.setText('Ошибка, некорректный ввод')