# Author : https://github.com/boguss1225
import os
import csv
from pathlib import Path
from tqdm import tqdm

# Path to be configured
source = "/Users/bogus/Desktop/dst/data_test.csv"
dst = "/Users/bogus/Desktop/dst/"

# Open CSV file
input_file = csv.DictReader(open(source))

for line in tqdm(list(input_file)):
    # define file name
    source_name = Path(line['filename']).stem
    file_name = source_name+".txt"
    file_name = os.path.join(dst,file_name)

    # get data from csv into int
    xmin = int(line['xmin'])
    xmax = int(line['xmax'])
    ymin = int(line['ymin'])
    ymax = int(line['ymax'])
    width = int(line['width'])
    height = int(line['height'])

    # calculate values into YOLOv5 format
    x = (xmin+xmax)/(2*width)
    y = (ymin+ymax)/(2*height)
    w = (xmax-xmin)/width
    h = (ymax-ymin)/height

    # round values
    x = str(round(x,6))
    y = str(round(y,6))
    w = str(round(w,6))
    h = str(round(h,6))

    # write to file
    if(os.path.isfile(file_name)):
        with open(file_name,'a+') as f:
            f.write(line['class']+" "+x+" "+y+" "+w+" "+h+'\n')
    else:
        with open(file_name,'w') as f:
            f.write(line['class']+" "+x+" "+y+" "+w+" "+h+'\n')    
