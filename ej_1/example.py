import display
import random
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.metrics

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["QT_STYLE_OVERRIDE"] = ""

"""
Para que las funciones retornen el resultado esperado,
usted debe cargar los datos con los siguientes nombres:
images, labels, model
"""


def show_image(images: np.array, labels: np.array, i: int, labelmap: dict):
    print(f"This image is from class: {labelmap[labels[i]]}")
    plt.figure()
    plt.imshow(images[i])
    plt.colorbar()
    plt.grid(True)
    plt.title(labelmap[labels[i]])
    plt.show()


def make_prediction(images: np.array, i: int, all_images: bool = False):
    if all_images:
        return model.predict(images)
    else:
        return np.argmax(model.predict(np.array([images[i]])))


if __name__ == "__main__":
    # numpy disable scientific notation
    np.set_printoptions(suppress=True)

    # loading dataset, labels and model
    print("\n- loading images...")
    images = np.load(os.path.join(os.getcwd(), "data", "images.pickle"), allow_pickle=True)
    labels = np.load(os.path.join(os.getcwd(), "data", "labels.pickle"), allow_pickle=True)
    model = np.load(os.path.join(os.getcwd(), "data", "model.pickle"), allow_pickle=True)
    print(f"- images: {images.shape}")
    print(f"- labels: {labels.shape}")

    # labelmap
    labelmap = np.array(
        [
            "T-shirt/top",
            "Trouser",
            "Pullover",
            "Dress",
            "coat",
            "Sandal",
            "Shirt",
            "Sneaker",
            "Bag",
            "Ankle boot",
        ]
    )

    # suffle list of images
    random.shuffle(images)

    # run prediction
    print("\n- running prediction")
    detections = make_prediction(images=images, i=0, all_images=True)
    detections = np.argmax(detections, axis=1)

    # extract 12-pack images
    images = images[:12]
    pred = detections[:12]

    # display prediction
    display.visualize(images, pred, labelmap)

    # calculate prediction report
    print("\n- confusion matrix and classification report")
    cm = sklearn.metrics.confusion_matrix(labels, detections)
    report = sklearn.metrics.classification_report(labels, detections, target_names=labelmap)
    print(report)

    # plot confusion matrix
    disp = sklearn.metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labelmap)
    disp.plot()
    plt.xticks(rotation=45)
    plt.show()
