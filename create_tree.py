#!/usr/local/bin/python3
from read_formula import *
from binary_tree import Tree
import math
import numpy as np


# Get the position of open & close parenthesis
def index_parenthesis(formula_list):
	index_open = list()
	index_close = list()
	for index in range(len(formula_list)):
		if formula_list[index] == '(':
			index_open.append(index)
		elif formula_list[index] == ')':
			index_close.append(index)
	return index_open, index_close

# Compress the list
def compress_list(formula_list):
	index_open, index_close = index_parenthesis(formula_list)
	while index_open:
		start_position = index_open[-1]
		end_position = index_close[list(np.array(index_close) > start_position).index(True)]
		temp = formula_list[start_position+1:end_position]
		del formula_list[start_position:end_position+1]
		formula_list.insert(start_position,temp)
		index_open, index_close = index_parenthesis(formula_list)
	return formula_list

# Convert the content in bracket
def convert_bracket(str):
	try:
		str = str.replace('inf_','inf')
		str = str.split(",")
		print(str)
		if len(str) != 2:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of bracket! \033[0m")	
		return [float(str[0]), float(str[1])]
	except: 
		sys.exit("\033[1;31;47m SyntaxError: Unknown Error in bracket! \033[0m")

# Create the tree
def get_tree(formula_list):
	if 'ev_' in formula_list:
		if len(formula_list) != 3:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of ev_! \033[0m")
		else:
			left = Tree(convert_bracket(formula_list[1][1:-1]),None,None)
			right = get_tree(formula_list[2])
			return Tree("ev",left,right)
	elif 'alw_' in formula_list:
		if len(formula_list) != 3:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of alw_! \033[0m")
		else:
			left = Tree(convert_bracket(formula_list[1][1:-1]),None,None)
			right = get_tree(formula_list[2])
			return Tree("alw",left,right)
	elif 'not_' in formula_list:
		if len(formula_list) != 2:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of not_! \033[0m")
		else:
			left = None
			right = get_tree(formula_list[1])
			return Tree("not",left,right)
	elif 'and_' in formula_list:
		if len(formula_list) != 3:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of and_! \033[0m")
		else:
			left = get_tree(formula_list[0])
			right = get_tree(formula_list[2])
			return Tree("and",left,right)
	elif 'or_' in formula_list:
		if len(formula_list) != 3:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of or_! \033[0m")
		else:
			left = get_tree(formula_list[0])
			right = get_tree(formula_list[2])
			return Tree("or",left,right)
	elif 'until_' in formula_list:
		if len(formula_list) != 3:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of until_! \033[0m")
		else:
			left = get_tree(formula_list[0])
			right = get_tree(formula_list[2])
			return Tree("until",left,right)
	else:
		return Tree(formula_list, None, None)
