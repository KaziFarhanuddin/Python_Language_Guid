class Human():
	def __init__(self, name):
		self.name = name
		

class Indian(Human):
	def __init__(self, name, age):
		Human.__init__(self, name)
		self.age = age

	def hindi(self):
		print("HAHAHA")

you =Indian('me', 12)
you.hindi()
print(you.name)
print(you.age)


class Chienese(Human):
	def __init__(self, name, age):
		super().__init__(name)
		self.age = age

	def chinese(self):
		print("AAAAAAAA")

chi =Chienese('lee', 12)
chi.chinese()
print(chi.name)
print(chi.age)
