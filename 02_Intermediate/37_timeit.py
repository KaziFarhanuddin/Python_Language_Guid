'''This is to show timit which can be used to bench mark other scripts or programs'''
import timeit
# timeit dosent have acess to variables outside of it
#	Cant use a list defined outside timeit inside the code in timeit

print(timeit.timeit('''
xyz = (i for i in range(100) if i%5==0)
''', number=1000))


print(timeit.timeit('''
xyz = [i for i in range(100) if i%5==0]
''', number=1000))

# xyz = [i for i in range(100) if i%5==0]
