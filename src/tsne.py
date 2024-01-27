import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from util.plot_struct import DataStruct



def plot_tsne(dataStruct:DataStruct, legend=True):
    tsne = TSNE(n_components=2, init='pca', random_state=20)
    features = np.asarray(dataStruct.features)
    tsne_result =  tsne.fit_transform(features) if not dataStruct.tsne_result else np.asarray(dataStruct.tsne_result)
    labels = dataStruct.labels
    classes = dataStruct.classes

    unique_labels = np.unique(labels)
    scatter = plt.scatter(tsne_result[:, 0], tsne_result[:, 1], c=labels, cmap='viridis')

    if legend:
        class_colors = plt.cm.viridis(np.linspace(0, 1, len(unique_labels)))
        if not classes:
            handles = [plt.Line2D([0], [0], marker='o', linestyle='None', color=class_colors[i], markerfacecolor=class_colors[i], markersize=10, label=labels[i]) for i in unique_labels]
        else:
            handles = [plt.Line2D([0], [0], marker='o', linestyle='None', color=class_colors[i], markerfacecolor=class_colors[i], markersize=10, label=classes[i]) for i in unique_labels]

        # plt.legend(handles=handles, title='Classes')
        plt.legend(handles=handles)

    plt.title(dataStruct.title)
    plt.savefig(dataStruct.filePath, dpi = dataStruct.dpi)

    if dataStruct.show:
        plt.show()

if __name__ == '__main__':
    dataStruct = DataStruct()
    import json
    with open('example/tsne.json', 'r') as f:
        data = json.load(f)
        dataStruct.features.extend(data['features'])
        dataStruct.labels.extend(data['labels'])
        dataStruct.pre.extend(data['pre'])
        dataStruct.tsne_result.extend(data['tsne_result'])
        dataStruct.classes.extend(data['classes'])
    
    dataStruct.title = 't-SNE Visualization'
    dataStruct.filePath = 'example/tsne.png'
    dataStruct.dpi = 300
    dataStruct.show = True    

    plot_tsne(dataStruct)