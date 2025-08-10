from base_node import BaseNode


class AddTextNode(BaseNode):
    def __init__(self, add_str=None, input_data=None):
        super().__init__(input_data)
        self.add_str = add_str

    def process(self):
        if self.add_str is not None:
            self.output = (self.input or "") + self.add_str
        else:
            self.output = self.input

        if self.next_node:
            self.next_node.input = self.output
            return self.next_node.process()
        return self.output
