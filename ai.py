import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import os, cv2

Px = 224


modelo = tf.keras.models.load_model(filepath='./ai_models/modeloProV2_1.h5', custom_objects={'KerasLayer':hub.KerasLayer}, compile=True, options=None)
#print(modelo)

img = cv2.imread('./test_images/f1_g7.png')
img = cv2.resize(img,(Px,Px))
print(img.shape)

print(modelo.predict(img.reshape((1,224,224,3))))
plt.imshow(cv2.resize(img,(Px,Px)))

cv2.imshow('ImageWindow', img)

cv2.waitKey()