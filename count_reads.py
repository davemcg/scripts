#!/usr/local/Anaconda/envs/py3.4.3/bin/python


import sys


def process(samtools_input):
	line = samtools_input
	reads = line[4]
	reads = reads.lower()
	ref = line[2]

	if reference == 'a':
		a = str(reads.count('.') + reads.count(','))
	else:
		a = str(reads.count('a'))
	if reference == 'c':
		c = str(reads.count('.') + reads.count(','))
	else:
		c = str(reads.count('c'))
	if reference == 'g':
		g = str(reads.count('.') + reads.count(','))
	else:
		g = str(reads.count('g'))
	if reference == 't':
		t = str(reads.count('.') + reads.count(','))
	else:
		t = str(reads.count('t'))
	counts = '\t'.join([a,c,g,t])
	return(counts)

def main():
	for line in sys.stdin:
		line = line.split()
		print("chr","position","Reference","ReadCoverage","A","C","G","T")
		print(line[0],line[1],line[2],line[3],process(line))

main()
