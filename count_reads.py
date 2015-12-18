#!/usr/local/Anaconda/envs/py3.4.3/bin/python


import sys


def process(samtools_input):
	line = samtools_input
	reads = line[4]
	reads = reads.lower()
	reference = line[2].lower()

	if reference == 'a':
		a = str(reads.count('.') + reads.count(','))
		c = str(reads.count('c'))
		g = str(reads.count('g'))
		t = str(reads.count('t'))
	elif reference == 'c':
		a = str(reads.count('a'))
		c = str(reads.count('.') + reads.count(','))
		g = str(reads.count('g'))
		t = str(reads.count('t'))
	elif reference == 'g':
		a = str(reads.count('a'))
		c = str(reads.count('c'))
		g = str(reads.count('.') + reads.count(','))
		t = str(reads.count('t'))
	elif reference == 't':
		a = str(reads.count('a'))
		c = str(reads.count('c'))
		g = str(reads.count('g'))
		t = str(reads.count('.') + reads.count(','))
	else:
		print("Reference is",reference,"!")
	counts = '\t'.join([a,c,g,t])
	return(counts)

def main():
	for line in sys.stdin:
		line = line.split()
		print("chr","position","Reference","ReadCoverage","A","C","G","T")
		print(line[0],line[1],line[2],line[3],process(line))

main()
