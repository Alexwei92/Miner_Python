#!/usr/local/bin/python3

from formula import *
from read_formula import *

#A simple example, "9*(11+5)*7"
token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
print("The original formula is: ", *token_list[0:-1], sep='')
tree = get_product(token_list)
print("The tree structure looks like:")
print_tree_indented(tree)
