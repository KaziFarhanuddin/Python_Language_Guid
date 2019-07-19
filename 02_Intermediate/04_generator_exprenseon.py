''' This is to show generator expressions in python'''
''' 
	Generators also make their own name space so you cant 
		acess last value of i outside it
'''

LIST = [10, 40, 2, 18, 30, 50, 5, 15]


def div_by_five(nu):
    '''Finds if no divisible by 5'''
    if nu % 5 == 0:
        return True
    else:
        return False


# Generator exprenseon
NUMBERS = (i for i in LIST if div_by_five(i))
print(NUMBERS, end='\n\n')
for i in NUMBERS:
    print(i)

print()

# Double
NUMBERS = ((print(x, y) for x in range(6)) for y in range(6))
for i in NUMBERS:
    for ii in i:
        ii
