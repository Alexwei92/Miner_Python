#!/usr/local/bin/python3

from cal_robustness import *
# import numpy as np

# Print-out control panel
class OPTION:
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
	Robust = Robustness(sys.argv, OPTION())
	# Create tree
	Robust.BiTree()
<<<<<<< HEAD
	time1 = np.linspace(0,10,1001)
	signal = np.array([time1])
=======
	# Create trajectory
	time = np.linspace(0,10,1001)
	signal = np.array([np.sin(2*np.pi*time) + np.cos(3*np.pi*time)])
>>>>>>> f90a3260a16a5286eeea7d5e8bdee54c668e7491
	name = ['x1']
	system = STL_Sys(name,signal,time)
	# Calculate robustness
	Robust.Eval_Robust(system)
	

if __name__ == '__main__':
	run_program()
