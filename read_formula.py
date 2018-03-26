#!/usr/local/bin/python3

from binary_tree import *
from enum import Enum

STATE          = ['x1','x2']
OPERATOR       = ['ev_','alw_','not_','until_','and_','or_']
SPECIAL_CHAR_1 = ['[',']','(',')','<','>',',']
SPECIAL_CHAR_2 = ['>=','<=']

# read the formula file
def read_file(filename = "example_formula.txt"):
    try:
        f = open(filename, 'rt')
        str = f.read()
        f.close()
        return str
    except FileNotFoundError as err:
        print(err)

def prep(str):
    str = str.strip('\n')
    str = str.replace(' ','')
    return str

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
        print("-"*30)
        print("Number of Eventually: ", number_ev)
        print("Number of Always: ", number_alw)
        print("Number of Negation: ", number_not)
        print("Number of Until: ", number_until)
        print("Number of Conjunction: ", number_and)
        print("Number of Disjunction: ", number_or)
        print("Number of Open parenthesis", number_open_parenthesis)
        print("Number of Close parenthesis", number_close_parenthesis)
        print("Number of Open bracket", number_open_bracket)
        print("Number of Close bracket", number_close_bracket)
        print("-"*30)

    if number_open_parenthesis != number_close_parenthesis:
        raise ValueError("The number of parenthesis do not match!")
    if number_open_bracket != number_close_bracket:
        raise ValueError("The number of bracket do not match!")
        
# read the character
def get_formula(index, str, formula):
    if str[index:index+3] == 'ev_':
        formula.append('ev_')
        index = index + 3
        if str[index] != '[':
            raise ValueError("Missing open bracket")
    elif str[index:index+4] == 'alw_':
        formula.append('alw_')
        index = index + 4
        if str[index] != '[':
            raise ValueError("Missing open bracket")
    elif str[index:index+4] == 'not_':
        formula.append('not_')
        index = index + 4
    elif str[index:index+6] == 'until_':
        formula.append('until_')
        index = index + 6
    elif str[index:index+4] == 'and_':
        formula.append('and_')
        index = index + 4
    elif str[index:index+3] == 'or_':
        formula.append('or_')
        index = index + 3
    elif str[index:index+4] == 'inf_':
        formula.append('inf_')
        index = index + 4
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
        if str[index] == '[':
            index_end = index
            while str[index_end] != ']':
                index_end = index_end + 1
            formula.append(str[index:index_end+1])
            index = index_end + 1
        else:
            formula.append(str[index])
            index = index + 1
    else:
        index_end = index
        while str[index_end].isdigit() or str[index_end] == '.':
            index_end = index_end + 1
        formula.append(str[index:index_end])
        index = index_end
    return index, formula  

# f2 = open('example_formula_output.txt', 'wt')
# str = f2.write(str(formula))
# f2.close()
