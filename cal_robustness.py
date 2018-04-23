#!/usr/local/bin/python3

import sys
from read_formula import *
from create_tree import*
from binary_tree import*

# Print out control
def print_out(value, flag, show):
	if not show: return
	else: 
		print("-"*50)
		if flag is "raw":
			print("The raw formula is:\n", value[0])
			print("The State(s) is(are):\n", value[1])
		elif flag is "list":
			print("The formula list is:\n", value)
		elif flag is "compress_list":
			print("The compressed formula is:\n", value)
		elif flag is "tree_formula":
			print("The tree formula is:")
			print_tree(value)
			print("")
		elif flag is "tree_structure":
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


# If the user does not provide any filename, then execute
# "example_formula.txt" and "example_state.txt" by default.

# If the user provides too many arguments, exit the program.
# If the user specifies the filename, use the that filename.

# The program will first read the formula and state file, then print out the raw formula
# and state. Unnecessary space and '\n' will be deleted afterward. A list is created from
# the input string and printed out. A compressed list is then used to build the tree and 
# show to the end-user. 

class Robustness:
	def __init__(self, argv, option):
		self.option = option
		if len(argv) == 1:
			self.formula_filename = "example_formula.txt"
			self.state_filename   = "example_state.txt"
		elif len(argv) == 2:
			self.formula_filename = argv[1]
			self.state_filename   = "example_state.txt"
		elif len(argv) == 3:
			self.formula_filename = argv[1]
			self.state_filename   = argv[2]
		else:
			sys.exit("\033[1;31;47m Error: Too many input arguments! \033[0m")

	def BiTree(self):
		formula_str = read_file(self.formula_filename)
		STATE = read_state(self.state_filename)
		print_out([formula_str, STATE], "raw", self.option.SHOW_RAW)

		formula_str = preprocess(formula_str)
		stat(formula_str, STATE, self.option.SHOW_STAT)

		index = 0
		formula_list = list()
		while index < len(formula_str):
			index, formula_list = get_formula(index, formula_str, formula_list, STATE)
		print_out(formula_list, "list", self.option.SHOW_LIST)

		formula_list = compress_list(formula_list)
		print_out(formula_list, "compress_list", self.option.SHOW_COMP_LIST)

		self.tree = get_tree(formula_list)
		# self.tree = auto_timebound(self.tree, self.tree.cargo['Bound'])

		print_out(self.tree, "tree_formula", self.option.SHOW_TREE_FORM)
		print_out(self.tree, "tree_structure", self.option.SHOW_TREE_STRUC)



	def Eval(self,system,interval=[]):
		tree = self.tree
		if tree is None: return 0

		if tree.cargo['Value'] == "ev":
			left = tree.cargo['Bound']
			#left = left.cargo
			self.tree = tree.right
			interval_ev_t = np.array([left[0], left[1]])
			value,interval_ev = self.Eval(system,interval_ev_t)
			value = np.max(value)
			return value, interval_ev

		elif tree.cargo['Value'] == "alw":
			left = tree.cargo['Bound']
			#left = left.cargo
			self.tree = tree.right
			interval_alw_t = np.array([left[0], left[1]])
			value, interval_alw = self.Eval(system, interval_alw_t)
			value = np.max(value)
			return value, interval_alw

		elif tree.cargo['Value'] == "not":
			left = tree.cargo['Bound']  # is none for not operator
			self.tree = tree.right
			interval_not_t = interval
			value, interval_not = self.Eval(system, interval_not_t)
			return -value, interval_not


		elif tree.cargo['Value'] == "and":
			self.tree = tree.left
			robust_left,interval_left_t = self.Eval(system,interval)
			self.tree = tree.right
			robust_right, interval_right_t = self.Eval(system,interval)
			robust_left = np.min(robust_left)
			robust_right = np.min(robust_right)
			value = min(robust_left,robust_right)
			interval_left = min(interval_left_t[0],interval_right_t[0])
			interval_right = min(interval_left_t[1], interval_right_t[1])
			interval_and = np.array([interval_left, interval_right])
			return value, interval_and

		elif tree.cargo['Value'] == "or":
			self.tree = tree.left
			robust_left, interval_left_t = self.Eval(system,interval)
			self.tree = tree.right
			robust_right, interval_right_t = self.Eval(system,interval)
			robust_left = np.max(robust_left)
			robust_right = np.max(robust_right)
			value = max(robust_left,robust_right)
			interval_left = min(interval_left_t[0],interval_right_t[0])
			interval_right = min(interval_left_t[1], interval_right_t[1])
			interval_and = np.array([interval_left, interval_right])
			return value, interval_and

		elif tree.cargo['Value'] == "until":
			#left = tree.left
			#right_right = tree.right.right
			right_left = tree.cargo['Bound']
			self.tree = tree.left
			value_left, interval_left = self.Eval(system,interval)
			if len(system.time) > 1:
			   delta_t = system.time[1] - system.time[0]
			value = np.empty([1])
			for index in range(1,len(interval_left)):
				self.tree = tree.left
				interval_1 = np.array([interval[0],interval[0] + index*delta_t])
				value_left, interval_1 = self.Eval(system, interval_1)
				value_1 = np.amin(value_left, axis=0)
				print(type(value_1))
				start_time = interval_left[0] + (index-1)*delta_t+ right_left[0]
				interval_un =  np.array([start_time, start_time + right_left[1]])
				self.tree = tree.right
				value_2_a, interval_un = self.Eval(system, interval_un)
				value_2 = np.amin(value_2_a,axis=0)
				print(type(value_2))
				print(type(value))
				value_t =min(value_1,value_2)
				value = np.append(value, value_t)

			value = np.max(value)
			return value, interval_left

		elif tree.cargo['Value'][1] == "<" or  tree.cargo['Value'][1] == "<=":
			 pi = tree.cargo['Value'][2]
			# pi = convert_to_float(pi)
			 ind = system.name.index(tree.cargo['Value'][0])
			 signal = system.signal[ind]
			 time  =  system.time
			 start_time = interval[0]
			 end_time =  interval[1]
			 if end_time > np.max(time):
				 end_time = np.max(time)

			 if start_time < np.min(time):
				 start_time = np.min(time)
			 id_start = (np.abs(time - start_time)).argmin()
			 id_end  = (np.abs(time - end_time)).argmin()
			 value = pi - signal[id_start:id_end]
			 return value, interval

		elif tree.cargo['Value'][1] == ">=" or tree.cargo['Value'][1] == ">":
			pi = tree.cargo['Value'][2]
			ind = system.name.index(tree.cargo['Value'][0])
			signal = system.signal[ind]
			time = system.time
			start_time = interval[0]
			end_time = interval[1]
			if end_time > np.max(time):
				end_time = np.max(time)

			if start_time < np.min(time):
				 start_time = np.min(time)

			id_start = (np.abs(time - start_time)).argmin()
			id_end = (np.abs(time - end_time)).argmin()
			value = pi - signal[id_start:id_end]
			return value, interval

# Robustness calculation
class STL_Sys:
    def __init__(self,name,signal,time):
        self.name=name
        self.signal=signal
        self.time=time












