# This script is to illustrate how to use methods in python

class Fighter():
	"""Hear we write class docs"""
	def __init__(self, helth, attack):
		"""Method docs"""
		self.helth = helth
		self.attack = attack

	def Attack(self, other):
		other.helth -= self.attack

	def Healed(self):
		"""Method docs"""
		self.helth += 5

fighter_1 = Fighter(100, 10)		
fighter_2 = Fighter(80, 15)		

print(fighter_2.helth)

fighter_1.Attack(fighter_2)

print(fighter_2.helth)

fighter_2.Healed()

print(fighter_2.helth)

print(fighter_2.Healed.__doc__)
print(fighter_2.__doc__)