#!/usr/bin/env python2.7

"""
Because unix cut won't process huge numbers of columns
I have to write my own version
"""

import argparse

parser = argparse.ArgumentParser(description="Output user-specified columns from a file.")

parser.add_argument("--input", type=argparse.FileType("r"), default = "-", help = \ 
                    "Input file. Can also take input from pipe.")
parser.add_argument("-l","--list", type=argparse.FileType("r"), help = \ 
                    "File with columns (\n separated) to be returned.")
parser.add_argument("-f", type = str, help = "unix cut like column input \
					e.g. -f 1,5,8,15")
parser.add_argument("-d","--delim", type = str, default = "\t", help = "Delimiter. \
					Default is \t")

args = parser.parse_args()

if args.list:
	columns = []
	for line in args.list:
		columns.append(line[:-1])

else:
	columns = args.f.split(",")

print columns
