#!/usr/bin/env python

"""
Checks for characters in fasta files
by line that contain non  A C G T N 
characters and returns the line number and line

2015-07-30
"""

import fileinput

allowed = set('agctn')

def check(seq):
	return set(seq) <= allowed 

line_num = 1
for line in fileinput.input():
	seq = line.lower()
	if seq[0] == ">":
		line_num += 1
		continue
	else:
		if check(seq[:-1]) is True:
			line_num += 1
			continue
		if check(seq[:-1]) is False:
			print line_num, line[:-1]
			line_num += 1
		
				
