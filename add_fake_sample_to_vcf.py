#!/usr/local/bin/python3

"""
Adds fake sample (het 0/1) to vcf. 

If there's a hom_alt, then the fake sample is 0/0
"""

import sys

file_name = open(sys.argv[1])
sample_name = sys.argv[2]

for line in file_name:
	# reprints vcf header
	if line[0:2]=="##":
		print(line[:-1])
	# adds FORMAT and sample column 
	elif line[0]=="#":
		line = line.split()
		line.append("FORMAT")
		line.append(sample_name)
		print('\t'.join(line))
	else:
		line = line.split()
		line.append("GT")
		info = line[7].split(';')
		# string comprehension loops through line looking for AC_Hom
		# then pulls out the number of AC_Hom (# of hom_alts)
		# it then splits by , (since occasionally there are multiple types 
		# of variants. Just takes the first one, which isn't ideal, but
		# making it more complicated would take WAY more code
		# 
		# if there are any AC_Hom, then the variant gets labelled as 0/0
#		if int([x for x in info if 'AC_Hom' in x][0].split('=')[1].split(',')[0]) > 0:
#			line.append('0/0')
		# otherwise, gets called a het (0/1)
#		else:
		line.append('0/1')
		print('\t'.join(line))
