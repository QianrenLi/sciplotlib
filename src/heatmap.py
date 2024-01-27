import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from util.plot_struct import DataStruct
import matplotlib.pyplot as plt
import numpy as np

def heatmap_plot(dataStruct: DataStruct):
    import matplotlib.colors as colors
    # Create a colormap that maps 0 to white
    cmap = plt.cm.jet_r
    cmap.set_under('white')

    unique_cha1, indices_cha1 = np.unique(dataStruct.xdata, return_inverse=True)
    unique_cha2, indices_cha2 = np.unique(dataStruct.ydata, return_inverse=True)

    min_val = np.min(dataStruct.val)
    # Create a 2D array filled with zeros
    valMesh = np.zeros((len(unique_cha1), len(unique_cha2)))

    # Insert rtt values into rtts
    for i in range(len(dataStruct.val)):
        valMesh[indices_cha1[i], indices_cha2[i]] = dataStruct.val[i]

    max_val = np.max(valMesh)
    min_val = np.average(np.min(valMesh) + min_val)
    
    # Create a normalizer that maps values less than 0.5 to under
    norm = colors.Normalize(vmin=0.5, vmax=max_val)

    # Plot
    plt.imshow(valMesh, origin='lower', aspect='auto', vmin = min_val, vmax = max_val, cmap=cmap)

    # label
    plt.xticks(np.arange(len(unique_cha2)), np.round(unique_cha2,2))
    plt.yticks(np.arange(len(unique_cha1)), unique_cha1)

    # Add rtt values onto the plot
    for i in range(valMesh.shape[0]):
        for j in range(valMesh.shape[1]):
            if valMesh[i, j] > 0:
                plt.text(j, i, round(valMesh[i, j], 2), ha='center', va='center', color='black')

    plt.colorbar()
    plt.xlabel(dataStruct.xlabel)
    plt.ylabel(dataStruct.ylabel)
    plt.savefig(dataStruct.filePath, dpi = dataStruct.dpi)

    if dataStruct.show:
        plt.show()

if __name__ == '__main__':
    ## read data
    dataStruct = DataStruct()
    import json
    
    with open('example/heatmap.json', 'r') as f:
        data = json.load(f)
        for _data in data:
            if _data['rtt'] > 1 or _data['rtt'] <= 0 or _data['tx_parts'][1] > 0.3:
                continue
            dataStruct.xdata.append(_data['tx_parts'][0])
            dataStruct.ydata.append(_data['tx_parts'][1])
            dataStruct.val.append(_data['rtt'] * 1000)

    dataStruct.xlabel = '2.4G Channel Occupancy'
    dataStruct.ylabel = '5G Channel Occupancy'

    dataStruct.filePath = 'example/heatmap.png'
    dataStruct.dpi = 300
    dataStruct.show = True

    heatmap_plot(dataStruct)