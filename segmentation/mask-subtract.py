import cv2
import numpy as np
from PIL import Image



def mask_subtract(img , mask):  
	out = Image.new('RGB', img.size, 0xffffff)

	width, height = mask.size
	tr,tg,tb = mask.getpixel((0,0))
	for x in range(width):
	    for y in range(height):
	        r,g,b = mask.getpixel((x,y))
	        if r == tr and g == tg and b == tb:
	            out.putpixel((x,y), 0)
	        else:
	        	out.putpixel((x,y), img.getpixel((x,y)))   	
	out.save('bar.png')

img = Image.open("shirt.jpeg") 
mask = Image.open("out.png")
mask_subtract(img , mask)