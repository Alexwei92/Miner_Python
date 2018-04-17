#!/usr/local/bin/python3

import sys
from time import time
from cal_robustness import*
import numpy as np
import matplotlib.pyplot as plt
# Print-out control panel
class OPTION:
	def __init__(self):
		self.SHOW_RAW        = True
		self.SHOW_PREP       = False
		self.SHOW_LIST       = True
		self.SHOW_COMP_LIST  = False
		self.SHOW_TREE_FORM  = False
		self.SHOW_TREE_STRUC = True
		self.SHOW_STAT		= True


if __name__ == '__main__':

	Robust = Robustness(sys.argv, OPTION())
	Robust.BiTree()

	signal = np.random.randn(2,100)
	time = np.linspace(0,10,100)
	name = ['x1', 'x2']
	system = STL_Sys(name,signal,time)

	value, interval = Robust.Eval(system)
	print(value)

	plt.plot(time,signal[0],'r--',time,signal[1], 'g-')
	plt.show()
