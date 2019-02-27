'''Comparing listcomprehension and generator expressions'''

#This is List comprehension []
XYZ = [x for x in  range(5)]
print(XYZ)

#Range is a generator exprenseon ()
#This is a generator that means it dosent store anything 
#	in memory so its faster to create but slower to iterate
XYZ = (x for x in  range(5))
print(XYZ)

for i in XYZ:
	print(i)

