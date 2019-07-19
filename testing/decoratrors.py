def deco(aa):
	def other(func):
		def ss():
			print(func())
		return ss

	return other

@deco('a')
def kk():
	return "aa"

kk()