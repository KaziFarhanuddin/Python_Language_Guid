'''This is a python program to illustrate functions inpython'''

def main(i):
    '''This is asimple function in which we are raising errors'''

    if i == 0:
    	raise Exception("Cant use 0")
    elif i == 10:
    	raise ValueError("Cant use 10")

    print(i)


I = int(input("Enter a number : "))

main(I)
