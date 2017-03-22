"""
detrend a timeseries
"""

import numpy as np

from scipy import stats

def xx_detrend(x,y):
    N = len(x)
    return np.random.random(N), 0., 0.

def detrend(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return y - (slope*x + intercept), slope, intercept
