class Aliens():
	def __init__(self, name):
		self.name = name

Venom = Aliens('Venom')
Venom.host = 'Someone'
print(Venom.name)
print(Venom.host)