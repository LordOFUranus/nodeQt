from base_node import BaseNode
from print_node import PrintNode
from add_text_node import AddTextNode
from read_excel_node import ReadExcelNode
from table_node import TableNode
import pandas as pd



# bn = BaseNode("123")
# pn = PrintNode("434")

# bn.process()
# pn.process()

# bn1 = BaseNode('34435')
# pn1 = PrintNode()

# bn1.next_node = pn1
# bn1.process()


# bn2 = BaseNode("Hello")
# pn2 = PrintNode()
# atn2 = AddTextNode("World")
# pn21 = PrintNode()

# bn2.next_node = pn2
# pn2.next_node = atn2
# atn2.next_node = pn21

# bn2.process()

df = ReadExcelNode()
df.set_path('C:/Users/Zhanibek/Downloads/Акт сверки взаимных расчетов KCC и KAZ GREEN ENER за период с 01.01.2025 по 31.07.xlsx')
tn = TableNode()
df.next_node = tn
tn2 = TableNode()
tn.next_node = tn2
df.process()
