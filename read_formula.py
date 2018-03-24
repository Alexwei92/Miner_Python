#!/usr/local/bin/python3

from binary_tree import *
from enum import Enum

state = ['x1', 'x2']


def check_is_state(str):
    str.find(state)
    


# def get_formula(formula_list, expected):
#     if formula_list[0] == expected:
#         del formula_list[0]
#         return True
#     return False

# def get_number(formula_list):
#     if get_formula(formula_list, "("):
#         x = get_sum(formula_list)
#         if not get_formula(formula_list, ")"):
#             raise ValueError("Missing close parenthesis")
#         return x
#     else:
#         x = formula_list[0]
#         if type(x) != type(0): return None
#         del formula_list[0]
#         return Tree(x, None, None)

# def get_product(formula_list):
#     a = get_number(formula_list)
#     if get_formula(formula_list, "*"):
#         b = get_product(formula_list)
#         return Tree("*", a, b)
#     return a

# def get_sum(formula_list):
#     a = get_product(formula_list)
#     if get_formula(formula_list, "+"):
#         b = get_sum(formula_list)
#         return Tree("+", a, b)
#     return a
f = open('example_formula.txt', 'rt')
data = f.read()
f.close()
print("The original formula:\n", data)
#delete all the space
data = data.replace(' ','')
print("After Step 1:\n", data)

number_ev    = data.count("ev_")
number_alw   = data.count("alw_")
number_not   = data.count("not")
number_until = data.count("until_")
number_and   = data.count("and")
number_or    = data.count("or")
print("-"*30)
print("number of eventually: ", number_ev)
print("number of always: ", number_alw)
print("number of negation: ", number_not)
print("number of until: ", number_until)
print("number of conjunction: ", number_and)
print("number of disjunction: ", number_or)
print("-"*30)

formula = list()
index = 0
while index < len(data):
    if data[index:index+3] == 'ev_':
        formula.append('ev_')
        index = index + 3
    elif data[index:index+4] == 'alw_':
        formula.append('alw_')
        index = index + 4
    elif data[index:index+3] == 'not':
        formula.append('not')
        index = index + 3
    elif data[index:index+6] == 'until_':
        formula.append('until_')
        index = index + 6
    elif data[index:index+3] == 'and':
        formula.append('and')
        index = index + 3
    elif data[index:index+2] == 'or':
        formula.append('or')
        index = index + 2
    elif data[index:index+3] == 'inf':
        formula.append('inf')
        index = index + 3
    # elif (data[index]).isdigit() or data[index] == '.':
    #     print("Yes")
    #     index = index + 1
    else:
        formula.append(data[index])
        index = index + 1
print(formula)

print(state[0])
print(type(state[0]))


