"""
Code to explore numpy arrays, pickle
"""

# imports
import numpy as np
import sys, os
import pickle

# make sure I have a place to save and output results
myplace = 'twho' 
out_dir = '../' + myplace + '_output/'

print('\nCreate an 1-D array (vector) from a [list]')
list1 = [5, 6, 9, 2, 10,]
a = np.array(list1)
print(a)


# Mess around with making arrays
print('\nCreate a 2-D array (matrix) from a [list]')
list2 = [list1 , [3, 5, 4, 28, 9]]
b = np.array(list2)
print(b)

bdim = b.ndim   # ndim gives the dimensions of the array
bshape = b.shape   # shape gives shape of the array, for example (2,5) for 2 rows and 5 columns
print(bdim, bshape)

print('\nnp.array inferes a data type that fits the array you made')
list3 = [['hi', 'how', 'are', 'you'], ['thank', 'you', 'and', 'goodbye']]
c = np.array(list3)
print(c)
ctype = c.dtype
print(ctype)

atype = a.dtype
print(atype)

btype = b.dtype
print(btype)


# Test 5 methods of choice on numpy arrays

print('\nArray Method 1 = np.concatenate(b,x)')
x = np.array(np.arange(10)).reshape((2,5))
d = np.concatenate((b,x), axis=1)
print(d)

print('\nArray Method 2 = mean with np.mean(d)')
mean = np.mean(d)
print(mean)

print('\nArray Method 3 = standard deviation with np.std(d)')
std = np.std(d)
print(std)

print('\nArray Method 4 = np.transpose(b)')
T = np.transpose(b)
print(T)

print('\nArray Method 5 = np.count_nonzero(d)')
d_int = np.count_nonzero(d)
print(d_int)


# Save an array as a pickle file
out_fn = out_dir + 'pickled_array.p'
pickle.dump(d, open(out_fn, 'wb'))  # 'wb' writes binary pickle file

# Read the pickled array back in
read_p = pickle.load(open(out_fn, 'rb'))  # 'rb' reads the binary file (read binary)

print('\nThe shape of the loaded object is:')
print(d.shape)