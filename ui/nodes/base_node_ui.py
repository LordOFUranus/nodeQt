from PySide6.QtWidgets import QGraphicsObject, QGraphicsItem, QLabel
from PySide6.QtCore import QRectF, Qt, QEvent
from PySide6.QtGui import QBrush, QPen, QColor, QFont
from ..pins.pins_ui import BasicPinItem, BasicPin
from core.pins.pins import PinDirection, PinType
from core.nodes.base_node import BaseNode

class BaseNodeItem(QGraphicsObject):
    def __init__(self, logic_node = None):
        super().__init__()
        self.logic_node = logic_node
        
        self.rect = QRectF(0, 0, 200, 100)
        self.title = "Базовая Нода"
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

        self.inputs = []
        self.outputs = []

    def add_default_pin(self):
        # pin = BasicPinItem(
        #     BasicPin("out1", PinType.INT, PinDirection.OUTPUT, self),
        #     x=self.rect.width() - 20,
        #     y=50,
        # )
        # pin.setParentItem(self)
        # self.outputs.append(pin)
        # self.inputs.append(pin)
        pass
        
    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget):

        body_color = QColor(83, 155, 224, 100)
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

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.RightButton:
            self.deleteLater()
        super().mouseDoubleClickEvent(event)
