#!/usr/local/bin/python3

import sys

#from binary_tree import *

# system has the data structure as follows:

class STL_Sys:
    def __init__(self,name,signal,time):
        self.name=name
        self.signal=signal
        self.time=time


def get_value(system, tree=[]):
    if tree is None: return 0

    if tree.cargo == "ev":
        left=tree.left
        right=tree.right
    elif tree.cargo == "alw":
        left=tree.left
        right=tree.right
    elif tree.cargo == "not":
        left=tree.left
        right=tree.right
    elif tree.cargo == "and":
        left=tree.left
        right=tree.right
    elif tree.cargo == "or":
        left=tree.left
        right=tree.right
    elif tree.cargo == "until":
        left=tree.left
        right=tree.right
    else:
        sys.exit("\033[1;31;47m SyntaxError: Improper use of or_! \033[0m")






