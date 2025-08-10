from enum import Enum, auto

class PinDirection(Enum):
    INPUT = auto()
    OUTPUT = auto()

class PinType(Enum):
    DATAFRAME = auto()
    STRING = auto()
    INT = auto()
    ANYTHING = auto()

class BasicPin:
    def __init__(self, name: str, pin_type: PinType, direction: PinDirection, node):
        self.name = name
        self.pin_type = pin_type
        self.direction = direction
        self.node = node 
        self.connected_pins = []  

    def connect(self, other_pin):
        """Подключить к другому пину"""
        if other_pin not in self.connected_pins:
            self.connected_pins.append(other_pin)
            other_pin.connected_pins.append(self)

    def disconnect(self, other_pin):
        """Отключить"""
        if other_pin in self.connected_pins:
            self.connected_pins.remove(other_pin)
            other_pin.connected_pins.remove(self)

    def is_connected(self) -> bool:
        return len(self.connected_pins) > 0
