class Fighter():
	def __init__(self, name):
		self.name = name
		self.health = 100

	def Attack(self, other):
		other.health -= 10

class WWE(Fighter):
	def Attack(self, other):
		other.health -= 5

class UFC(Fighter):
	def Attack(self, other):
		other.health -= 20

danyal = UFC('Danyal')
noman = WWE('Noman')

print(danyal.health) 
print(noman.health)

danyal.Attack(noman)
noman.Attack(danyal)
print('\nAfter attack', end='\n\n')

print(danyal.health) 
print(noman.health)
