"""
Try to plot some solute profile data from TN 314 to test out functionality using matplotlib
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Local imports, file paths
import os, sys
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
myplace = 'twho'

# Input / Output Directories
in_dir = '../' + myplace + '_data/'
out_dir = '../' + myplace + '_output/'

# Define Input / Output file names
#in_fn = in_dir + 'TN314_testdata_plotting.txt'   # test set of TN314 solute data, GC4
out_fn = out_dir + 'TN314_GC4test.png'   # spit out a png of the profile



# ====================================================================
# Take 1 : Try to copy what we did in a previous homework and turn my data
# into a text file that I could read in and parse into columns using 'line.split'
"""
# Open the output file for writing
outfile = open(out_fn, 'w')

# Make empty lists for Cl, Br, SO4
Cl = []
Br = []
SO4 = []

signal = False

with open(in_fn, 'r', errors='ignore') as f:
    for line in f:
        if signal == True:
            line_list = line.split()
            Cl.append(float(line_list[1]))
            Br.append(float(line_list[2]))
            SO4.append(float(line_list[3]))
        if '*END OF HEADER' in line and signal is False:
            signal = True

print(Cl)
"""

# ====================================================================

# Take 2 : I don't want to waste time wrangling with turning copy/pasted
# Excel columns into a text file and then reading that in. I'll explore
# the pandas read_csv module instead. I took one gravity core (GC4) from 
# TN314 cruise, three measured solutes, and will plot them here.


# Data file
in_fn = in_dir + 'TN314data.csv'

# Read the CSV file and pull each column of data into its own variable
GC4 = pd.read_csv(in_fn)

depth = GC4['Depth (cm)']
Cl = GC4['Cl (mM)']
Br = GC4['Br (mM)']
SO4 = GC4['SO4 (mM)']


# Make some plots
#fig = plt.figure(figsize=(12,8))
#fig, ax = plt.subplots()
#fig, ax = plt.subplots(1, 3, sharey=True)   # sharey makes all subplots share a y-axis
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)  # this way I have more control over each subplot

ax1.plot(Cl,depth, 'D', color='k', markersize=5)
ax1.set_xlabel('$Cl^{-} (mM)$')  # or ax1.set_xlabel('Cl (mM)') if I didn't want charge
ax1.set_ylabel('Depth (cmbsf)')
ax1.set_xlim([0, 600])

ax2.plot(Br,depth, 'D', color='k', markersize=5)
ax2.set_xlabel('$Br^{-} (mM)$')
ax2.set_xlim([0, 1])

ax3.plot(SO4,depth, 'D', color='k', markersize=5)  # in the future, assign variables to color and 
# markersize so I don't have to type it all out again each time; ex: ms = markersize=5 ?
ax3.set_xlabel('$SO_4^{2-} (mM)$')
ax3.set_xlim([0, 30])

# Make plots look better
fig.suptitle('TN314 Site 2 GC4 downcore solute profiles')   #title over all plots
plt.gca().invert_yaxis()   # inverts y-axis
plt.savefig(out_fn)
plt.show()


