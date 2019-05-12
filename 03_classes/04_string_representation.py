# String representation of class

class Student():

	def __init__(self, name, age):
		self.name = name
		self.age = age 

	def __str__(self): #Dander method
		return f'{self.name} : {self.age}'

someone = Student('someone',21)

print(someone)