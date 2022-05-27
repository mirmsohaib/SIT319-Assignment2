# Dependencies
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16


# def predict(img_path):
def getPrediction(filename):
     model = tf.keras.models.load_model("/Users/Sohaib/Desktop/Project/Resources/Model/cnn.hdf5")
     img = load_img('/Users/Sohaib/Desktop/Project/static'+filename, target_size=(180, 180))
     img = img_to_array(img)
     img = img / 255
     img = np.expand_dims(img,axis=0)
     category = model.predict_classes(img)
     answer = category[0]
     probability = model.predict(img)
     probability_results = 0

     if answer == 1:
          answer = "Recyclable"
          probability_results = probability[0][1]
     else:
          answer = "Not Recyclable"
          probability_results = probability[0][0]

     answer = str(answer)
     probability_results=str(probability_results)

     values = [answer, probability_results, filename]
     return values[0], values[1], values[2]