import concurrent.futures
import time
import os

def main(no):
	time.sleep(1)
	print(f'Thread {os.getpid()} is dooing {no}\n')

if __name__ == '__main__':
	with concurrent.futures.ProcessPoolExecutor() as ex:
		ex.map(main, [1,2,3,4])





