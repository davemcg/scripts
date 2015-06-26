#!/usr/bin/env python2.7

"""
Merges adjacent columns in a pairwise manner:
e.g. T T C T A G C G becomes TT CT AG CG
"""

import argparse 

parser = argparse.ArgumentParser(description="Merge together adjacent columns in a pairwise manner. For example T T C T A G C G becomes TT CT AG CG. \
								User can specify which column to begin on with -c.") 

parser.add_argument("--input", type=argparse.FileType("r"), default = "-", help = \
					"Input file. Can also take input from pipe.")
parser.add_argument("-c","--column", type=int, default=1, help = "Which column to \
					begin on.")

args = parser.parse_args()


for line in args.input:
	# split on space
	line = line.split()
	length = len(line)
	col_to_start = args.column 
	output = []
	# add non-merge beginning columns to list
	for i in range(0,col_to_start-1,1):
		output.append(line[i])
	# add merged (pasted) columns to list
	for i in range(col_to_start-1,length-1,2):
		output.append(line[i]+line[i+1])
	print '\t'.join(output)	
