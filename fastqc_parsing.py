#!/usr/local/bin/python3

import glob
import subprocess
import argparse

parser = argparse.ArgumentParser(description=\
        """ \
        Scrapes folders of fastqc runs and extracts \
        important info for large analyses. \
        \
        Just run in directory holding the fastqc folders. \
        Will use the folder names to name the files. """)


zips = glob.glob('*.zip')

#unzips the fastqc data
[subprocess.call("unzip " + i, shell=True) for i in zips]


# roll through dirs and parse data 
for i in zips[:=4]:
    file = i + '/fastqc_data.txt'
    data = file.readlines()
    for i in data:
        if i != '>>END_MODULE'
            continue
        if i[0:2] == '>>':
            file_name = '_'.join(i.split()[0])
            output = open(file_name,'w')
        if re.match(i,'^#[A-Z]'):
            i = i.strip() + '\tFilename\n'
        if re.match(i,'^Filename'):
            filename = i.split()[1]
            output.write(i)
        else:
            i = i.strip() + '\t' + filename + '\n'
            output.write(i)

