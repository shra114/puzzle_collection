#cd to a particular directory where pngs are there 
#run : python rename_images.py <prefix> 
#    : python rename_images.py puz_low_001_ 1
#    This will rename the images to puz_low_001_01.png puz_low_001_02.png  etc

import os
import sys

myformat = ".png"
prefix   = sys.argv[1]
startnum = int(sys.argv[2])

# Define the directory path where the images are located
#directory = '/path/to/images'

# Get a list of all files and directories in the specified path
#file_list = os.listdir(directory)
file_list = os.listdir()

# Filter only the JPG files
png_files = [f for f in file_list if f.lower().endswith(myformat)]


num = startnum

for file in png_files:
    if (file[0]== "."):
        continue
    three_digit_str = str(num).zfill(3)
    num = num+1

    os.rename(file, prefix+three_digit_str+myformat)