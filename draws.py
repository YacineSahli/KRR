import matplotlib.pyplot as plt
import sys

SAVE = False

COLORS = {}

def plot_params(xlabel: str, ylabel: str, title: str=None):
    if title is not None:
        plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    
def read_file(filepath: str):
    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()
    
    i = 0
    while i < len(lines) and i != -1:
        i = plot_data(lines, i)
        i += 1
    
    
def plot_data(filelines, index):
    i = skip_empty_lines(filelines, index)
    line = filelines[i]
    sline = line.split('=')
    
    if sline[0] != 'legend':
        return -1
    legend = False
    if sline[1] == '1\n':
        legend = True 
    
    i += 1
    sline = filelines[i].split('|')
    
    title = sline[0]
    if sline[1] == '':
        filename = title.replace(' ','') + '.png'
    else:
        filename = sline[1].replace(' ','') + '.png'
    
    i = skip_empty_lines(filelines, i+1)
    xlabel, ylabel = filelines[i].strip('\n').split('-')
    
    plot_params(xlabel, ylabel, title)
    
    i += 1
    while filelines[i] != '---\n':
        add_curve(filelines, i, legend)
        i += 3
        
    if legend:
        leg = plt.legend()
    
    if SAVE:
        plt.savefig(filename, format='png', dpi=200)
    else:
        if leg:
            leg.set_draggable(True)
        plt.show()
    plt.close() 
    return i    
    
    
def add_curve(filelines, index, legend):
    xi, yi, name = filelines[index:index+3]
    xdata = [float(n) for n in xi.strip('\n').split(',')]
    ydata = [float(n) for n in yi.strip('\n').split(',')]
    
    q_name, q_type = name.split(' - ')

    col = COLORS.get(q_name)
        
    if q_type == 'fo\n':
        p = plt.plot(xdata, ydata, color=col, marker='o', linestyle='dashed')
    else:
        p = plt.plot(xdata, ydata, color=col, marker='o', label=q_name)
    
    if COLORS.get(q_name) is None:
        COLORS[q_name] = p[0].get_color()
        
    
def skip_empty_lines(filelines, i):
    line = filelines[i]
    while line == '\n':
        i += 1
        line = filelines[i]
    return i
    
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must specify the file you want to treat")
    else:
        read_file(sys.argv[1])
        
"""
The input file must respect this syntax :

----------------------
legend=1
title first plot | filename | information not readed

x_axis title - y_axis title
x1, x2, x3, x4 
y1, y2, y3, y4 
first curve name
x11, x12, x13, x14
y11, y12, y13, y14
second curve name
---

legend=0
title second plot - 
...
---
---------------------


A '-' must be placed after the plot titles, even if no information follows
The filename must be without extension
If '--' follows the plot title, the plot will be saved on ./'titlewithoutspaces.png'
(x1, y1), (x2, y2), ... are the points of the first curve
(x11, y11), (x12, y12) the points of the second curve
the curves names are only used when legend=1 but must always be specified
Other curves can be added following the same syntax
After a plot specification, a '---' is needed
"""

