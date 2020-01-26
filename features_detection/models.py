import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D,Dropout,Activation
from keras.preprocessing.image import ImageDataGenerator

input_size = (128,128)

def typeOfSleevesLength(images):
	classes = {0:'sleevesless',1:'full sleeves',2:'half sleeves'}

	#load and initialize model
	model = Sequential()
	model.load('./sleeve_model')
	model.load_weights('./sleeve_weights.h5')

	#predict
	prediction = model.predict_classes(images, batch_size=1)
	k.clear_session()
	return(classes[prediction[0]])



def typeOfPattern(images):
	
	classes = {0:'',1:''}

	#load and initialize model
	model = Sequential()
	model.load('./sleeve_model')
	model.load_weights('./sleeve_weights.h5')

	#predict
	prediction = model.predict_classes(images, batch_size=1)
	k.clear_session()
	return(classes[prediction[0]])

filename = '/home/pritesh/projects/ImageBasedProductRecommendation/test/skirts.jpeg'
img = image.load_img(filename, target_size=(128,128))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
result = typeOfSleeves(images)