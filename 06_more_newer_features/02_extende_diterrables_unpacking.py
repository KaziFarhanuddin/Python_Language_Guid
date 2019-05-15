
# 1
def func(a, *b):
	print(a)
	print(b)

a = [1,2,23,35,6,64]
func(*a)

print()

# 2
a, *b = 'asd',2,3,33,435
print(a)
print(b)