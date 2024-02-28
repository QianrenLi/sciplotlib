import os, sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import numpy as np
from matplotlib import pyplot as plt
from util.plot_struct import DataStruct

COLORS = ([(2/255,48/255,74/255), (33/255, 158/255, 188/255), (254/255, 183/255, 5/255), (250/255, 134/255 ,0)] + plt.rcParams["axes.prop_cycle"].by_key()["color"])

def plot_cdf(data: DataStruct):
    ## determine dimensions
    x_data = data.xdata

    class_num = len(data.classes)
    is_label = True
    if class_num == 0:
        class_num = 1
        is_label = False

    line_style_num = len(data.line_style)
    is_line_style = True if line_style_num > 0 else False

    assert line_style_num == class_num or line_style_num == 0, 'line_style should be same as class_num or 0'    

    color_iter = iter(COLORS)
    if len(data.color) > 0:
        color_iter = iter(data.color)

    ## Plot cdf
    fig, ax = plt.subplots()
    line_style = ['-', '--', '-.', ':']
    for i in range(len(x_data)):
        x = np.sort(x_data[i])
        y = np.arange(1, len(x) + 1) / len(x)
        if is_line_style:
            plt.plot(x, y, line_style[data.line_style[i]] , label=data.classes[i], color=next(color_iter))
        else:
            plt.plot(x, y , label=data.classes[i], color=next(color_iter))
    
    plt.xlabel(data.xlabel)
    plt.ylabel(data.ylabel)
    plt.title(data.title)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.legend()

    if is_label:
        plt.legend()
    plt.savefig(data.filePath, dpi = data.dpi)

    if data.show:
        plt.show()

    return fig

if __name__ == '__main__':
    data = DataStruct()
    data.xdata = [np.random.normal(0, 1, 1000), np.random.normal(1, 1, 1000)]
    data.classes = ['class1', 'class2']
    data.xlabel = 'x'
    data.ylabel = 'y'
    data.title = 'CDF'
    data.filePath = 'example/cdf.png'
    plot_cdf(data)