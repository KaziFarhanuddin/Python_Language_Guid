name = 'Kazi'
age = 21

#Fastest (speed) #Coms with python 3.6 & +
print(f'I am {name} and i am {age} years old')

#Middle
print('I am %s and i am %s years old'%(name, age))

#Middle
print('I am {} and i am {} years old'.format(name, age))

#Slowest
from string import Template
string = Template("I am $name and i am $age years old")
NewString = string.substitute(name=name, age=age)
print(NewString)