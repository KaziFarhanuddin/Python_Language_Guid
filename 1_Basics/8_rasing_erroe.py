def main(i):
	if i == 0:
		raise Exception("Cant use 0")
	elif i==10:
		raise ValueError("Cant use 10")
	print(i)
	
i = int(input("Enter a number : "))
main(i)