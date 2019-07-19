# import timeit

# print(timeit.timeit('''
# import numpy as np
# my_array = np.arange(50)
# my_array**2
# 	'''))

# print(timeit.timeit('''
# my_list = list(range(50))
# [i**2 for i in my_list]
# 	'''
# 	))

import numpy as np

import numpy as np
my_array = np.arange(50)
print(my_array.ndim)	#Dimenstion
print(my_array.shape)	# rows, cols, ..
print(my_array.dtype)	# Datatype

oth_arr = np.array(['a', 'b', 'c'])
print(oth_arr.ndim)	#Dimenstion
print(oth_arr.shape)	# rows, cols, ..
print(oth_arr.dtype)	# Datatype


# np.lookfor('linspace')	#Search for feature