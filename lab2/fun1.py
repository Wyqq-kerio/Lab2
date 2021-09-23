import string
import string
import os
import re

# Count the "keyword" statistics
def count_keyword(lines):
    keywords = [
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
    'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
    ]

    total_num = 0
    for line in lines:
        str = line.split(' ')
        for i in str:
            for j in keywords:
                if i == j:
                    total_num += 1
                    break
                
    print('total num: %d' % total_num)
    return total_num