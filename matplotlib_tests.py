"""
Script to play around with how to make a variety of plots using matplotlib and
numpy. I'll be using object-oriented interface instead of the pyplot interface to 
make plots because these are far more customizable.
"""

import matplotlib.pyplot as plt
import numpy as np

# Create a figure with 2 axes, both same scale, and plot a line
fig, ax = plt.subplots()  # creates a figure containing a single axes scale
ax.plot([1,2,3,4], [4,1,3,2])
# plt.plot([1,2,3,4], [4,1,3,2])  <-- another way to make the same plot, but simpler


# Easiest to make a new figure and axes with pyplot
fig = plt.figure()   # an empty figure with no Axes
fig, ax = plt.subplots()   # a figure with a single Axes, defaults scale 0 to 1 
fig, axs = plt.subplots(2,2)   # a figure with a 2x2 grid of plots, default scale 0-1


# Plot different equations on one figure
x = np.linspace(0,2,100)   # make array from 0 to 2 with 100 intervals between

fig, ax = plt.subplots()   # create a figure iwth an axes
ax.plot(x, x, label='linear')   # plot line x=y and name it 'linear'
ax.plot(x, x**2, label='quadratic')   # plot line x^2 and name it 'quadratic'
ax.plot(x, x**3, label='cubic')   # plot line x^3 and name it 'cubic'

ax.set_xlabel('x label')   # add an x-label to the axes
ax.set_ylabel('y label')   # add a y-label to teh axes
ax.set_title("Simple Plot")   # add a title to the axes
ax.legend()   # add a legend; I think this adds the 'label's made in the ax.plot() lines






# Show all the plots (made with 'plt') made up to this point
plt.show()




