#!/usr/local/bin/python3

import sys
from cal_robustness import Robustness
from other import*
import numpy as np
from Eval_Formula import *
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
	Robust = Robustness(sys.argv, OPTION()).BiTree()
	print(type(Robust))
	signal = np.random.randn(2,100)
	time = np.linspace(0,10,100)
	name = ['x1', 'x2']
	system = STL_Sys(name,signal,time)

#	value,intervl= get_value(system, Robust.tree)
#	print(value)