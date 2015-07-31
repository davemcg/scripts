#!/usr/bin/env python3

from Bio import SeqIO
import sys

fasta = open(sys.argv[1])

for i in SeqIO.parse(fasta,'fasta'):
	print(i.id, len(i.seq),sep="\t")

