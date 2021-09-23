import string
import os
import re

# Count the number of "if, else if, else" structures
def count_if_elseif_else(lines):
    # the number of structures
    if_elif_num = []
    if_elif_total = 0
    # Number of "else"
    flag_else = 0 
    # Number of total "elif"
    flag_elif = 0  
    # Number of "elif" in each group of structures
    temp_elif = 0 
    for line in lines:
        # Convert the list to a string
        str = ''.join(line)

        if str.find("else if") != -1:
            if_elif_num.append('1')
        elif str.find("if") != -1:
            if_elif_num.append('2')
        elif str.find("else") != -1:
            if_elif_num.append('3')
        else:
            continue

    # Reverse counting
    if_elif_num.reverse() 
    for i in range(len(if_elif_num)):
        if if_elif_num[i] == '1':
            flag_elif += 1
            temp_elif += 1
        if if_elif_num[i] == '2':
            if flag_else >= 1 and flag_elif >= 1:
                if_elif_total += 1
                flag_elif -= temp_elif
            else:
                flag_else -= 1
                flag_elif -= 0
        if if_elif_num[i] == '3':
            flag_else += 1

    print("if-elseif-else num: ", if_elif_total)
    return if_elif_total
