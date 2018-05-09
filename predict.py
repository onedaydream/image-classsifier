import tensorflow as tf
import numpy as np
import os,glob,cv2
import sys,argparse
from check_name import check


# Image path
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path=sys.argv[1]
filename = dir_path +'/' +image_path
image_size=128
num_channels=3
images = []
# Reading the image using OpenCV
image = cv2.imread(filename)
# Resizing the image to desired size
image = cv2.resize(image, (image_size, image_size),0,0, cv2.INTER_LINEAR)
images.append(image)
images = np.array(images, dtype=np.uint8)
images = images.astype('float32')
images = np.multiply(images, 1.0/255.0)
# Reshape input to [1 image_size image_size num_channels].
x_batch = images.reshape(1, image_size,image_size,num_channels)

# Start session
sess = tf.Session()
# Recreate the network graph.
saver = tf.train.import_meta_graph('result.meta')
# Load weights
saver.restore(sess, tf.train.latest_checkpoint('.'))

# Accessing the default graph
graph = tf.get_default_graph()

# Prediction
y_pred = graph.get_tensor_by_name("y_pred:0")

# Let's feed the images to the input placeholders
x= graph.get_tensor_by_name("x:0") 
y_true = graph.get_tensor_by_name("y_true:0") 
y_test_images = np.zeros((1, 35)) 


#print y_true
### Creating the feed_dict that is required to be fed to calculate y_pred 
feed_dict_testing = {x: x_batch, y_true: y_test_images}

result=sess.run(y_pred, feed_dict=feed_dict_testing)
# result is of this format [probabiliy_of_rose probability_of_sunflower]
#print(result)
#print(max(result[0]))

#print (sorted(result[0])[-2])
p1, = np.where(result[0] == sorted(result[0])[-1])
p2, = np.where(result[0] == sorted(result[0])[-2])
p3, = np.where(result[0] == sorted(result[0])[-3])
#print(type(int(i)))
lines = []
with open('classess.txt') as f:
	lines = f.read().splitlines()
#print (lines[int(i)])
print ('**********************************************************')
print ('the top 3 possibility')
print ('the picture may be {}, the accuracy of that is {}'.format(lines[int(p1)], sorted(result[0])[-1]))
print ('the picture may be {}, the accuracy of that is {}'.format(lines[int(p2)], sorted(result[0])[-2]))
print ('the picture may be {}, the accuracy of that is {}'.format(lines[int(p3)], sorted(result[0])[-3]))
print ('**********************************************************')
check(lines[int(p1)])
check(lines[int(p2)])
check(lines[int(p3)])