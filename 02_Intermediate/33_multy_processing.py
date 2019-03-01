import multiprocessing

def s(i,j):
	print(f"{i} {j} HELLOW")

if __name__ == '__main__':
	for i in range(0,100):
		p = multiprocessing.Process(target=s, args=(i,i+1))
		p.start() 
		# p.join()