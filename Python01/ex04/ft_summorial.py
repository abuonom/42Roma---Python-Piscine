import sys
if len(sys.argv) == 2:
	n = int(sys.argv[1])
	res: int = 0
	if(n >= 0):
		while n > 0:
			res += n
			n -= 1
		print('The sum is: ' + str(res))
	else:
		print("Error! n must be >=0")
else:
	print("Error! Usage: python3 ft_summorial.py <n>")
