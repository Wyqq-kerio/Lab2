from edit import edit_text
from fun1 import count_keyword
from fun2 import count_switch
from fun3 import count_if_else
from fun4 import count_if_elseif_else

#input the path of the code file
file_path = input()
# input completion level
level = int(input())

# Read the file
with open(file_path) as file_object:
    lines = file_object.readlines()

# Process file contents
lines = edit_text(lines)

if level >= 1:
    total_num = count_keyword(lines)
if level >= 2:
    switch_num, case_num = count_switch(lines)
    print('case num: ', end='')
    for num in case_num:
        print(num, end=' ')
if level >= 3:
    if_else_num = count_if_else(lines)
if level >= 4:
    if_elif_total=count_if_elseif_else(lines)
