from flask import Flask
from marvin import Learning
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
app = Flask(__name__)

test = Learning()

#TODO Create Microservice for Marvin with only a few Options. Later: Create multiple Microservices for Preprocessing and so on
#TODO Create Middleware for frontend communication
@app.route('/')
def hello():
    return "Hello World!"

#TODO Change Plot to Json Object to show with d3js
def print_images():
    global test
    # Visualize preprocessed images
    figure = plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(test.train_images[i], cmap=plt.cm.binary)
        plt.xlabel(test.class_names[test.train_labels[i]])
    return figure

#TODO Create real Plot function for Image and classification Statistics
@app.route('/plot.png')
def plot_png():
    fig = print_images()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

#TODO Function for Ploting one Image
def print_image():
    # Visualize one image
    plt.figure()
    plt.imshow(test.train_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.savefig("foo.png")

def plot_images():
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

if __name__ == '__main__':
    test.preprocessing()
    test.layers()
    test.compile()
    test.learning()
    test.evaluate()
    predictions = test.predict(test.test_images)
    app.run(host='0.0.0.0')
