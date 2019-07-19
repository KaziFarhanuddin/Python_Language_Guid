'''
	This is to show zip 
		It will make a generator which over iterating will give tuples containing
		values taken from same indexe.
		If one of the list/tuple is smaller generator will ony be iterated by length 
		of smalles list/tuple.
'''
a = [1, 2, 3, 4]
b = [5, 6, 0, 10]
c = ['a', 'b', 'c', 'd']

for x,y,z in zip(a, b, c):
	print(x,y,z)

print()

for i in zip(a, b, c):
	print(i)

print()

print(list(zip(a, b, c)))

print()

print(dict(zip(a, c)))

print(dict([(1,2), (2,4)]))