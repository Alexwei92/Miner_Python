#!/usr/local/bin/python3

from binary_tree import *

def get_formula(formula_list, expected):
    if formula_list[0] == expected:
        del formula_list[0]
        return True
    return False

def get_number(formula_list):
    if get_formula(formula_list, "("):
        x = get_sum(formula_list)
        if not get_formula(formula_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = formula_list[0]
        if type(x) != type(0): return None
        del formula_list[0]
        return Tree(x, None, None)

def get_product(formula_list):
    a = get_number(formula_list)
    if get_formula(formula_list, "*"):
        b = get_product(formula_list)
        return Tree("*", a, b)
    return a

def get_sum(formula_list):
    a = get_product(formula_list)
    if get_formula(formula_list, "+"):
        b = get_sum(formula_list)
        return Tree("+", a, b)
    return a