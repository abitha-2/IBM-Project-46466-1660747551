# -*- coding: utf-8 -*-
"""Apply_ImageDataGenerator_Functionality_To_Train_And_Test_Set.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xxYvKaLFXWildZ3rWIIWeOF2MM1Y9DRh

# **Image Preprocessing**

### **Import ImageDataGenerator Library And Configure It**
"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Training Datagen
train_datagen = ImageDataGenerator(rescale=1/255,zoom_range=0.2,horizontal_flip=True,vertical_flip=False)
# Testing Datagen
test_datagen = ImageDataGenerator(rescale=1/255)

import tensorflow as tf
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as display
from PIL import Image
import pathlib

"""## Apply ImageDataGenerator Functionality To Train And Test set"""

from google.colab import drive

!unzip '/content/DATASET.zip'

from tensorflow.keras.preprocessing.image import ImageDataGenerator
print("This dataset has been created and uploaded by IBM-TeamID-IBM-Project-45753-1660732074")

train_datagen = ImageDataGenerator(rescale=1./255,zoom_range=0.2,horizontal_flip=True, vertical_flip=False)

test_datagen= ImageDataGenerator(rescale=1./255)

x_train = train_datagen.flow_from_directory('/content/drive/MyDrive/dataset/training_set',target_size=(64,64), batch_size=300,
                                          class_mode='categorical', color_mode = "grayscale")

x_test = test_datagen.flow_from_directory('/content/drive/MyDrive/dataset/test_set',target_size=(64,64), batch_size=300,
                                          class_mode='categorical', color_mode = "grayscale")

x_train.class_indices

x_test.class_indices