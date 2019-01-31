import argparse
import sys 

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x', type=float, default=1.0, help="Value of x")
	parser.add_argument('--y', type=float, default=1.0, help="Value of y")
	parser.add_argument('--o', type=str, default='add', help="What to perform")

	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))

def calc(args):
	o = args.o
	x = args.x
	y = args.y
	if o == 'add':
		return x+y
	elif o=='sub':
		return x-y
	elif o=='mul':
		return x*y
	elif o=='div':
		return x/y 

if __name__ == '__main__':
	main()