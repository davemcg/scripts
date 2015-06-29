#!/usr/bin/env python2.7

"""
Takes in a file and outputs user-specified lines
"""

import argparse

parser = argparse.ArgumentParser(description="Output user-specified lines from a file.")

parser.add_argument("--input", type=argparse.FileType("r"), default = "-", help = \
					"Input file. Can also take input from pipe.")
parser.add_argument("-l","--list", type=argparse.FileType("r"), help = \
					"File with lines (\n separated) to be returned.")

args = parser.parse_args()

lines_to_return = []
for line in args.list:
	lines_to_return.append(line[:-1])

current_line = 1
for line in args.input:
	if str(current_line) in lines_to_return:
		print line[:-1]
		current_line += 1
	else:
		current_line += 1
		continue
