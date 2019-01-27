class human():
	className = 'human'	#Class Variable

	def __init__(self, name):
		self.name = name #Instance Variable
		
someone = human('someone')
anyone = human('anyone')

print(someone.className+' - '+someone.name)
print(anyone.className+' - '+anyone.name)

# someone.className = "Asian"
someone.name = "jom"
print(someone.className+' - '+someone.name)
print(anyone.className+' - '+anyone.name)

human.className = 'Indian'
print(someone.className+' - '+someone.name)
print(anyone.className+' - '+anyone.name)
