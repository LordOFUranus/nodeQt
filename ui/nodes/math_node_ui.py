from ui.nodes.base_node_ui import BaseNodeItem
from PySide6.QtWidgets import QGraphicsObject, QGraphicsItem, QLabel
from PySide6.QtCore import QRectF, Qt, QEvent
from PySide6.QtGui import QBrush, QPen, QColor, QFont
from ..pins.pins_ui import BasicPinItem, BasicPin
from core.pins.pins import PinDirection, PinType

class MathNodeItem(BaseNodeItem):
    def __init__(self, logic_node=None):
        super().__init__(logic_node)
        