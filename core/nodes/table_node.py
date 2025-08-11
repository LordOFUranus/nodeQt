from base_node import BaseNode

import pandas as pd

class TableNode(BaseNode):
    def __init__(self, input_data=None):
        super().__init__(input_data)
    
    def process(self):
        self.output = self.input
        if not isinstance(self.output, pd.DataFrame):
            print('Не DataFrame')
            return
        print(self.output)
        if self.next_node:
            self.next_node.input = self.output
            return self.next_node.process()
       
        return self.output
