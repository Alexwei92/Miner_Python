#!/usr/local/bin/python3

from enum import Enum

# Define the operators
class Unary_op(Enum):
	NEXT       = 1
	ALWAYS     = 2
	EVENTUALLY = 3
	NOT	   = 4

class Binary_op(Enum):
	IMPLICATION = 1
	AND         = 2
	OR          = 3
	UNTIL       = 4
	THEN        = 5
