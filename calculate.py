import argparse
import math_lib as math

if __name__ == '__main__':
	#argparse stuff, get args
	parser = argparse.ArgumentParser(description = "add and divide")

	parser.add_argument('--intadd1',
						type = int,
						help = 'first integer to be added',
						required = True)
	parser.add_argument('--intadd2',
						type = int,
						help = 'second integer to be added',
						required = True)
	parser.add_argument('--numerator',
						type = int,
						help = 'numerator',
						required = True)
	parser.add_argument('--denominator',
						type = int,
						help = 'denominator',
						required = True)
	args = parser.parse_args()

	print(args.intadd1 + " + " + args.intadd2 + " = " + math.add(args.intadd1,args.intadd2))
	print(args.numerator + "/" + args.denominator + " = " math.div(args.numerator, args.denominator))

