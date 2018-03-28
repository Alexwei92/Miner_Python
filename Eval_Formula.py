#!/usr/local/bin/python3

import sys

#from binary_tree import *

# system has the data structure as follows:

class STL_Sys:
    def __init__(self,name,signal,time):
        self.name=name
        self.signal=signal
        self.time=time


def get_value(system, tree=[],interval=[]):
    if tree is None: return 0

    if tree.cargo == "ev":
        left = tree.left
        right = tree.right
        interval_ev_ = [left[0], left[1]]
        value,interval_ev = get_value(system,right,interval_ev_)
        return value, interval_ev

    elif tree.cargo == "alw":
        left = tree.left
        right = tree.right
        interval_alw_ = [left[0], left[1]]
        value, interval_alw = get_value(system, right, interval_alw_)
        return value, interval_alw

    elif tree.cargo == "not":
        left = tree.left   # is none for not operator
        right = tree.right
        interval_not_ = interval
        value, interval_not = - get_value(system, right, interval_not_)
        return value, interval_not

    elif tree.cargo == "and":
        left = tree.left
        right = tree.right
        robust_left,interval_left_ = get_value(system, left)
        robust_right, interval_right_ = get_value(system, right)
        value = min(robust_left,robust_right)
        interval_left = min(interval_left_[0],interval_right_[0])
        interval_right = min(interval_left_[1], interval_right_[1])
        interval_and = [interval_left, interval_right]
        return value, interval_and

    elif tree.cargo == "or":
        left = tree.left
        right = tree.right
        robust_left, interval_left_ = get_value(system, left)
        robust_right, interval_right_ = get_value(system, right)
        value = max(robust_left,robust_right)
        interval_left = min(interval_left_[0],interval_right_[0])
        interval_right = min(interval_left_[1], interval_right_[1])
        interval_and = [interval_left, interval_right]
        return value, interval_and

    elif tree.cargo == "until":
        left = tree.left
        right = tree.right

        
    else:
        sys.exit("\033[1;31;47m SyntaxError: Improper use of or_! \033[0m")






