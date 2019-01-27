#This is not a generator
#We are using List comprehension []
xyz = [x for x in  range(5)]
print(xyz)

#Range is a generator exprenseon
#This is a generator that means it dosent store anything 
#	in memory so its faster to create but slower to iterate
xyz = (x for x in  range(5))
print(xyz)

for i in xyz:
	print(i)

