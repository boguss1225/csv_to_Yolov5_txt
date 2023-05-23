# Author : https://github.com/boguss1225
import os
import csv
from pathlib import Path
from tqdm import tqdm

# Path to be configured
source = "../images-original.csv"
dst = "../images-original/"

# Open CSV file
input_file = csv.DictReader(open(source))

def label_process(label):
    if label == "money" :
        return 0
    elif label == "animal_alive" :
        return 1
    elif label == "animal_dead" :
        return 2
    elif label == "animal_skin" :
        return 3
    elif label == "low_animal_alive" :
        return 4
    elif label == "low_animal_dead" :
        return 5
    elif label == "low_animal_skin" :
        return 6
    elif label == "muzina_alive" :
        return 7
    elif label == "muzina_dead" :
        return 8
    elif label == "muzina_skin" :
        return 9
    elif label == "orc_alive" :
        return 10
    elif label == "orc_dead" :
        return 11
    elif label == "orc_skin" :
        return 12
    elif label == "scol_alive" :
        return 13
    elif label == "scol_dead" :
        return 14
    elif label == "scol_skin" :
        return 15
    elif label == "mans_alive" :
        return 16
    elif label == "mans_dead" :
        return 17
    elif label == "mans_skin" :
        return 18
    else :
        print("label error", label)

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


    # process label
    labelname = str(label_process(line['class']))

    # write to file
    if(os.path.isfile(file_name)):
        with open(file_name,'a+') as f:
            f.write(labelname +" "+x+" "+y+" "+w+" "+h+'\n')
    else:
        with open(file_name,'w') as f:
            f.write(labelname +" "+x+" "+y+" "+w+" "+h+'\n')    
