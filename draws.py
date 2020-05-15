import matplotlib.pyplot as plt
import argparse

def plot_params(xlabel: str, ylabel:str, title: str=None):
    if title is not None:
        plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
def show():
    plt.show()
    
def add_line(xdata, ydata):
    plt.plot(xdata, ydata)
    
    
    
def format_list(l: list):    
    return [int(i) for i in l]
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--xdata', '-X', required=True,
                        type=str, nargs='+', help='No help')
    parser.add_argument('--ydata', '-Y', required=True,
                        type=str, nargs='+', help='No help')
    parser.add_argument('--xlabel', '-x', required=True,
                        type=str, nargs='+', help='No help')
    parser.add_argument('--ylabel', '-y', required=True,
                        type=str, nargs='+', help='No help')
    parser.add_argument('--title', '-t', required=False,
                        type=str, nargs='+', help='No help')
    args = parser.parse_args()
    print(args.xdata)
    if args.title is None:
        plot_data(format_list(args.xdata), format_list(args.ydata), args.xlabel[0], args.ylabel[0])
    else:
        plot_data(format_list(args.xdata), format_list(args.ydata), args.xlabel[0], args.ylabel[0], args.title[0])
    input("Press enter to quit")
    
