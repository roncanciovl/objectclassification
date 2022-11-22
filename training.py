import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

NUMBER_OF_EPOCHS = 10
RESCALING = False
IMAGE_SIZE = 256
#COLOR_MODE = 'rgb'
COLOR_MODE = 'grayscale'

if COLOR_MODE == 'rgb':
  CHANNELS = 3
else:
  CHANNELS  = 1    

#Trainig Set

#Class 

train_ds = tf.keras.utils.image_dataset_from_directory(
    directory = "../persp_set",
    labels='inferred',
    label_mode='int',
    class_names=None,
    color_mode= COLOR_MODE,
    batch_size=32,
    image_size=(IMAGE_SIZE, IMAGE_SIZE),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False,
    )

# https://www.tensorflow.org/guide/keras/preprocessing_layers

rescaling_layer = layers.Rescaling(1./255) #NORMALIZACIÓN
train_ds_rescaled =train_ds.map(lambda x, y: (rescaling_layer(x), y))
train_ds_rescaled = train_ds_rescaled.prefetch(tf.data.AUTOTUNE)
#image_batch, labels_batch = next(iter(train_ds_rescaled))

class_names = train_ds.class_names
print(class_names)

model = tf.keras.models.Sequential([
                                                         
  # Add convolutions and max pooling
  tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMAGE_SIZE, IMAGE_SIZE, CHANNELS)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Add the same layers as before
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(4, activation='softmax')
])

# Print the model summary
model.summary()

# Use same settings
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

if RESCALING == True:
  model.fit(train_ds_rescaled, epochs = NUMBER_OF_EPOCHS)
  # Evaluate on the test set
  print(f'\nMODEL EVALUATION:')
  test_loss = model.evaluate(train_ds_rescaled)

else:
  model.fit(train_ds, epochs = NUMBER_OF_EPOCHS)
  # Evaluate on the test set
  print(f'\nMODEL EVALUATION:')
  test_loss = model.evaluate(train_ds)



# print(model.predict(train_ds))

#model.save('./ai_models/test_model2.h5')

tf.keras.models.save_model(
    model,
    filepath = './ai_models/test_model11.h5',
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None,
    save_traces=True
)


