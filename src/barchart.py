import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import numpy as np
from matplotlib import pyplot as plt
from util.plot_struct import DataStruct

COLORS = ([(2/255,48/255,74/255), (33/255, 158/255, 188/255), (254/255, 183/255, 5/255), (250/255, 134/255 ,0)] + plt.rcParams["axes.prop_cycle"].by_key()["color"])


def plot_barchart(data: DataStruct):
    ## determine dimensions
    x_data = data.xdata
    y_data = data.ydata

    class_num = len(data.classes)
    comparison_num = len(x_data[0])

    assert class_num > 0, 'No class data'
    assert comparison_num > 0, 'No comparison data'

    ## plot
    fig, ax = plt.subplots()
    index = np.arange(comparison_num)
    inter_width = data.inter_width
    bar_width = 0.35
    opacity = 0.8
    
    color_iter = iter(COLORS)
    if len(data.color) > 0:
        color_iter = iter(data.color)
    

    for i in range(class_num):
        plt.bar(index * (inter_width + class_num * bar_width) + i * bar_width, y_data[i], bar_width, alpha=opacity, label=data.classes[i], color = next(color_iter))

    if data.print_ydata:
        for i in range(class_num):
            for j in range(comparison_num):
                plt.text(index[j] * (inter_width + class_num * bar_width) + i * bar_width, y_data[i][j], str(y_data[i][j]), ha='center', va='bottom')

    plt.xlabel(data.xlabel)
    plt.ylabel(data.ylabel)
    plt.title(data.title)

    refine_index = index * (inter_width + class_num * bar_width) + (class_num - 1) / 2 * bar_width

    plt.grid(True, axis='y', linestyle='--', alpha=0.5)

    plt.xticks( refine_index , x_data[0] )
    
    y_lim_max = max([max(y) for y in y_data]) * 1.2
    y_lim_min = 0 if min([min(y) for y in y_data]) > 0 else min([min(y) for y in y_data]) * 1.2
    plt.ylim(y_lim_min, y_lim_max)

    plt.legend()
    plt.savefig(dataStruct.filePath, dpi = dataStruct.dpi)

    if dataStruct.show:
        plt.show()



if __name__ == '__main__':
    dataStruct = DataStruct()
    dataStruct.xdata = [['A', 'B', 'C', 'D']]
    dataStruct.ydata = [[20, 35, 30, 35], [25, 32, 34, 20], [25, 20, 31, 19]]
    dataStruct.classes = ['Class1', 'Class2', 'Class3']
    dataStruct.xlabel = 'Group'
    dataStruct.ylabel = 'Scores'
    dataStruct.print_ydata = True
    dataStruct.title = 'Scores by group'
    dataStruct.filePath = 'example/barchart.png'
    dataStruct.show = True
    plot_barchart(dataStruct)