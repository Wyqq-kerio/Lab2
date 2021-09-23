import string
import os
import re

# Count the number of "if else" structures
def count_if_else(lines):
    # Number of structures
    if_else_num = []
    if_else_total=0
    for line in lines:
        line1=line.strip().split('\n')
        # Convert the list to a string
        line2=''.join(line1)

        # remove "else if" interference
        if line2.find("else if")!=-1:
            if_else_num.append('0')
        # mark "if" and "else" with '1' and '2' respectively 
        elif line2.find("if")!=-1:
            if_else_num.append('1')
        elif line2.find("else")!=-1:
            if_else_num.append('2')
        else:
            continue

    for i in range(len(if_else_num)):
        if if_else_num[i]=='1' and if_else_num[i+1]=='2':
            if_else_total+=1
            
    print("\nif-else num: ",if_else_total)
    return  if_else_total



