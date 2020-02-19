import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D,Dropout,Activation
from keras.preprocessing.image import ImageDataGenerator

input_size = (128,128)
#loading data
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True) 
test_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory('../datasets/',target_size=input_size,classes=['fullsleeves','halfsleeves','sleeveless'],batch_size = 10)
validation_data = test_datagen.flow_from_directory('../datasets/',target_size=input_size,classes=['fullsleeves','halfsleeves','sleeveless'],batch_size = 10)

#design model

model = Sequential()

#Convolution and Max pooling
model.add(Conv2D(32, (3, 3), input_shape = (128, 128, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(128, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(256, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(512, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

#Flatten
model.add(Flatten())
 
#Full connection
model.add(Dense(512, activation = 'relu'))
model.add(Dense(256, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))
#Compile model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#print(model.summary())

#fit model
model.fit_generator(train_data,steps_per_epoch=10,validation_data=validation_data,validation_steps=3,epochs = 30 ,verbose = 1)


#save model and weights
model.save('model.h5')
model.save_weights('weights.h5')
