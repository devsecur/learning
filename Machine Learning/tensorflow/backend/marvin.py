import os

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
        self.path = "/notebooks/app/checkpoint.ckpt"

        self.source()
        self.datamining()
        self.preprocessing()
        self.layers()
        self.compile()
        if os.path.isfile(self.path+".index"):
            self.model.load_weights(self.path)
        else:
            self.learning()
        self.evaluate()
        self.predictions = self.predict(self.test_set_pp)

    def source(self):
        self.fashion_mnist = keras.datasets.fashion_mnist


    def datamining(self):
        """Mining necessary features for processing.
        Return:
        train_set
        train_labels
        test_set
        test_labes
        class_names
        """
        (self.train_set, self.train_labels), (self.test_set, self.test_labels) = self.fashion_mnist.load_data()

        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


    #TODO Define preprocessing language to make preprocessing easy
    def preprocessing(self):
        """Preprocess train_set and test_set
        """
        self.train_set_pp = self.train_set / 255.0
        for i in range(len(self.train_set)/2):
            self.train_set_pp[i*2] = np.transpose(self.train_set[i*2])
        self.test_set_pp = self.test_set / 255.0
        for i in range(len(self.test_set)/2):
            self.test_set_pp[i*2] = np.transpose(self.test_set[i*2])

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
        checkpoint_path = "cp.ckpt"
        checkpoint_dir = os.path.dirname(checkpoint_path)

        # Create checkpoint callback
        cp_callback = tf.keras.callbacks.ModelCheckpoint(self.path,
                                                         save_weights_only=True,
                                                         verbose=1)

        self.model.fit(self.train_set_pp, self.train_labels, epochs=3, callbacks = [cp_callback])

    def evaluate(self):
        self.test_loss, self.test_acc = self.model.evaluate(self.test_set_pp, self.test_labels)

        print('Test accuracy:', self.test_acc)

    def predict(self, predictable):
        return self.model.predict(self.test_set_pp)
