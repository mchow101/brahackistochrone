# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:50:27 2020

@author: Mitali
"""

# imports
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches
import numpy as np

# constants
g = 9.8
# for curves
h = 10
a = 4
b = 1
c = -2
step = 0.1
# for animations
fname = 'test1'
width, height = 1200, 1200
nframes = 50
fps=20

t_vals = np.linspace(0, np.pi)

# functions
# TODO: fix and update functions
def get_curve(t):
    return a * (t - np.sin(t)) - b * t, a * (1 - np.cos(t))

def get_curve_deriv(x):
    return 3 * a * x ** 2 + 2 * b * x + c 

def get_v(dist):
    return np.sqrt(np.abs(2 * g * dist))

# optimize curve
is_optimized = False
while not is_optimized:
    x, y = get_curve(t_vals)
    plt.plot(x, -y)
    plt.title(a)
    # plt.plot(x_vals, get_curve_deriv(x_vals))
    
    m = get_curve_deriv(t_vals)
    replace = np.where(m == 0)
    acc = g * m / np.sqrt(m ** 2 + 1)
    m[replace] = np.inf
    dist = np.sqrt(t_vals[1] ** 2 + (t_vals[1] / m) ** 2)
    
    # plt.plot(x_vals, get_time(acc, dist))
    # a = a + step
    b = b - step
    is_optimized = (b <= -1) # TODO: update condition
plt.show()