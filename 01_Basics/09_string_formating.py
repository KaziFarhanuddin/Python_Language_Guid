'''This script illustrates different types of string formating in python'''

from string import Template

NAME = 'Kazi'
AGE = 21

# Fastest (speed) #Coms with python 3.6 & +
print(f'I am {NAME} and i am {AGE} years old')

# Middle
print('I am %s and i am %s years old' % (NAME, AGE))

# Middle
print('I am {} and i am {} years old'.format(NAME, AGE))

# Slowest
STRING = Template("I am $NAME and i am $AGE years old")
NEWSTRING = STRING.substitute(NAME=NAME, AGE=AGE)
print(NEWSTRING)
