#!/usr/local/bin/python3

from read_formula import *
from binary_tree import Tree
from fractions import Fraction
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

# Compress the list with sublist
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

# Check if is a fraction expression
def get_fraction(str):
	try:
		if str.count('/') > 0:
			return Fraction(str)
		else: return str
	except:
		sys.exit("\033[1;31;47m Error: Unknown error when converting the fraction! \033[0m")

# Convert the content in bracket
def convert_bracket(str):
	try:
		str = str.replace('inf_','inf')
		str = str.split(",")
		if len(str) != 2:
			sys.exit("\033[1;31;47m SyntaxError: Missing content in bracket! \033[0m")	
		elif float(get_fraction(str[0])) > float(get_fraction(str[1])):
			sys.exit("\033[1;31;47m SyntaxError: In [a, b], b should be larger than a! \033[0m")
		return [float(get_fraction(str[0])), float(get_fraction(str[1]))]
	except: 
		sys.exit("\033[1;31;47m SyntaxError: Unknown Error in bracket! \033[0m")

# Convert the predicate formula
# !!!Need to add in the future!!!
def convert_predict(formula_list):
	new_list = list()
	for x in formula_list:
		if x.count('/') > 0 or x.count('.') > 0 or x.isdigit():
			new_list.append(float(get_fraction(x)))
		else: new_list.append(x)
	return new_list

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
		if len(formula_list) != 4:
			sys.exit("\033[1;31;47m SyntaxError: Improper use of until_! \033[0m")
		else:
			left = get_tree(formula_list[0])		
			right = get_tree(formula_list[3])
			cargo = "until"
			cargo.append(formula_list[2])
			return Tree(cargo,left,right)
	else:
		return Tree(convert_predict(formula_list), None, None)
