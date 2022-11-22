import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os, cv2
import enum 

# https://keras.io/api/

#Px = 256

class Categories(enum.Enum):
    BOTTLE = 0
    CAN = 1
    OTHER = 2
    NO_OBJECT = 3

IMAGE_SIZE = 256
RESCALING = False
#COLOR_MODE = 'rgb'
COLOR_MODE = 'grayscale'

if COLOR_MODE == 'rgb':
  CHANNELS = 3
else:
  CHANNELS  = 1    



def classifyObject(img):

    #modelo = tf.keras.models.load_model(filepath='./ai_models/test_model.h5', custom_objects={'KerasLayer':hub.KerasLayer}, compile=True, options=None)
    modelo = tf.keras.models.load_model(filepath='./ai_models/test_model11.h5', custom_objects=None, compile=True, options=None)
    
    if COLOR_MODE == 'grayscale':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.resize(img,(IMAGE_SIZE,IMAGE_SIZE))

    if RESCALING == True:
        img_preprocessed = img / 255.0
    else:    
        img_preprocessed = img
    
    #print(img.shape)
    #print(img2)

    outputs_prediction = modelo.predict(img_preprocessed.reshape((1,IMAGE_SIZE,IMAGE_SIZE,CHANNELS)))
    #print(outputs_prediction)
    #Get the index with highest value
    prediction = np.argmax(outputs_prediction)
    
    return prediction


def testIAwithImage():
    #plt.imshow(cv2.resize(img,(Px,Px)))
    # Test Code
    img = cv2.imread('./test_images/l1_g5.png')
    prediction = classifyObject(img)
    print(f'Class with the highest probability: {Categories(prediction)}')
    print(f'Object belongs to category number : {prediction}')
    cv2.imshow('ImageWindow', img)
    cv2.waitKey()

if __name__ == "__main__":
    testIAwithImage()    

