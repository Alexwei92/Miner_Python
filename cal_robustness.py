#!/usr/local/bin/python3

import sys
from create_tree import *
from binary_tree import *

# Print out control
def print_out(value, flag, show):
	if not show: return
	else: 
		print("-"*50)
		if flag == "raw":
			print("The raw formula is:\n", value)
		elif flag == "prep":
			print("The preprocessed formula is:\n", value)
		elif flag == "list":
			print("The formula list is:\n", value)
		elif flag == "compress_list":
			print("The compressed formula is:\n", value)
		elif flag == "tree_formula":
			print("The tree formula is:")
			print_tree(value)
			print("")
		elif flag == "tree_structure":
			print("The tree structure looks like:\n")
			print_tree_indented(value)
		else:
			sys.exit("\033[1;31;47m\tError: Unrecognized flag to print_out!\t\033[0m")

# Write to a file
def write_file(filename = "example_output.txt", Output = None):
    try:
        f = open(filename, 'wt')
        str = f.write(str(Output))
        f.close()
    except:
        sys.exit("\033[1;31;47m Error: Unable to write to '%s'. \033[0m" %filename)


# If the user does not provide any filename, then execute
# "example_formula.txt" and "example_state.txt" by default.

# If the user provides too many arguments, exit the program.
# If the user specifies the filename, use the that filename.

# The program will first read the formula and state file, then print out the raw formula
# and state. Unnecessary space and '\n' will be deleted afterward. A list is created from
# the input string and printed out. A compressed list is then used to build the tree and 
# show to the end-user. 

class Robustness:
	def __init__(self, argv, option):
		self.option = option
		if len(argv) == 1:
			self.formula_filename = "example_formula.txt"
			self.state_filename   = "example_state.txt"
		elif len(argv) == 2:
			self.formula_filename = argv[1]
			self.state_filename   = "example_state.txt"
		elif len(argv) == 3:
			self.formula_filename = argv[1]
			self.state_filename   = argv[2]
		else:
			sys.exit("\033[1;31;47m Error: Too many input arguments! \033[0m")

	def BiTree(self):
		formula_str = read_file(self.formula_filename)
		STATE = read_state(self.state_filename)
		print_out(formula_str, "raw", self.option.SHOW_RAW)
		print("The State(s) is(are):\n", STATE)

		formula_str = prep(formula_str)
		print_out(formula_str, "prep", self.option.SHOW_PREP)
		stat(formula_str, STATE, self.option.SHOW_STAT)

		index = 0
		formula_list = list()
		while index < len(formula_str):
			index, formula_list = get_formula(index, formula_str, formula_list, STATE)
		print_out(formula_list, "list", self.option.SHOW_LIST)

		formula_list = compress_list(formula_list)
		print_out(formula_list, "compress_list", self.option.SHOW_COMP_LIST)

		self.tree = get_tree(formula_list)
		print_out(self.tree, "tree_formula", self.option.SHOW_TREE_FORM)
		print_out(self.tree, "tree_structure", self.option.SHOW_TREE_STRUC)

	def Eval(self):
		return True
