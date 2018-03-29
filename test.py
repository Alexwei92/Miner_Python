#!/usr/local/bin/python3

import sys
from cal_robustness import Robustness

# Print-out control panel
class OPTION:
	SHOW_RAW        = True
	SHOW_PREP       = False
	SHOW_LIST       = True
	SHOW_COMP_LIST  = False
	SHOW_TREE_FORM  = False
	SHOW_TREE_STRUC = True
	SHOW_STAT		= True


if __name__ == '__main__':
	tree = Robustness(sys.argv, OPTION()).BiTree()
	Robustness.Eval(tree)