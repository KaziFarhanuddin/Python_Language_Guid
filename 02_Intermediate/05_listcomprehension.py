''' This script is to practice List comprehension '''

#for
[print(x) for x in range(6)]
print()

#Alse works with if
[print(i) for i in range(20) if i%5 == 0]
print()

#Double
[[print(x, y) for x in range(6)] for y in range(6)]