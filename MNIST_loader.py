import numpy as np

def load_training_images(filepath):
    with open(filepath, "rb") as file:
        file.seek(16)
        x = np.fromfile(file, dtype=np.ubyte, count=784*60000)
        x = np.reshape(x, (60000, 784, 1))
        x = x/255.0
    return x


def load_training_labels(filepath):
    with open(filepath, "rb") as file:
        file.seek(8)
        labels = np.fromfile(file, dtype=np.ubyte, count=60000)
    return labels


def load_test_images(filepath):
    with open(filepath, "rb") as file:
        file.seek(16)
        x = np.fromfile(file, dtype=np.ubyte, count=784*10000)
        x = np.reshape(x, (10000, 784, 1))
        x = x/255.0
    return x


def load_test_labels(filepath):
    with open(filepath, "rb") as file:
        file.seek(16)
        labels = np.fromfile(file, dtype=np.ubyte, count=10000)
    return labels
