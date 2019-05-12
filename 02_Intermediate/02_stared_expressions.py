# script to illustrate *, and **
# expression to unpack a *list, **dict 

# Docs :- https://www.python.org/dev/peps/pep-0448/

def a(*a):
    print(a)
    print(type(a))

b = [1,2,3,4]
a(*b)
a(b)

def c(**k):
    print(k)
    print(type(k))

d = {'a':12, 'b':23}
c(**d)
c(d=d)


def e(a, b=123, *args):
    print(a)
    print(b)
    print(args)

print('')

e(*b, 12, 23)   #intresting
print('')

e('1', '2', *b)
print('')

e(a='1', b='2', *b)     #This is because 
# *args -> is evaluated before **kwargs
