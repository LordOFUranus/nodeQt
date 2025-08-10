class BaseNode:
    def __init__(self, input_data=None):
        self.input = input_data
        self.output = None
        self.next_node = None

    def process(self):
        self.output = self.input
        if self.next_node:
            self.next_node.input = self.output 
            return self.next_node.process()
        return self.output
