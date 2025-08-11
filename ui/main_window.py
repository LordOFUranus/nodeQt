from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtGui import QAction
from .editor import Editor
from .nodes.base_node_ui import BaseNodeItem
from .nodes.intermediate_node_ui import IntermediateNodeItem
from .nodes.read_excel_node_ui import ExcelReadNodeItem

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
      
        button_add_basic_node = QAction('Добавить Базовую пустую Ноду', self)
        button_add_basic_node.triggered.connect(self.create_basic_node)

        button_add_intermediate_node = QAction('Добавить Промежуточный узел', self)
        button_add_intermediate_node.triggered.connect(self.create_intermediate_node)

        button_add_excel_read_node = QAction('Добавить Считыватель Excel', self)
        button_add_excel_read_node.triggered.connect(self.create_excel_read_node)
        
        button_add_table_node = QAction('Показать Таблицу',self)

        toolbar.addAction(button_add_basic_node)
        toolbar.addAction(button_add_intermediate_node)
        toolbar.addAction(button_add_excel_read_node)
        toolbar.addAction(button_add_table_node)
        toolbar.addSeparator()
        
        button_run = QAction('Запустить', self)

        toolbar.addAction(button_run)
    def create_basic_node(self):
        node = BaseNodeItem()
        self.editor.scene.addItem(node) 
        node.setPos(100, 100)
    def create_intermediate_node(self):
        node = IntermediateNodeItem()
        self.editor.scene.addItem(node) 
        node.setPos(100, 100)
    def create_excel_read_node(self):
        node = ExcelReadNodeItem()
        self.editor.scene.addItem(node) 
        node.setPos(100, 100)