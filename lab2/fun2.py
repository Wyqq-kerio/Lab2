import string
import os
import re

# Count the number of the number of "switch case" structures
# output the number of "case" corresponding to each group
def count_switch(lines):
    # Number of elements in the stack
    stack_num = 0
    # Number of switch
    switch_num = 0
    # Number of case
    case_num = []
    # The number of cases in each group of structures
    temp_num = 0
    # Used to determine whether it is in the same structure
    flag = False   
    
    for line in lines:
        lines_index = lines.index(line)
        str = line.split(' ')
        if 'switch' in str:
            switch_num += 1
            temp_num = 0
            flag = True          
        if 'case' in str:
            temp_num += 1
        if '{' in str and flag is True:
            stack_num += 1
        if '}' in str and flag is True:
            stack_num -= 1
            flag = False
            if stack_num == 0:
                case_num.append(temp_num)

    print('switch num: %d' % switch_num)
    return switch_num, case_num