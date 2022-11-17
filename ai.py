import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os, cv2
import enum 

Px = 256

class Categories(enum.Enum):
    BOTTLE = 0
    CAN = 1
    OTHER = 2
    NO_OBJECT = 3




def detectObjectAI(img):

    #modelo = tf.keras.models.load_model(filepath='./ai_models/test_model.h5', custom_objects={'KerasLayer':hub.KerasLayer}, compile=True, options=None)
    modelo = tf.keras.models.load_model(filepath='./ai_models/test_model4.h5', custom_objects=None, compile=True, options=None)
    #print(modelo)
    #print(modelo)



    img = cv2.resize(img,(Px,Px))
    #img2 = img / 255.0
    img2 = img
    print(img.shape)
    #print(img2)

    outputs_prediction = modelo.predict(img2.reshape((1,Px,Px,3)))
    print(outputs_prediction)
    # Get the index with highest value
    prediction = np.argmax(outputs_prediction)
    print(f'Class with the highest probability: {Categories(prediction)}')

    return prediction


def testIAwithImage():
    #plt.imshow(cv2.resize(img,(Px,Px)))
    # Test Code
    img = cv2.imread('./test_images/B1_G3.png')
    # detectObjectAI(img)
    # cv2.imshow('ImageWindow', img)
    # cv2.waitKey()

