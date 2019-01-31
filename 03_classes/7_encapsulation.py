print("Not Now encapulated".center(100, '-'))
class Human():
	def __init__(self, name, age):
		if type(age) == int:
			self.age = age
		else:
			raise ValueError("Age needs to be a number")
		self.name = name

farhan = Human('farhan', 19)
farhan.age = 'something'
print(farhan.age)

print("Now encapulated".center(100, '-'))

class Human_New():
	def __init__(self, name, age):
		if type(age) == int:
			self.__age = age
		else:
			raise ValueError("Age needs to be a number")
		self.name = name

	def set_age(self, age):
		if type(age) == int:
			self.__age = age
		else:
			raise ValueError("Age needs to be a number")

	def get_age(self):
		return self.__age

kazi = Human_New('kazi' ,12)
kazi.__age = 'someone'
print(kazi.get_age())

