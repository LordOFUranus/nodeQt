import pandas as pd

from base_node import BaseNode

class ReadExcelNode(BaseNode):
    def __init__(self, input_data=None):
        super().__init__(input_data)
        self.file_path = None  

    def set_path(self, path: str):
        self.file_path = path

    def process(self):
        path_to_use = self.input or self.file_path
        if not path_to_use:
            raise ValueError("Нет входных данных или пути к файлу")
            
        self.output = pd.read_excel(path_to_use)

        if self.next_node:
            self.next_node.input = self.output
            return self.next_node.process()
        
        return self.output