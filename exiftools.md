# prepends 4 digit year to files ending in jpg in current dir
exiftool '-filename<DateTimeOriginal' -d %Y__%%f.%%e -ext jpg .
# replaces exif date with 1984-01-01 12pm for all jpg in current dir
exiftool "-datetimeoriginal=1984:01:01 12:00:00" -ext jpg .
