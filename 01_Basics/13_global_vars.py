# This script illustrates how to use global variables in python

a = 10 

def add():
	global a
	a += 1

add()
print(a)

# In Python a global variable is always limited to the module
# Global variables are considered a bad practice because
#	 functions can have non-obvious behavior