'''This is to illustrate how to use argparse to male a cli(command line interphase)'''

import argparse
import sys

def main():
    '''
        This is where we parse all arguments 
        and call other function passing the argument
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Value of x")
    parser.add_argument('--y', type=float, default=1.0, help="Value of y")
    parser.add_argument('--o', type=str, default='add', help="What to perform")

    args = parser.parse_args()
    sys.stdout.write(str(calculate(args)))

def calculate(args):
    ''' This will do arithmatic operation as per the arguments '''
    operation = args.o
    x = args.x
    y = args.y
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y

if __name__ == '__main__':
    main()
