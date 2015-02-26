#!/usr/bin/env python2.7

"""
Randomly samples text files and returns N% of the lines

Can be set to always return the header (of x lines)

Can also be set to pick N% of y set of lines
	e.g.	fastq files have four lines per set of sequence
			so you would want to pick N% of the quartet

Random sampling could be used to select exactly N lines 
but this is dangerous because this requires the entire
file to be held in memory for the sort. Hence the simpler
approach, which is to return (with exceptions above)
N% of any given line

"""

import argparse, random, itertools

parser = argparse.ArgumentParser(description="Sample N percent of lines or groups \
								in a file")
parser.add_argument("N",help="N percent lines to sample in the file", 
					type=int)
parser.add_argument("-head","--header", help="How many header lines to return",
					type=int)
parser.add_argument("-g", "--group", help="Return random lines in groups. Useful \
					for when sets of lines are important, e.g. fastq files",
					type=int)
parser.add_argument("--input", type=argparse.FileType("r"), default = "-")
								
args = parser.parse_args()

N=args.N
file = args.input
header_lines = args.header
group_size = args.group

# function to print or not print a line randomly
def returnN(line, N):
	if random.randrange(0,100) < N:
		print line[:-1]
		return
	else:
		return

# function to batch lines together in n groups
def grouper(n, iterable, fillvalue=None):
	args = [iter(iterable)] * n
	return itertools.izip_longest(fillvalue=fillvalue, *args)


# if there is a header
if args.header >= 1:
	# lines are being grouped
	if group_size:									
		line_count = 0	
		for line in file:	
			# print header
			if line_count < header_lines:		
				print line[:-1]
				line_count += 1
			# after printing header, then print the randomly 
			# selected groups
			else:
				for line in grouper(group_size, file):
					if random.randrange(0,100) < N:
						print ''.join(line)[:-1]
					else:
						continue		
	# grouping is not specified
	else:
		line_count = 0	
		for line in file:
			# again, print header
			if line_count <= header_lines:
				print line[:-1]
				line_count += 1
			# after header, print random lines
			else:
				returnN(line, N)

# no header present
else:
	if group_size:						#if grouping is specified
		for line in grouper(group_size, file):
			if random.randrange(0,100) < N:
				print ''.join(line)[:-1]
			else:
				continue
	else:							#grouping is not specified
		for line in file:
			returnN(line, N)


	
