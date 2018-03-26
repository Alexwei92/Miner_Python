#!/usr/local/bin/python3

from read_formula import *
from binary_tree import *
import numpy as np


def index_parenthesis(formula_list):
	index = 0
	index_open = list()
	index_close = list()
	for index in range(len(formula_list)):
		if formula_list[index] == '(':
			index_open.append(index)
		if formula_list[index] == ')':
			index_close.append(index)
	return index_open, index_close

def combine_list(formula_list):
	index_open, index_close = index_parenthesis(formula_list)
	while index_open:
		start_position = index_open[-1]
		end_position = index_close[list(np.array(index_close)>start_position).index(True)]
		temp = formula_list[start_position+1:end_position]
		del formula_list[start_position:end_position+1]
		formula_list.insert(start_position,temp)
		index_open, index_close = index_parenthesis(formula_list)
	return formula_list

def get_tree(formula_list):
	if 'ev_' in formula_list:
		left = Tree(formula_list[1],None,None)
		right = get_tree(formula_list[2])
		return Tree("ev",left,right)
	elif 'alw_' in formula_list:
		left = Tree(formula_list[1],None,None)
		right = get_tree(formula_list[2])
		return Tree("alw",left,right)
	elif 'not_' in formula_list:
		left = None
		right = get_tree(formula_list[1])
		return Tree("not",left,right)
	elif 'and_' in formula_list:
		left = get_tree(formula_list[0])
		right = get_tree(formula_list[2])
		return Tree("and",left,right)
	elif 'or_' in formula_list:
		left = get_tree(formula_list[0])
		right = get_tree(formula_list[2])
		return Tree("or",left,right)
	elif 'until_' in formula_list:
		left = get_tree(formula_list[0])
		right = get_tree(formula_list[2])
		return Tree("until",left,right)
	else:
		return Tree(formula_list, None, None)


data = read_file()
print("The original formula:\n", data, "\n")
data = prep(data)
print("After Preprocessing:\n", data, "\n")
stat(data, show = True)

formula_list = list()
index = 0
while index < len(data):
	index, formula_list = get_formula(index, data, formula_list)

print("The formula list is:\n", formula_list, "\n")

formula_list = combine_list(formula_list)
print("The combined formula is:\n",formula_list,"\n")


tree = get_tree(formula_list)
print("The tree looks like:")
print_tree_indented(tree)
