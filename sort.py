from os.path import isfile, join
from os import listdir
from shutil import copyfile
import os
import csv

#global value
picnames = []
categorys_1 = []
#categorys_2 = []
#categorys_3 = []
data_dir = "./picture"

#open csv
with open('Pictures.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')

	for row in readCSV:
		try:
			picname = int(row[0])
		except:
			continue

		category_1 = row[1]
#		category_2 = row[3]
#		category_3 = row[5]

		picnames.append(picname)
		categorys_1.append(category_1)
#		categorys_2.append(category_2)
#		categorys_3.append(category_3)

#create folder
for filename in listdir(data_dir):
    if isfile(join(data_dir, filename)):
        tokens = filename.split('.')
        if tokens[-1] == 'jpg':
            image_path = join(data_dir, filename)
            fileindex = picnames.index(int(tokens[0]))
            
            if not os.path.exists(join(data_dir, categorys_1[fileindex])):
                os.makedirs(join(data_dir, categorys_1[fileindex]))
#            if not os.path.exists(join(data_dir, categorys_2[fileindex])):
#                os.makedirs(join(data_dir, categorys_2[fileindex]))
#            if not os.path.exists(join(data_dir, categorys_3[fileindex])):
#                os.makedirs(join(data_dir, categorys_3[fileindex]))
            copyfile(image_path, join(join(data_dir, categorys_1[fileindex]), filename))
#            copyfile(image_path, join(join(data_dir, categorys_2[fileindex]), filename))
#            copyfile(image_path, join(join(data_dir, categorys_3[fileindex]), filename))
            os.remove(image_path)
        else:
        	image_path = join(data_dir, filename)
        	os.remove(image_path)	


