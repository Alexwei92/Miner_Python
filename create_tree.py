#!/usr/local/bin/python3

def get_formula(formula_list, expected):
    if formula_list[0] == expected:
        del formula_list[0]
        return True
    return False

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

def get_eventually(formula_list):
	

from read_formula import *
from binary_tree import *

data = read_file()
print("The original formula:\n", data)
data = prep(data)
print("\nAfter Preprocessing:\n", data)
stat(data, show = False)

formula_list = list()
index = 0
while index < len(data):
    index, formula_list = get_formula(index,data,formula_list)
print("\nThe formula list is:\n",formula_list)











