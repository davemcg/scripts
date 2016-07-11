#!/usr/local/bin/python3


import argparse
import subprocess
import glob

parser = argparse.ArgumentParser(description =\
	"Moves image files into folders by date (Year-Month-Day)\
	and renames based on optional prepend argument")
parser.add_argument('--directory', help =\
	"Give the directory path to process files \
	Example: \
   		~/git/./Sony_ARW_Rename_and_Organize.py ~/Pictures/2016/")
parser.add_argument('--pattern', nargs='?', default="D*.ARW", help =\
	"Give pattern to identify files to move. Default is \"D.*ARW\"")
parser.add_argument('--prepend', nargs='?', default="", help =\
	"Prepend to each file. Default is nothing.")
parser.add_argument('--filetype', nargs='?', default="ARW", help =\
	"Give file ending for exiftool to process. Default is ARW.")
args = parser.parse_args()

directory_path = args.directory
pattern = args.pattern
prepend = args.prepend
filetype = args.filetype

path_file = directory_path + '/' + pattern
file_matches = glob.glob(path_file)

# rename
for image_file in file_matches:
	file_name = image_file.split('/')[-1]
	new_file = directory_path  + prepend + file_name
	# bash rename command
	mv_command = 'mv ' + image_file + ' ' + new_file
	subprocess.call(mv_command, shell='True')

# call exiftool to move files to directory (YYYY-MM-DD)
# based on image capture data exif field
exiftool_command = 'exiftool \"-Directory<DateTimeOriginal\" -d \"%Y-%m-%d\" -P -ext ' + filetype + ' ' + directory_path
subprocess.call(exiftool_command, shell='True')


