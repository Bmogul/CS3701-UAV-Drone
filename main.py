import cv2
import scipy

data = scipy.io.loadmat('./image_label/1/anotation.mat')
print(data.keys())
print(data)