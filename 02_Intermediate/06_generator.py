''' 
	This is to illustrate generators in python
	
	Generators dosent store anything in memory so its faster to create 
		but slower to iterate
	Generators also make their own name space so you cant 
		acess last value of i outside it
'''

def simple_gen():
    '''This is a simple generator'''
    print("THis is first")
    yield 'This'
    print("THis is second")

    yield 'is'
    print("THis is Third")

    yield 'a'
    print("THis is Fourth")

    yield 'generator'

for i in simple_gen():
    print(i)
