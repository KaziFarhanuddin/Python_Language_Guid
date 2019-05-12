# This is to show basic declaration of class 

# class Froots:
# class Froots(object):
class Froots():
	"""This is Froots class"""

	def __init__(self, name, color):
		"""This is the constructor/initialization method """
		self.name = name
		self.color = color

	def __del__(self):
		"""This is destructor in python """
		print("Object got destroyed")

apple = Froots('Apple', 'red')
	
print(apple.name,apple.color)

print(apple.__doc__)
print(apple.__init__.__doc__)

# print(dir(mango))
# help(apple.__init__)
# del apple
