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

parser = argparse.ArgumentParser(description="Sample N lines or groups in a file. \
								If no arguments given, it will return 1 percent of \
								lines.")
parser.add_argument("--input", type=argparse.FileType("r"), default = "-", help = \
					"Input file. Can also take input from pipe.")

parser.add_argument("-p","--percent", help="P percent lines to sample in the file, \
					may not be used with -n", type=int, default = 1)
parser.add_argument("-n","--number", help="N number of lines to sample in the file, \
					may not be used with -p", type=int)
parser.add_argument("-head","--header", help="How many header lines to return",
					type=int)
parser.add_argument("-g", "--group", help="Return random lines in groups. Useful \
					for when lines are grouped sequentially, e.g. fastq files",
					type=int)
								
args = parser.parse_args()

P = args.percent
N = args.number
file = args.input
header_lines = args.header
group_size = args.group

# function to print or not print a line randomly
def returnLine(line, P):
	if random.randrange(0,100) < P:
		print line[:-1]
		return
	else:
		return

# function to batch lines together in n groups
def grouper(g, iterable, fillvalue=None):
	args = [iter(iterable)] * g
	return itertools.izip_longest(fillvalue=fillvalue, *args)





# if user asks for N lines to be returned:
if args.number:
	line_storage = list()
	line_num = 0
	# header is present
	if args.header >=1:
		# lines are grouped
		if group_size:
			pass #fill in later
		# lines are not grouped
		else:
			pass #fill in later
	# no header
	else:
		# lines are grouped
		if group_size:
			for line in grouper(group_size, file):
				if line_num < N:
					line_storage.append(line)
				else:
					j = random.randint(0,line_num)
					if j < N:
						line_storage[j] = line
					else:
						pass
				line_num += 1
			for line in line_storage:
				print ''.join(line)[:-1]

		# lines are not grouped
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


# if user asks for P percent lines to be returned:
else:
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
						if random.randrange(0,100) < P:
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
					returnLine(line, P)
	
	# no header present
	else:
		if group_size:						#if grouping is specified
			for line in grouper(group_size, file):
				if random.randrange(0,100) < P:
					print ''.join(line)[:-1]
				else:
					continue
		else:							#grouping is not specified
			for line in file:
				returnLine(line, P)
	










