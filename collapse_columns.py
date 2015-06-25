#!/usr/bin/env python2.7

"""
Merges adjacent columns in a pairwise manner:
e.g. T T C T A G C G becomes TT CT AG CG
"""

import fileinput

for line in fileinput.input():
	line = line.split()
	
