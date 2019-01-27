def simple_gen():
	print("THis is first")
	yield 'oh'
	print("THis is second")

	yield 'hear'
	print("THis is Third")

	yield 'it'
	print("THis is Fourth")

	yield 'is'


# for i in simple_gen():
	# print(i)

##
correct = (3, 6, 1)

# Without
# found = False
# for c1 in range(10):
# 	if found:
# 		break
# 	for c2 in range(10):
# 		if found:
# 			break
# 		for c3 in range(10):
# 			if (c1, c2, c3) == correct:
# 				found = True
# 				print(f'Fund {c1, c2, c3}')
# 				break
# 			print(c1, c2, c3)

#With
def combo_jen():
	for c1 in range(10):
		for c2 in range(10):
			for c3 in range(10):
				yield(c1, c2, c3)

for (c1, c2, c3) in combo_jen():
	print(c1, c2, c3)
	if (c1, c2, c3) == correct:
		print(f'found combo {c1, c2, c3}')
		break



