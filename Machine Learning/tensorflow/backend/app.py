import io
import numpy as np

from flask import Flask
from flask import Response
from flask import jsonify


from marvin import Learning
from Pagination import Pagination
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
app = Flask(__name__)

test = Learning()


@app.route('/test/<int:page>')
def testset(page):
    paginator = Pagination(test.predictions.tolist())
    return jsonify(paginator.page(page))


#TODO Create Microservice for Marvin with only a few Options. Later: Create multiple Microservices for Preprocessing and so on
#TODO Create Middleware for frontend communication
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/plot/<int:id>')
def plot(id):
    fig = plot_image(id)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

#TODO Function for Ploting one Image
def print_image(id):
    # Visualize one image
    figure = plt.figure()
    plt.imshow(test.train_set_pp[id], cmap=plt.cm.binary)
    plt.grid(False)
    return figure

def get_infos():
    results = {}
    results["Test Set"] = len(test.test_set_pp)
    results["Train Set"] = len(test.train_set_pp)
    results["Class Names"] = test.class_names

def plot_image(id):
    def image(i, predictions_array, true_label, img, class_names):
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

    def value_array(i, predictions_array, true_label):
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

    figure = plt.figure(figsize=(4, 2))
    plt.subplot(1, 2, 1)
    image(id, test.predictions, test.test_labels, test.test_set_pp, test.class_names)
    plt.subplot(1, 2, 2)
    value_array(id, test.predictions, test.test_labels)
    return figure


if __name__ == '__main__':
    app.run(host='0.0.0.0')
