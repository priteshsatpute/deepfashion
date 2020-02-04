from keras_segmentation.pretrained import  pspnet_101_voc12
import cv2
import numpy as np

PATH = 'received_images/'
def segmentImage(img):
	#model = pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset

	# model = pspnet_101_cityscapes() # load the pretrained model trained on Cityscapes dataset

	model = pspnet_101_voc12() # load the pretrained model trained on Pascal VOC 2012 dataset

	out = model.predict_segmentation(
	    inp=PATH + img,
	    out_fname=PATH + 'out.jpeg'
	)

#segmentImage('../received_images/d.jpeg')