from os.path import isfile, join
from os import listdir
from shutil import copyfile
import os
import csv

#global value
def check(index1):
    categorys_1 = []
    categorys_2 = []
    data_dir = "./picture"

    #open csv
    with open('Pictures.csv') as csvfile:
    	readCSV = csv.reader(csvfile, delimiter = ',')

    	for row in readCSV:
            category_1 = row[1]
            category_2 = row[2]
            categorys_1.append(category_1)
            categorys_2.append(category_2)

    print (categorys_2[categorys_1.index(index1)])
