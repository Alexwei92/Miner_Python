#!/usr/local/bin/python3

<<<<<<< HEAD
=======
from time import time
>>>>>>> 51f0175ae500f7eae006d199ac21be3e2f48bbe4
from cal_robustness import *
# import numpy as np

# Print-out control panel
class OPTION:
<<<<<<< HEAD
	SHOW_RAW        = False
	SHOW_LIST       = False
	SHOW_COMP_LIST  = False
	SHOW_TREE_FORM  = False
	SHOW_TREE_STRUC = True
	SHOW_STAT       = False
	SHOW_ROBUST		= True
	SHOW_TIME		= False

def run_program():
	# Read formula and state
=======
	SHOW_RAW        = True
	SHOW_LIST       = True
	SHOW_COMP_LIST  = True
	SHOW_TREE_FORM  = False
	SHOW_TREE_STRUC = True
	SHOW_STAT       = True


if __name__ == '__main__':
	START_TIME = time()
>>>>>>> 51f0175ae500f7eae006d199ac21be3e2f48bbe4
	Robust = Robustness(sys.argv, OPTION())
	# Create tree
	Robust.BiTree()
<<<<<<< HEAD
	# Create trajectory
	time = np.linspace(0,10,1001)
	signal = np.array([np.sin(2*np.pi*time) + np.cos(3*np.pi*time)])
	name = ['x1']
	system = STL_Sys(name,signal,time)
	# Calculate robustness
	Robust.Eval_Robust(system)
	

if __name__ == '__main__':
	run_program()
=======

	# signal = np.random.randn(2,100)
	# time = np.linspace(0,10,100)
	# name = ['x1', 'x2']
	# system = STL_Sys(name,signal,time)

	# value, interval = Robust.Eval(system)
	# print('\n',value)

	print("<Elapsed Time = ", time()-START_TIME, "s >")
>>>>>>> 51f0175ae500f7eae006d199ac21be3e2f48bbe4
