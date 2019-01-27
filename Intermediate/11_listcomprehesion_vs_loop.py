# for loop changes value of variable in script
# list comprehension dosent affectany variable in script
x = [1, 2, 3, 4]
y = [5, 6, 0, 10]
z = ['a', 'b', 'c', 'd']

#It will not affect any variable outside it
[print(x,y) for x,y in zip(x,y)]
print('x is ',x)

print('\n')

#It will affect variable with same name outside it
for x,y in zip(x,y):
	print(x,y)
print('x is ',x)

