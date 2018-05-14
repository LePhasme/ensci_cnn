# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 3 - Test

from keras.models import load_model

import sys

train_index = sys.argv[1]
train_image = sys.argv[2]

classifier = load_model('training_set_' + train_index + '.h5')

import numpy as np

from keras.preprocessing import image

test_image = image.load_img('testset/' + train_image, target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

result = classifier.predict(test_image)

if result[0][0] == 1:
  prediction = '--> SECOND category (B)'
else:
  prediction = '--> FIRST category (A)'

print(prediction)
