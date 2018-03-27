#!/usr/local/bin/python3

import sys
from create_tree import *
from binary_tree import *
from other import print_out

# If the user does not provide the filename,
# then execute "example_formula.txt" by default.

# If the user provides too many arguments, exit the program.
# If the user specifies the filename, use the provided filename.

# The program will first print out the raw formula,
# then delete unnecessary space and '\n', print out the preprocessed formula

SHOW_RAW        = True
SHOW_PREP       = False
SHOW_LIST       = True
SHOW_COMP_LIST  = False
SHOW_TREE_FORM  = False
SHOW_TREE_STRUC = True
SHOW_STAT		= True


if __name__ == '__main__':
	if len(sys.argv) == 1:
		filename = "example_formula.txt"
	elif len(sys.argv) > 2:
		sys.exit("\033[1;31;47m Error: Too many inputs! \033[0m")
	else:
		filename = sys.argv[1]
		formula_str = read_file(filename)
		print_out(formula_str, "raw", SHOW_RAW)
	
	formula_str = prep(formula_str)
	print_out(formula_str, "prep", SHOW_PREP)
	stat(formula_str, SHOW_STAT)

	# Initialization
	index = 0
	formula_list = list()
	while index < len(formula_str):
		index, formula_list = get_formula(index, formula_str, formula_list)
	print_out(formula_list, "list", SHOW_LIST)

	formula_list = compress_list(formula_list)
	print_out(formula_list, "compress_list", SHOW_COMP_LIST)

	tree = get_tree(formula_list)
	print_out(tree, "tree_formula", SHOW_TREE_FORM)
	print_out(tree, "tree_structure", SHOW_TREE_STRUC)
	