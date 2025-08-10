from PySide6.QtWidgets import QGraphicsScene,QGraphicsView
from PySide6.QtGui import QPainter

class Editor(QGraphicsView):
    def __init__(self):
        super().__init__()  
        self.scene = QGraphicsScene()
        self.setScene(self.scene) 
        self.scene.setSceneRect(0, 0, 800, 600)
        self.setRenderHint(QPainter.Antialiasing)
        