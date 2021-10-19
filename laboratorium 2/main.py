import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import string
import random

def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    
    if (x1.shape != y1.shape) or (x2.shape != y2.shape):
        return None
    else:
        fig, ax = plt.subplots()
        ax.plot(x1, y1, 'b', linewidth = 4, label=label1)
        ax.plot(x2, y2, 'r', linewidth = 2, label=label2)
        ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
        ax.legend()
        return fig

def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):
    if (x1.shape != y1.shape) or (x2.shape != y2.shape) or min(x1.shape) == 0 or min(x2.shape) == 0:
        return None
    if orientation == '-':
        fig, (ax1, ax2) = plt.subplots(2,1)
    elif orientation == '|':
        fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(x1, y1)
    ax1.set(xlabel=x1label, ylabel=y1label)
    ax2.plot(x2, y2)
    ax2.set(xlabel=x2label, ylabel=y2label)
    fig.suptitle(title)
    return fig

def log_plot(x:np.ndarray,y:np.ndarray,xlabel:str,ylabel:str,title:str,log_axis:str): 
    if x.shape != y.shape:
        return None
    fig, ax = plt.subplots() 
    ax.plot(x, y)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    if log_axis == 'x':
        ax.set_xscale('log')
    elif log_axis == 'y':
        ax.set_yscale('log')
    else:
        ax.set_xscale('log')
        ax.set_yscale('log')
    return fig     