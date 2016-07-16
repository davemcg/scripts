#!/usr/local/bin/python3


import argparse
import subprocess
import glob
import re

parser = argparse.ArgumentParser(description =\
	"Moves image files into folders by date (Year-Month-Day)\
	and renames based on optional prepend argument")
parser.add_argument('--directory', help =\
	"Give the directory path to process files \
	Example: \
   		~/git/./Sony_ARW_Rename_and_Organize.py ~/Pictures/2016/")
parser.add_argument('--substitute', nargs='?', default="^", help =\
	"Give pattern to substitute. Default is \"^\"")
parser.add_argument('--replace', nargs='?', default='RX1RII_', help =\
	"Replacement text to replace. Default is \"RX1RII_\"")
parser.add_argument('--filetype', nargs='?', default="ARW", help =\
	"Give file ending for exiftool to process. Default is ARW.")
args = parser.parse_args()

directory_path = args.directory
substitute = args.substitute
replace = args.replace
filetype = args.filetype

path_file = directory_path + '/' + '*' + filetype
file_matches = glob.glob(path_file)

# rename
for image_file in file_matches:
	file_name = image_file.split('/')[-1]
	new_file_name = '/' + re.sub(substitute, replace, file_name)
	new_file = directory_path  + new_file_name
	# bash rename command
	mv_command = 'mv ' + image_file + ' ' + new_file
	subprocess.call(mv_command, shell='True')

# call exiftool to move files to directory (YYYY-MM-DD)
# based on image capture data exif field
exiftool_command = 'exiftool \"-Directory<DateTimeOriginal\" -d \"%Y-%m-%d\" -P -ext ' + filetype + ' ' + directory_path
subprocess.call(exiftool_command, shell='True')


