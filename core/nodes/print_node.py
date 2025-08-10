from base_node import BaseNode

class PrintNode(BaseNode):
    def process(self):
        print(f"PrintNode: {self.input}")
        self.output = self.input
        if self.next_node:
            self.next_node.input = self.output
            return self.next_node.process()
        return self.output