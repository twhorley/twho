"""
Try to plot some solute profile data from TN 314 to test out functionality using matplotlib
"""

# Imports
import numpy as np
import matplotlib as plt
import pandas as pd

import os, sys
sys.path.append(os.path.abspath('shared'))
import my_module as mymod

myplace = 'twho'

# Input / Output Directories
in_dir = '../' + myplace + '_data/'
out_dir = '../' + myplace + '_output/'

# Define Input / Output file names
#in_fn = in_dir + 'TN314_testdata_plotting.txt'   # test set of TN314 solute data, GC4
out_fn = out_dir + 'out_TN314_testdata.png'   # spit out a png of the profile

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





