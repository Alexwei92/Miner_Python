#!/usr/local/bin/python3
import sys

STATE          = ['x1','x2']
OPERATOR       = ['ev_','alw_','not_','until_','and_','or_']
SPECIAL_CHAR_1 = ['[',']','(',')','<','>']
SPECIAL_CHAR_2 = ['>=','<=']

# Read the formula file.
# If the file does not exist, exit the program.
# If the file is empty, exit the program.
def read_file(filename = "example_formula.txt"):
    try:
        f = open(filename, 'rt')
        str = f.read()
        f.close()
        if not str:
            sys.exit("\033[1;31;47m Error: The file is empty! \033[0m")
    except FileNotFoundError as err:
        sys.exit(err)
    else:
        return str

# Delete all the space and newline characters.
def prep(str):
    str = str.strip('\n')
    str = str.replace(' ','')
    return str

# Show the statistics of the formula.
# If show = True, print out the result.
def stat(str, show = True):
    number_ev                = str.count('ev_')
    number_alw               = str.count('alw_')
    number_not               = str.count('not_')
    number_until             = str.count('until_')
    number_and               = str.count('and_')
    number_or                = str.count('or_')
    number_open_parenthesis  = str.count('(')
    number_close_parenthesis = str.count(')')
    number_open_bracket      = str.count('[')
    number_close_bracket     = str.count(']')

    if show:
        print("-"*50)
        print("Number of Eventually:        ", number_ev)
        print("Number of Always:            ", number_alw)
        print("Number of Negation:          ", number_not)
        print("Number of Until:             ", number_until)
        print("Number of Conjunction:       ", number_and)
        print("Number of Disjunction:       ", number_or)
        print("Number of Open parenthesis:  ", number_open_parenthesis)
        print("Number of Close parenthesis: ", number_close_parenthesis)
        print("Number of Open bracket:      ", number_open_bracket)
        print("Number of Close bracket:     ", number_close_bracket)

    if number_open_parenthesis != number_close_parenthesis:
        sys.exit("\033[1;31;47m Error: The number of parenthesis does not match! \033[0m")
    if number_open_bracket != number_close_bracket:
        sys.exit("\033[1;31;47m Error: The number of bracket does not match! \033[0m")
        
# Read the character
def get_formula(index, str, formula):
    if str[index:index+3] == 'ev_':
        formula.append('ev_')
        index = index + 3
        if str[index] != '[':
            sys.exit("\033[1;31;47m SyntaxError: Missing open bracket! \033[0m")
    elif str[index:index+4] == 'alw_':
        formula.append('alw_')
        index = index + 4
        if str[index] != '[':
            sys.exit("\033[1;31;47m SyntaxError: Missing open bracket! \033[0m")
    elif str[index:index+4] == 'not_':
        formula.append('not_')
        index = index + 4
        if str[index] != '(':
            sys.exit("\033[1;31;47m SyntaxError: Missing open parenthesis! \033[0m")
    elif str[index:index+6] == 'until_':
        formula.append('until_')
        index = index + 6
        if str[index] != '(':
            sys.exit("\033[1;31;47m SyntaxError: Missing open parenthesis! \033[0m")
    elif str[index:index+4] == 'and_':
        formula.append('and_')
        index = index + 4
        if str[index] != '(':
            sys.exit("\033[1;31;47m SyntaxError: Missing open parenthesis! \033[0m")
    elif str[index:index+3] == 'or_':
        formula.append('or_')
        index = index + 3
        if str[index] != '(':
            sys.exit("\033[1;31;47m SyntaxError: Missing open parenthesis! \033[0m")
    elif str[index:index+2] == 'x1':
        formula.append('x1')
        index = index + 2
    elif str[index:index+2] == 'x2':
        formula.append('x2')
        index = index + 2
    elif str[index:index+2] in SPECIAL_CHAR_2:
        formula.append(str[index:index+2])
        index = index + 2
    elif str[index] in SPECIAL_CHAR_1:
        if str[index] == '(' and index == len(str)-1:
            sys.exit("\033[1;31;47m SyntaxError: Improper use of parenthesis! \033[0m")
        elif str[index] == '[' and index == len(str)-1:
            sys.exit("\033[1;31;47m SyntaxError: Improper use of bracket! \033[0m")
        elif str[index] == '[':
            index_end = index + 1
            while str[index_end] != ']':
                if str[index_end] == '[':
                    sys.exit("\033[1;31;47m SyntaxError: Improper use of bracket! \033[0m")
                else: index_end += 1
            if index_end - index < 4 or str[index:index_end+1].count(',') != 1:
                sys.exit("\033[1;31;47m SyntaxError: Improper use of bracket! \033[0m")
            else:
                formula.append(str[index:index_end+1])
                index =  index_end + 1
        else:
            formula.append(str[index])
            index += 1
    else:
        index_end = index
        while str[index_end].isdigit() or str[index_end] in ['.', '+', '-', '*', '/']:
            index_end += 1
        formula.append(str[index:index_end])
        index = index_end
    return index, formula  

# Write to a file
def write_file(filename = "example_formula_output.txt", formula = None):
    try:
        f = open(filename, 'wt')
        str = f.write(str(formula))
        f.close()
    except:
        sys.exit("\033[1;31;47m Error: Unable to write to the file! \033[0m")
