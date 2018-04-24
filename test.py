#!/usr/local/bin/python3

from time import time
from cal_robustness import *
# import numpy as np

# Print-out control panel
class OPTION:
	SHOW_RAW        = True
	SHOW_LIST       = True
	SHOW_COMP_LIST  = True
	SHOW_TREE_FORM  = False
	SHOW_TREE_STRUC = True
	SHOW_STAT       = True
	SHOW_ROBUST		= True

def run_program():
	# Count time
	START_TIME = time()
	# Read formula and state
	Robust = Robustness(sys.argv, OPTION())
	# Create tree
	Robust.BiTree()
	# Create trajectory
	time1 = np.linspace(0,10,1001)
	signal = np.array([np.sin(2*np.pi*time1) + np.cos(3*np.pi*time1)])
	name = ['x1']
	system = STL_Sys(name,signal,time1)
	# Calculate robustness
	Robust.Eval_Robust(system)
	print("\n<Elapsed Time = %.6f" %(time()-START_TIME), "s>")	

if __name__ == '__main__':
	run_program()
