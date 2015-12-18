#!/usr/local/Anaconda/envs/py3.4.3/bin/python


import sys
import subprocess

def run_samtools(bamfile, region):
	samtools_input = 'samtools mpileup -r' + region + 
		"-f /fdb/GATK_resource_bundle/hg19-2.8/ucsc.hg19.fasta" + 
		bamfile 

	samtools_view = (subprocess.check_output(samtools_input, shell=True)).decode('utf-8')
	return(samtools_view)

def process(samtools_input):
	"""
	Takes input from samtools mpileup (requires reference) and counts
	numbers of A, C, G, T in pileup. 
	
	Currently only tested when fed a single line 
	"""
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
	#	print("chr","position","Reference","ReadCoverage","A","C","G","T")
		samtools_return = run_samtools(sys.argv[1],sys.argv[2])
		print(line[0],line[1],line[2],line[3],process(samtools_return))

main()
