my_list = [10,40,2,18,30,50,5,15]

def div_by_five(n):
	if n%5 == 0:
		return True
	else:
		return False

#Generator exprenseon
xyz = (i for i in my_list if div_by_five(i))

print(xyz, end='\n\n')
for i in xyz:
	print(i)

print()

#Double
xyz = ((print(x, y) for x in range(6)) for y in range(6))
for i in xyz:
	for ii in i:
		ii 

