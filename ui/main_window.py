from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtGui import QAction
from .editor import Editor
from .nodes.base_node_ui import BaseNodeItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Нодовый редактор Excel")
        self.setGeometry(100, 100, 800, 600)

        self.editor = Editor()
        self.setCentralWidget(self.editor)

        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        new_action = QAction("&New", self)
        file_menu.addAction(new_action)
   
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        button_add_basic_node = QAction('Добавить Ноду', self)
        button_add_basic_node.triggered.connect(self.create_basic_node)
        toolbar.addAction(button_add_basic_node)

    def create_basic_node(self):
        node = BaseNodeItem()
        self.editor.scene.addItem(node) 
        node.setPos(100, 100)