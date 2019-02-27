#This is simply
# file = open('data.txt', 'r')
# print(file.read())

def read(file):
	with open(file, 'r') as fi:
		data = fi.read()
	return data

def write(file):
	info = input("What to write ? \n")
	info += '\n'
	with open(file, 'w') as fi:
		fi.write(info)

def append(file):
	info = input("What to append ? \n")
	info += '\n'
	with open(file, 'a') as fi:
		fi.write(info)

write('data.txt')
print()
append('data.txt')
print()
data = read('data.txt')
print(data)

