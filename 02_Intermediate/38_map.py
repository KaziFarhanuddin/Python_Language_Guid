'''This is to illustrate how to us e map function in python'''

'''
	map : (function, *iterrable)

Makes an iterrator that computes the function using arguments from each of the iterrables. 
Stop when the shotest iterable is exhausted
'''

a  = [1, 2, 3, 4, 5]
b  = [3, 5, 7, 34, 34]
c  = [32, 32, 21, 114, 335]

def add(a, b, c):
	return a+b+c

d = map(add, a, b, c)

print(d)
[print(x) for x in d]
