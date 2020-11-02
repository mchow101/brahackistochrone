'''
equation for curve with certain constants
plot curve, calculate time needed for ball
if the time is faster than previous time, continue updating constants

choose start, end, and some intermediate curves to animate 
'''
# imports
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches
import numpy as np

# constants
g = 9.8
# for curves
h = 10
a = 0
b = 0.1
c = -2
step = 0.001
# for animations
fname = 'test1'
width, height = 1200, 1200
nframes = 50
fps=20

x_vals = np.linspace(0, 10)

# functions
# TODO: fix and update functions
def get_curve(x):
    return a * x ** 3 + b * x ** 2 + c * x + h

def get_curve_deriv(x):
    return 3 * a * x ** 2 + 2 * b * x + c 

def get_time(acc, dist):
    return np.sqrt(np.abs(2 * acc * dist))

# optimize curve
is_optimized = False
while not is_optimized:
    plt.plot(x_vals, get_curve(x_vals))
    plt.plot(x_vals, get_curve_deriv(x_vals))
    
    m = get_curve_deriv(x_vals)
    replace = np.where(m == 0)
    acc = g * m / np.sqrt(m ** 2 + 1)
    m[replace] = np.inf
    dist = np.sqrt(x_vals[1] ** 2 + (x_vals[1] / m) ** 2)
    
    plt.plot(x_vals, get_time(acc, dist))
    a = a + step
    b = b - step * 10
    is_optimized = (a >= 0.01) # TODO: update condition
    plt.show()
    
def animate(nframe, empty=False):
    # set up frame
    t_anim = nframe / float(nframes)
    w_scale = width / np.max(x_vals)
    h_scale = height / np.max(get_curve(x_vals))
    
    fig = plt.gcf()
    fig.clf()
    ax_canvas = plt.gca()
    ax_canvas.set_position((0, 0, 1, 1))
    ax_canvas.set_xlim(0, width)
    ax_canvas.set_ylim(-height, height)
    ax_canvas.axis('off')
    
    # draw the ramp
    points = []
    for i in range(len(x_vals)):
        y = get_curve(i)
        x, y = np.array([i * w_scale, y * h_scale])
        points.append([x, y])
    
    rampline = patches.Polygon(points, closed=False, facecolor='none',
                       edgecolor='black', linewidth=4, capstyle='butt')
    # points.append([0, 0])
    # points.append([0, height])
    ramp = patches.Polygon(points, closed=True, facecolor='#c0c0c0', edgecolor='none')
    ax_canvas.add_patch(ramp)
    ax_canvas.add_patch(rampline)
    
    # add ball
    # TODO: fix animation
    y = get_curve(nframe)
    x, y = np.array([nframe, y])
    print (nframe, x, y)
    ax_canvas.add_patch(patches.Circle((x, y), radius=10.,
                            facecolor='red', edgecolor='black'))

# create and save animation
fig = plt.figure(figsize=(width/100., height/100.))
anim = animation.FuncAnimation(fig, animate, frames=nframes)
print ('saving', fname + '.gif')
anim.save(fname + '.gif', fps=fps)