from PySide6.QtWidgets import QGraphicsItem,QGraphicsPathItem
from PySide6.QtCore import QRectF, Qt, QPointF,  QPoint
from PySide6.QtGui import QBrush, QPen, QColor, QPainterPath, QCursor, QPainter
from core.pins.pins import BasicPin, PinType, PinDirection

class BasicPinItem(QGraphicsItem):
    def __init__(self, pin: BasicPin, x=0, y=0):
        super().__init__()
        self.pin = pin
        self.setPos(x, y)
        self.radius = 8

    def boundingRect(self) -> QRectF:
        return QRectF(0, 0, self.radius * 2, self.radius * 2)

    def paint(self, painter, option, widget=None):

        colors = {
            PinType.ANYTHING: QColor(200, 200, 200),
            PinType.DATAFRAME: QColor(83, 155, 224),
            PinType.STRING: QColor(224, 155, 83),
            PinType.INT: QColor(155, 224, 83),
        }
        color = colors.get(self.pin.pin_type, QColor(150, 150, 150))

        painter.setBrush(QBrush(color))
        painter.setPen(QPen(Qt.black, 1))

        # Разная форма для разных типов
        if self.pin.pin_type == PinType.STRING:
            # треугольник
            points = [
                (self.radius, 0),
                (0, self.radius * 2),
                (self.radius * 2, self.radius * 2)
            ]
            painter.drawPolygon(*[QPointF(x, y) for x, y in points])
        else:
            # круг
            painter.drawEllipse(0, 0, self.radius * 2, self.radius * 2)
    
    def mousePressEvent(self, event):
        scene_pos = self.mapToScene(self.radius, self.radius)
        
        self.temp_line = QGraphicsPathItem()
        self.temp_line.setPen(QPen(Qt.black, 2))
        path = QPainterPath()
        path.moveTo(scene_pos)
        path.lineTo(scene_pos)  
        self.temp_line.setPath(path)
        self.scene().addItem(self.temp_line)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.temp_line:
            start_pos = self.mapToScene(self.radius, self.radius)
            end_pos = event.scenePos()
            path = QPainterPath()
            path.moveTo(start_pos)
            path.lineTo(end_pos)
            self.temp_line.setPath(path)

    def mouseReleaseEvent(self, event):
        if self.temp_line:
            self.scene().removeItem(self.temp_line)
            self.temp_line = None