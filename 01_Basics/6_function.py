def main(one, two):
	print("For main function : "+str(one+two))
main(1,3)

def default(one, two=10):
	print("For default function : "+str(one+two))
default(2)

def args(*args):
	add = 0 
	for i in args:
		add+=i
	print("For args function : "+str(add))
args(1,2,3)

def kwargs(**kwargs):
	add=0
	for i in kwargs.values():
		add+=i
	print("For kwargs function : "+str(add))
kwargs(a=10,b=20)
