# TensorFlow and tf.keras
import matplotlib
matplotlib.use('Agg')
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

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
        self.model.fit(self.train_images, self.train_labels, epochs=10)

    def evaluate(self):
        self.test_loss, self.test_acc = self.model.evaluate(self.test_images, self.test_labels)

        print('Test accuracy:', self.test_acc)

    def predict(self, predictable):
        return self.model.predict(self.test_images)

test = Learning()
# Visualize one image
plt.figure()
plt.imshow(test.train_images[0])
plt.colorbar()
plt.grid(False)
plt.savefig("foo.png")

test.preprocessing()
# Visualize preprocessed images
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test.train_images[i], cmap=plt.cm.binary)
    plt.xlabel(test.class_names[test.train_labels[i]])
plt.savefig("bar.png")

test.layers()
test.compile()
test.learning()
test.evaluate()
predictions = test.predict(test.test_images)

def plot_image(i, predictions_array, true_label, img, class_names):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
        100*np.max(predictions_array),
        class_names[true_label]),
        color=color)
    #plt.savefig("predictions_%s.png"%i)

def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
    #plt.savefig("predictions_values_%s.png"%i)

num_rows = 10
num_cols = 10
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test.test_labels, test.test_images, test.class_names)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test.test_labels)
plt.savefig("predictions.png")
