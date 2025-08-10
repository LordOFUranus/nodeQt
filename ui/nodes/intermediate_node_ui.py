from ui.nodes.base_node_ui import BaseNodeItem
from PySide6.QtWidgets import QGraphicsObject, QGraphicsItem, QLabel
from PySide6.QtCore import QRectF, Qt, QEvent
from PySide6.QtGui import QBrush, QPen, QColor, QFont
from ..pins.pins_ui import BasicPinItem, BasicPin
from core.pins.pins import PinDirection, PinType


class IntermediateNodeItem(BaseNodeItem):
    def __init__(self):
        super().__init__()
        self.rect = QRectF(0, 0, 100, 100)

        self.title = "Промежуточный Узел"
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

        self.inputs.clear()
        self.outputs.clear()

        self.add_default_pin()
    def add_default_pin(self):
        pin_in = BasicPinItem(
            BasicPin("in1", PinType.ANYTHING, PinDirection.INPUT, self),
            x=self.rect.width()-110,
            y=self.rect.height() / 2,
        )
        pin_out = BasicPinItem(
            BasicPin("out1", PinType.ANYTHING, PinDirection.OUTPUT, self),
            x=self.rect.width() - 10,
            y=self.rect.height() / 2,
        )

        pin_in.setParentItem(self)
        pin_out.setParentItem(self)

        self.inputs.append(pin_in)
        self.outputs.append(pin_out)

    def paint(self, painter, option, widget):

        body_color = QColor(200, 190, 190, 150)
        painter.setBrush(QBrush(body_color))
        painter.setPen(QPen(QColor("black"), 2))
        painter.drawRect(self.rect)

        title_height = 25
        title_color = QColor(160, 150, 150)
        painter.setBrush(QBrush(title_color))
        painter.setPen(QPen(QColor("black"), 1))
        painter.drawRect(0, 0, self.rect.width(), title_height)
        painter.setPen(QColor("white"))
        painter.setFont(QFont("Arial", 10))
        painter.drawText(
            QRectF(0, 0, self.rect.width(), title_height), Qt.AlignCenter, self.title
        )
