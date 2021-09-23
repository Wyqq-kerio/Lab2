# Edit the file content

def edit_text(lines):
    # Skip the part that doesn't count
    notes_flag = False 
    for line in lines[::-1]:
        lines_index = lines.index(line)
        # Convert strings to lists 
        line_str = list(line)
        # Delete header files
        if '#include' in line or '#define' in line or '#undef' in line \
                or '#ifdef' in line or '#ifndef' in line or '#endif' in line:
            del lines[lines_index]
        # Remove single-line comments
        elif '//' in line:
            del lines[lines_index]          
        # Remove multi-line comments
        elif '*/' in line:
            notes_flag = True
            del lines[lines_index]
        elif '/*' in line:
            notes_flag = False
            del lines[lines_index]
        elif notes_flag is True:
            del lines[lines_index]
        # Convert the list back to a string
        line = ''.join(line_str)

    # Standardize the processing of articles  

    for line in lines:
        lines_index = lines.index(line)
        # Convert strings to lists 
        line_list = list(line)

        # Add a space at the end of each line before a newline
        line_list[len(line_list) - 1] = ' '
        line_list.append('\n')

        # Convert the list back to a string
        line = ''.join(line_list)
        # update
        lines[lines_index] = line

    for line in lines:
        lines_index = lines.index(line)
        # Convert strings to lists 
        line_list = list(line)

        # Add space after '{'
        index = line.find('{')
        if index >= 0:
            line_list.insert(index + 1, ' ')
            line_list.insert(index, ' ')
            
            # Convert the list back to a string
            line = ''.join(line_list)
            # update
            lines[lines_index] = line


    for line in lines:
        lines_index = lines.index(line)
        # Convert strings to lists 
        line_str = list(line)
        
        # Delete the content between the quotes
        if '"' in line:
            i = line.find('"')
            j = line.rfind('"')
            line_str[i:j + 1] = " "
        # Change other punctuation marks to Spaces
        for unit in line_str:
            str_index = line_str.index(unit)
            if unit == '?' or unit == '!' or unit == ',' or unit == '.' or unit == '(' or unit == ')' or unit == '[' or unit == ']' or unit == ':' or unit == ';':
                line_str[str_index] = ' '


        # Convert the list back to a string
        line = ''.join(line_str)
        # update
        lines[lines_index] = line
        
    return lines
