"""
Our first experimentation with methods that can be enacted on a string. Yahoo!
"""

# define a string
a = 'abcdefg' 
A = 'ABCDEFG'
b = 'python for data analysis'
c = '1234567'

# an example of ' zfill ' method. This method basically pads a numeric string
# with zeros to fit the length of characters defined
#def experiment(a):
print('a.zfille(10)')
print(a.zfill(10))  # should return '000abcdefg'


# an example of ' capitalize ' method. This method makes the first character 
# of the string upper case and the rest lower case
print('a.capitalize()')
print(a.capitalize())  # should return 'Abcdefg'
print('b.capitalize()')
print(b.capitalize())  # should return 'Python for data analysis'

# an example of 'title ' method. This is differnet from ' characterize ' in that
# it capitalizes the first letter of every word in the given string.

print('a.title()')
print(a.title())  # should return 'Abcdefg'
print('b.title()')
print(b.title())  # should return 'Python For Data Analysis'

# an example of ' swapcase ' method. This will return a copy of the string with 
# uppercase characters converted to lower case, and vice versa

print('a.swapcase()')
print(a.swapcase())  # should return 'ABCDEFG'
print('A.swapcase()')
print(A.swapcase())  # should return 'abcdefg'

# an example of ' casefold ' method. This will return a version of the string suitable
# for caseless comparisons

print('A == a')
print(A == a) #should return as False because A is a string of capital letters, a is all lower case
print('A.casefold() == a.casefold()')
print(A.casefold() == a.casefold())  # should return as True

## an example of ' translate ' and ' maketrans ' methods. It's kind of like cryptography.

print('a.translate(a.maketrans(a,c))')
print(a.translate(a.maketrans(a,c)))  # should return '1234567'


