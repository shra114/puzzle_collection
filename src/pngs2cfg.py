#pngs to cfgfile

import os
import sys

heading = sys.argv[1]
myformat = ".png"
file_list = os.listdir()

# Filter only the JPG files
png_files = [f for f in file_list if f.lower().endswith(myformat)]

strout = "Heading : "+heading + "\n"


for myfile in png_files:
    if (myfile[0]== "."):
        continue

    strout += "/startq\n"
    strout += "Q \n"
    strout += "I "+myfile+"\n"
    strout += "O \n"
    strout += "S \n"
    strout += "/endq\n"

print (strout)