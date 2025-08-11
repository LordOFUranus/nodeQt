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
        return self.output
