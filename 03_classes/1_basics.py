# class Froots:
# class Froots(object):
class Froots():
	""" Docs go hear """
	def __init__(self, name, color):
		self.name = name
		self.color = color

apple = Froots('Apple', 'red')
mango = Froots('Mango', 'yellow')
	
print(apple.name,apple.color)
print(mango.name,mango.color)
print(mango.__doc__)
print(dir(mango))