#!/usr/local/bin/python3

import re
import glob
import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description=\
	""" \
	Scrapes folders of fastqc runs and extracts \
	important info for large analyses. \
	\
	Just run in directory holding the fastqc folders. \
	Will use the folder names to name the files. """)
parser.add_argument('-d','--directory', help='Give a \
		directory to crawl that has the fastqc zip files')

args = parser.parse_args()
dir = args.directory

if dir:
	zips = glob.glob(dir + '/*zip')
else:
	zips = glob.glob('*.zip')

#unzips the fastqc data
[subprocess.call("unzip " + i, shell=True) for i in zips]

# roll through dirs and parse data 
for i in zips:
	i = i[:-4]
	file = open(i + '/fastqc_data.txt','r')
	data = file.readlines()
	for line in data:
		count = 0
		if re.match('^>>END_MODULE',line):
			continue
		elif re.match('^##', line):
			continue
		elif re.match('^>>', line):
			file_name = line.strip().split()
			# grab fastqc pass, warn, fail tag
			fastqc_filter = file_name[-1]
			# get fastqc section name and use as filename
			file_name[0] = file_name[0].split('>>')[1]
			file_name = '_'.join(file_name[0:-1])
			output = open(file_name,'a')
		elif re.match('^Filename',line): #grab input file for FastQC to write to column
			filename = line.split()[1]
		elif re.match('^#[A-Z]',line): # IDs a new section and writes the header just once
			line = line.strip() + '\tFilename' + '\tFastQC_Filter\n'
			if os.stat(file_name).st_size == 0:
				output.write(line[1:])
		else:
			line = line.strip() + '\t' + filename + '\t' + fastqc_filter + '\n'
			output.write(line)

