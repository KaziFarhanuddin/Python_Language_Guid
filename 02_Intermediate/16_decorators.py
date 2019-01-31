from functools import wraps
#if we dont use functools then the function . __name__ will give new on gift


def add_style(style):
	def add_wrapper(itm):
		@wraps(itm)		#From functools to avod overwriting of __name__
		def new():
			return f"A {style} raped up box of {itm()}"
		return new
	return add_wrapper

# def add_wrapper():
# 	@wraps(itm)		#From functools to avod overwriting of __name__
# 	def new():
# 		return f"A raped up box of {itm()}"
# 	return new


@add_style('beautifullt')
@add_style('horribally')
def gift():
	return "GTX 2080 Ti"

print(gift())
print(gift.__name__)	
