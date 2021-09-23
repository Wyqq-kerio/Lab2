import unittest
from edit import edit_text
from fun1 import count_keyword
from fun2 import count_switch
from fun3 import count_if_else
from fun4 import count_if_elseif_else

with open("code.txt") as file_object:
    read_lines = file_object.readlines()
lines = edit_text(read_lines)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        total_num = count_keyword(lines)
        self.assertEqual(total_num, 35)  # add assertion here

    def test_2(self):
        switch_num, case_num = count_switch(lines)
        self.assertEqual(switch_num, 2)  # add assertion here
        self.assertEqual(case_num, [3, 2])

    def test_3(self):
        if_else_total= count_if_else(lines)   
        self.assertEqual(if_else_total, 2)  # add assertion here

    def test_4(self):
        if_elif_total= count_if_elseif_else(lines)   
        self.assertEqual(if_elif_total, 2)  # add assertion here    


if __name__ == '__main__':
    unittest.main()
