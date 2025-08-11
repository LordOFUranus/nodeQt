from ui.nodes.base_node_ui import BaseNodeItem
from PySide6.QtWidgets import QGraphicsObject, QGraphicsItem, QLabel, QFileDialog, QLineEdit, QPushButton, QGraphicsProxyWidget
from PySide6.QtCore import QRectF, Qt, QEvent
from PySide6.QtGui import QBrush, QPen, QColor, QFont
from ..pins.pins_ui import BasicPinItem, BasicPin
from core.pins.pins import PinDirection, PinType


class ExcelReadNodeItem(BaseNodeItem):
    def __init__(self):
        super().__init__()
        self.rect = QRectF(0, 0, 200, 100)

        self.title = "Чтение Excel"
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

        self.inputs.clear()
        self.outputs.clear()

        self.add_default_pin()

        #прокси виджет, графические объекты не поддерживают виджеты и надо чередовать через создание виджета и закрепления за прокси
        #полноценный виджет - переменная его прокси, которая через setwidget(наша нода, и сам виджет, который добавить)

        self.path_edit = QLineEdit()
        self.path_edit.setFixedHeight(25)
        self.path_edit.setFixedWidth(140)
        self.path_edit.setPlaceholderText("Выберите файл Excel...")

        proxy_edit = QGraphicsProxyWidget(self)
        proxy_edit.setWidget(self.path_edit)
        proxy_edit.setPos(10, 35)

        self.btn_select = QPushButton("...")
        self.btn_select.setFixedSize(30, 25)
        self.btn_select.clicked.connect(self.select_file)

        proxy_btn = QGraphicsProxyWidget(self)
        proxy_btn.setWidget(self.btn_select)
        proxy_btn.setPos(150, 35)



    def add_default_pin(self):
        #у excel ноды только выходящий пин
        
        pin_out = BasicPinItem(
            BasicPin("out1", PinType.DATAFRAME, PinDirection.OUTPUT, self),
            x=self.rect.width() - 10,
            y=self.rect.height() / 2,
        )

        pin_out.setParentItem(self)

        self.outputs.append(pin_out)


    def paint(self, painter, option, widget):

        body_color = QColor(100, 250, 130, 100)
        painter.setBrush(QBrush(body_color))
        painter.setPen(QPen(QColor("black"), 2))
        painter.drawRect(self.rect)
        
        title_height = 25
        title_color = QColor(60, 120, 200)
        painter.setBrush(QBrush(title_color))
        painter.setPen(QPen(QColor("black"), 1))
        painter.drawRect(0, 0, self.rect.width(), title_height)
        painter.setPen(QColor("white"))
        painter.setFont(QFont("Arial", 10))
        painter.drawText(
            QRectF(0, 0, self.rect.width(), title_height), Qt.AlignCenter, self.title
        )

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(None, "Выбрать Excel файл", "", "Excel Files (*.xlsx *.xls)")
        if path:
            self.path_edit.setText(path)