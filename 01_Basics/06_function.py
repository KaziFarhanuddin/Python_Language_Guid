'''This is a script to illustrate functions in python'''

def paramater_function(one, two):
    '''This is a function to illustrate a function which takes parameters'''
    print("For main function : "+str(one+two))


paramater_function(1, 3)

def default_value_function(one, two=10):
    '''
    This is a function to illustrate a function which takes parameters
    and also has a default parameter
    '''

    print("For default function : "+str(one+two))


default_value_function(2)


def args_function(*args):
    '''This is a function to illustrate a function which takes many arguments'''

    add = 0
    for i in args:
        add += i
    print("For args function : "+str(add))


args_function(1, 2, 3)


def kwargs_function(**kwargs):
    '''This is a function to illustrate a function which takes key=value pairs'''

    add = 0
    for i in kwargs.values():
        add += i
    print("For kwargs function : "+str(add))


kwargs_function(a=10, b=20)
