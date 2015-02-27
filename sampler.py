#!/usr/bin/env python2.7

"""
Randomly samples text files and returns P% of the lines

Can be set to always return the header (of x lines)

Can also be set to pick P% of y set of lines
	e.g.	fastq files have four lines per set of sequence
			so you would want to pick N% of the quartet

Also can be run to select N total lines. Modifications 
for header and groups the same as above. 
"""

import argparse, random, itertools

parser = argparse.ArgumentParser(description="Randomly sample lines (or groups of lines) \
								in a file and print to stdout. Can either return percent \
								of lines or N total lines. Input can be given either \
 								with --input or via pipe. If no arguments (besides \
								input) are given, it will return 1 percent of lines.")
parser.add_argument("--input", type=argparse.FileType("r"), default = "-", help = \
					"Input file. Can also take input from pipe.")
parser.add_argument("-p","--percent", help= "P percent lines to sample in the file, \
					may not be used with -n.", type=int, default = 1)
parser.add_argument("-n","--number", help="N number of lines to sample in the file, \
					may not be used with -p.", type=int)
parser.add_argument("-head","--header", help="How many header lines to return.",
					type=int)
parser.add_argument("-g", "--group", help="Return random lines in groups. Useful \
					for when lines are grouped sequentially, e.g. fastq files.",
					type=int)
parser.add_argument("-r", "--random", help="Give seed for random.seed. Use when you \
					want to get consistent results. Very useful for when you are \
					sampling paired fasta/q files. Default is system time.", 
					default=None)
								
args = parser.parse_args()

P = args.percent
N = args.number
file = args.input
header_lines = args.header
group_size = args.group

# set seed
random.seed(args.random)

# function to print or not print a line randomly
def returnLine(line, P):
	if random.randrange(0,100) < P:
		print line[:-1]
		return
	else:
		return

# function to batch lines together in n groups
def grouper(group_size, iterable, fillvalue=None):
	args = [iter(iterable)] * group_size
	return itertools.izip_longest(fillvalue=fillvalue, *args)

# returns N selected groups with Algorithm R
def groupReservoir(group_size, file):
	storage = list()
	line_num = 0
	for line in grouper(group_size, file):
		if line_num < N:
			storage.append(line)
		else:
			j = random.randint(0,line_num)
			if j < N:
				storage[j] = line
		line_num += 1
	return storage

# print header, if present
def headerP():
	line_num = 0
	for line in file:
		if line_num < header_lines:
			print line[:-1]
			line_num += 1
		else:
			break

# if user asks for N lines to be returned:
if args.number:
	line_storage = list()
	line_num = 0
	# header is present
	if args.header >=1:
		headerP()
		# lines are grouped
		if group_size:
			for line in groupReservoir(group_size, 
				itertools.islice(file,header_lines-1,None)):
				print ''.join(line)[:-1]
		# lines are not grouped. Algorithm R
		else:
			for line in itertools.islice(file,header_lines-1,None):
				if line_num < N:
					line_storage.append(line[:-1])
				else:
					j = random.randint(0,line_num)
					if j < N:
						line_storage[j] = line[:-1]
					else:
						pass
				line_num += 1
			for line in line_storage:
				print line 
	# no header, lines are grouped
	elif group_size:
		for line in groupReservoir(group_size, file):
			print ''.join(line)[:-1]
	# no header, lines are not grouped. Algorithm R
	else:
		for line in file:
			if line_num < N:
				line_storage.append(line[:-1])
			else:
				j = random.randint(0,line_num)
				if j < N:
					line_storage[j] = line[:-1]
				else:
					pass
			line_num += 1
		for line in line_storage:
			print line 


# if user asks for P percent lines to be returned and there is a header
elif args.header >=1:
	headerP()
	# lines are being grouped
	if group_size:									
		for line in grouper(group_size, 
			itertools.islice(file,header_lines-1,None)):
			if random.randrange(0,100) < P:
				print ''.join(line)[:-1]
	# grouping is not specified
	else:
		for line in itertools.islice(file,header_lines-1,None):
			returnLine(line, P)
	
# no header present, grouping
elif group_size:
	for line in grouper(group_size, file):
		if random.randrange(0,100) < P:
			print ''.join(line)[:-1]
# no header, no grouping
else:	
	for line in file:
		returnLine(line, P)
	

