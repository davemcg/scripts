# prepends 4 digit year to files ending in jpg in current dir
exiftool '-filename<DateTimeOriginal' -d %Y__%%f.%%e -ext jpg .
# replaces exif date with 1984-01-01 12pm for all jpg in current dir
exiftool "-datetimeoriginal=1984:01:01 12:00:00" -ext jpg .
# for loops to do the above two in folders starting with 19:
for i in 19*; do exiftool "-datetimeoriginal=$i:01:01 12:00:00" $i ; done

for i in 19*; do rm $i/*_original; done

for i in 19*; do exiftool '-filename<DateTimeOriginal' -d %Y__%%f.%%e -ext jpg $i ; done
