#!/usr/local/bin/python3

import sys
from binary_tree import print_tree, print_tree_indented

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