#!/usr/local/Anaconda/envs/py3.4.3/bin/python


import sys


def process(samtools_input):
	line = samtools_input
	reads = line[4]
	reads = reads.lower()
	a = str(reads.count('a'))
	c = str(reads.count('c'))
	g = str(reads.count('g'))
	t = str(reads.count('t'))
	ref = str(reads.count('.') + reads.count(','))
	counts = '\t'.join([a,c,g,t,ref])
	return(counts)

for line in sys.stdin:
	line = line.split()
	print("chr","position","Reference","ReadCoverage","A","C","G","T","REF")
	print(line[0],line[1],line[2],line[3],process(line))
