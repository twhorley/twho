"""
Code to explore how to use argparse

Code to test passing command line arguments to a program using the 
argparse module.

This is a helpfule technique for making code that runs both on your
laptop and on a remote machine - where you might tell it to process
a larger pile of data.

Usage from the linux command line:
python use_argparse -a 'hello' -b 6 -v True

Usage from the ipython command line:
run use_argparse -a 'hello' -b 6 -v True
"""

# Imports
import argparse

def boolean_string(s):
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True'   # == means that it truly equals, I think

# Create the parser object
parser = argparse.ArgumentParser()

parser.add_argument('-a', '--a_string', default='hi', type=str)
parser.add_argument('-b', '--b_string', default='today is my birthday ', type=str)
parser.add_argument('-c', '--c_string', default='now I am:', type=str)
parser.add_argument('-d', '--integer_d', default=20, type=int)
parser.add_argument('-e', '--integer_e', default=9, type=int)
parser.add_argument('-v', '--verbose', default=True, type=boolean_string)


# Get the arguments
args = parser.parse_args()

# Output
print('\nYour string is ' + args.a_string + args.b_string + args.c_string)
print(args.integer_d + args.integer_e)


