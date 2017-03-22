"""
Simple example for testing
This code is supposed to provide functionality
to remove a linear trend from a timeseries
"""

import numpy as np
import matplotlib.pyplot as plt
from detrend import detrend

def gen_dummy_data(std=20., slope=2., offset=-5.):
    N = 1000
    x = np.arange(N)/100.
    e = np.random.random(N)*std
    y = x*slope + offset + e
    return x,y

def plot(x,y,yn):
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.plot(x,y, label='raw')
    ax.plot(x,yn,label='detrend')
    ax.legend()
    ax.grid()
    plt.show()

def main():
    x,y = gen_dummy_data()
    yn, m, b = detrend(x,y)
    plot(x,y,yn)

if __name__ == '__main__':
    main()
