import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import numpy as np
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
from util.plot_struct import DataStruct
import itertools

def plot_confusion_matrix(dataStruct:DataStruct, cmap=plt.cm.Blues, fontsize=20):
    labels = dataStruct.labels
    pre = dataStruct.pre
    classes = dataStruct.classes
    title = dataStruct.title
    
    conf_numpy = confusion_matrix(labels, pre) if not dataStruct.conf_matrix else np.asarray(dataStruct.conf_matrix)

    if dataStruct.normalize:
        conf_numpy = conf_numpy.astype('float') / conf_numpy.sum(axis = 1)
        conf_numpy = np.around(conf_numpy,decimals=2)
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(conf_numpy)

    # plt.figure(figsize=(8, 7))
    plt.imshow(conf_numpy, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=fontsize)
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=fontsize)

    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, fontsize=fontsize)
    plt.yticks(tick_marks, classes, fontsize=fontsize)

    fmt = '.2f' if dataStruct.normalize else 'd'
    thresh = conf_numpy.max() / 2.
    for i, j in itertools.product(range(conf_numpy.shape[0]), range(conf_numpy.shape[1])):
        plt.text(j, i, format(conf_numpy[i, j], fmt),
                 horizontalalignment="center",
                 fontsize=fontsize,
                 color="white" if conf_numpy[i, j] > thresh else "black")

    plt.ylabel('True label', fontsize=fontsize)
    plt.xlabel('Predicted label', fontsize=fontsize)
    plt.tight_layout()
    plt.savefig(dataStruct.filePath, dpi = dataStruct.dpi)

    if dataStruct.show:
        plt.show()

if __name__ == '__main__':
    dataStruct = DataStruct()
    # dataStruct.labels = [0,0,0,0,1,1,1,1,2,2,2,2]
    # dataStruct.pre = [0,0,0,0,1,1,1,1,2,2,2,2]
    dataStruct.conf_matrix = [[40,0,0],[1,35,4],[1,5,34]]
    dataStruct.classes = ['Pushing & \nPulling','Beckoning','Rubbing \nFingers']
    dataStruct.filePath = 'example/confusion_matrix.png'
    dataStruct.title = 'Confusion Matrix'
    dataStruct.normalize = True
    dataStruct.show = True

    plot_confusion_matrix(dataStruct)

