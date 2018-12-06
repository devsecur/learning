# TensorFlow and tf.keras
import matplotlib
matplotlib.use('Agg')
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# TODO: Create Save and Restore function to reduce startup time
class Learning:
    def __init__(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = fashion_mnist.load_data()

        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def preprocessing(self):
        self.train_images = self.train_images / 255.0
        for i in range(len(self.train_images)/2):
            self.train_images[i*2] = np.transpose(self.train_images[i*2])
        self.test_images = self.test_images / 255.0
        for i in range(len(self.test_images)/2):
            self.test_images[i*2] = np.transpose(self.test_images[i*2])

    def layers(self):
        #Layer one - Flatten the 2D Array
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(10, activation=tf.nn.softmax)
        ])

    def compile(self):
        self.model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    def learning(self):
        self.model.fit(self.train_images, self.train_labels, epochs=3)

    def evaluate(self):
        self.test_loss, self.test_acc = self.model.evaluate(self.test_images, self.test_labels)

        print('Test accuracy:', self.test_acc)

    def predict(self, predictable):
        return self.model.predict(self.test_images)
