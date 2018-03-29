#!/usr/local/bin/python3

import sys

#from binary_tree import *
from other import*
import numpy as np
# system has the data structure as follows:


def get_value(system, tree=[],interval=[]):
    if tree is None: return 0

    if tree.cargo == "ev":
        left = tree.left
        left = left.cargo
        right = tree.right
        interval_ev_t = np.array([left[0], left[1]])
        value,interval_ev = get_value(system,right,interval_ev_t)
        value = np.max(value)
        return value, interval_ev

    elif tree.cargo == "alw":
        left = tree.left
        left = left.cargo
        right = tree.right
        interval_alw_t = np.array([left[0], left[1]])
        value, interval_alw = get_value(system, right, interval_alw_t)
        value = np.max(value)
        return value, interval_alw

    elif tree.cargo == "not":
        left = tree.left   # is none for not operator
        right = tree.right
        interval_not_t = interval
        value, interval_not = get_value(system, right, interval_not_t)
        return -value, interval_not


    elif tree.cargo == "and":
        left = tree.left
        right = tree.right
        robust_left,interval_left_t = get_value(system,left,interval)
        robust_right, interval_right_t = get_value(system, right,interval)
        robust_left = np.min(robust_left)
        robust_right = np.min(robust_right)
        value = min(robust_left,robust_right)
        interval_left = min(interval_left_t[0],interval_right_t[0])
        interval_right = min(interval_left_t[1], interval_right_t[1])
        interval_and = np.array([interval_left, interval_right])
        return value, interval_and

    elif tree.cargo == "or":
        left = tree.left
        right = tree.right
        robust_left, interval_left_t = get_value(system, left,interval)
        robust_right, interval_right_t = get_value(system, right,interval)
        robust_left = np.max(robust_left)
        robust_right = np.max(robust_right)
        value = max(robust_left,robust_right)
        interval_left = min(interval_left_t[0],interval_right_t[0])
        interval_right = min(interval_left_t[1], interval_right_t[1])
        interval_and = np.array([interval_left, interval_right])
        return value, interval_and

    elif tree.cargo == "until":
        left = tree.left
        right = tree.right
        t_left = min(interval)
        t_right = max(interval)

    elif tree.cargo[1] == "<" or  tree.cargo[1] == "<=":
         pi = tree.cargo[2]
         pi = convert_to_float(pi)
         ind = system.name.index(tree.cargo[0])
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
         value = np.empty([1])
         for index in range(id_start,id_end):
             value_t = pi-signal[index]
             value = np.append(value, value_t)
         return value, interval

    elif tree.cargo[1] == ">=" or tree.cargo[1] == ">":
        pi = tree.cargo[2]
        pi = convert_to_float(pi)
        ind = system.name.index(tree.cargo[0])
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

        value = np.empty([1])
        for index in range(id_start, id_end):
            value_t = pi - signal[index]
            value = np.append(value, value_t)
        return value, interval






















