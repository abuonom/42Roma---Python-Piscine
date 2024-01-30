import sys
try:
		nome, x, y, z = sys.argv
		if float(x) >= float(y) and float(x) >= float(z):
			print('The max is: ' + str(float(x)))
		elif float(y) >= float(x) and float(y) >= float(z):
			print('The max is: ' + str(float(y)))
		else :
			print('The max is: ' + str(float(z)))
except:
	print("Error! Usage: python3 ft_max.py <x> <y> <z>")
