"""
Code to test if we can extract depth and temperature data from CTD file '2017-01-0118.ctd.txt', a
Canadian CTD text file. 

Goal is to make a plot of temp v depth and save it as a png in the output directory effcomp/twho_output
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
import numpy as numpy
import matplotlib.pyplot as plt

myplace = 'twho' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd.txt'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# define the output filename
out_fn = out_dir + 'out_testCTD.png'

# open the output file for writing
outfile = open(out_fn, 'w')

# make empty lists for depth and temperature
depth = []
temp = []

signal = False   # just a way of telling us when we've hit the block of data and not text

with open(in_fn, 'r', errors='ignore') as f:   # using the 'with open()' command automatically closes f when indentation goes back to normal
    for line in f:
        if signal == True:
            line_list = line.split()   # splits the columns of data
            depth.append(float(line_list[1]))   # appends the data into the empty columns in lines 36 and 37
            temp.append(float(line_list[2]))
        if '*END OF HEADER' in line and signal is False:   # I don't know what this line and the next line do
            signal = True


""" none fo this block of text worked
for line in f:
    if line == ('*END OF HEADER') and signal == False:
        signal = True
    elif signal == True:
        line_list = line.split()  # split the lines apart at the columns
        # lls[1]  # column 1 is depth (looked at the CTD text file to make sure)
        # lls[2]  # column 2 is temperature (looked at the CTD text file to make sure)
        depth.append(float(line_list[1]))
        temp.append(float(line_list[2]))
f.close()
"""

# print out the lists
print(depth)
print(temp)

# plot the temp and depth data
figure = plt.figure()
plt.plot(temp,depth)
plt.xlabel('Temperature (ºC)')
plt.ylabel('Depth (mbsl)')
plt.gca().invert_yaxis()   # inverts y-axis
plt.show()
plt.savefig('out_fn')
