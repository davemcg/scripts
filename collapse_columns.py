#!/usr/bin/env python2.7

"""
Merges adjacent columns in a pairwise manner:
e.g. T T C T A G C G becomes TT CT AG CG
"""

import fileinput

for line in fileinput.input():
	# split on space
	line = line.split()
	length = len(line)
	col_to_start = 5 
	output = []
	# add non-merge beginning columns to list
	for i in range(0,col_to_start-1,1):
		output.append(line[i])
	# add merged (pasted) columns to list
	for i in range(col_to_start-1,length-1,2):
		output.append(line[i]+line[i+1])
	print '\t'.join(output)	
