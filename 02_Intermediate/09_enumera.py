'''
	This is to show enumerate 
		It allows us to iterate over a list and also get the index at the same time
'''

LIST = [i for i in range(100)]
for i in range(len(LIST)):
    print(LIST[i], i)

LIST = [i for i in range(100)]
for j, i in enumerate(LIST):
    print(j, i)
