#!/usr/local/bin/python3

import sys
from create_tree import *
from binary_tree import *
from other import print_out

# Print-out control panel
#########################
SHOW_RAW        = True
SHOW_PREP       = False
SHOW_LIST       = True
SHOW_COMP_LIST  = False
SHOW_TREE_FORM  = False
SHOW_TREE_STRUC = True
SHOW_STAT		= True
#########################

# If the user does not provide any filename, then execute
# "example_formula.txt" and "example_state.txt" by default.

# If the user provides too many arguments, exit the program.
# If the user specifies the filename, use the that filename.

# The program will first read the formula and state file, then print out the raw formula
# and state. Unnecessary space and '\n' will be deleted afterward. A list is created from
# the input string and printed out. A compressed list is then used to build the tree and 
# show to the end-user. 


if __name__ == '__main__':
	if len(sys.argv) == 1:
		formula_filename = "example_formula.txt"
		state_filename   = "example_state.txt"
	elif len(sys.argv) == 2:
		formula_filename = sys.argv[1]
		state_filename   = "example_state.txt"
	elif len(sys.argv) == 3:
		formula_filename = sys.argv[1]
		state_filename   = sys.argv[2]
	else:
		sys.exit("\033[1;31;47m Error: Too many inputs! \033[0m")
	formula_str = read_file(formula_filename)
	STATE = read_state(state_filename)
	print_out(formula_str, "raw", True)
	print("The State(s) is(are):\n", STATE)

	formula_str = prep(formula_str)
	print_out(formula_str, "prep", SHOW_PREP)
	stat(formula_str, STATE, SHOW_STAT)

	index = 0; formula_list = list()
	while index < len(formula_str):
		index, formula_list = get_formula(index, formula_str, formula_list, STATE)
	print_out(formula_list, "list", SHOW_LIST)

	formula_list = compress_list(formula_list)
	print_out(formula_list, "compress_list", SHOW_COMP_LIST)

	tree = get_tree(formula_list)
	print_out(tree, "tree_formula", SHOW_TREE_FORM)
	print_out(tree, "tree_structure", SHOW_TREE_STRUC)
