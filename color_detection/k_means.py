from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import webcolors

PATH = 'received_images/'
actual_name__list = []
closest_name_list = []

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name



def color_cluster(img_vec):
	kmeans = KMeans(n_clusters=3)
	kmeans.fit( img_vec )

	unique_l, counts_l = np.unique(kmeans.labels_, return_counts=True)
	sort_ix = np.argsort(counts_l)
	sort_ix = sort_ix[::-1]

	fig = plt.figure()
	ax = fig.add_subplot(111)
	x_from = 0.05

	for cluster_center in kmeans.cluster_centers_[sort_ix]:
	    ax.add_patch(patches.Rectangle( (x_from, 0.05), 0.29, 0.9, alpha=None,
	                                    facecolor='#%02x%02x%02x' % (int(cluster_center[2]), int(cluster_center[1]),int(cluster_center[0] )) ) )
	    x_from = x_from + 0.31
	    requested_colour = (int(cluster_center[2]), int(cluster_center[1]),int(cluster_center[0] ))
	    print(requested_colour)
	    actual_name, closest_name = get_colour_name(requested_colour)

	    actual_name__list.append(actual_name)
	    closest_name_list.append(closest_name)
	    
	    print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)

	# plt.show()
	return actual_name__list , closest_name_list



def detect_color(masked):
	img = cv2.imread(PATH+masked)
	height, width, dim = img.shape
	# img = img[(height/4):(3*height/4), (width/4):(3*width/4), :]
	# height, width, dim = img.shape
	img_vec = np.reshape(img, [height * width, dim] )
	return color_cluster(img_vec)