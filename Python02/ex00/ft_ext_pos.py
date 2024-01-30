import sys
try:
	lista = sys.argv
	lista.pop(0)
	min = 0
	max = 0
	for i in range(len(lista)):
		if int(lista[i]) <= int(lista[min]):
			min = i
		elif int(lista[i]) >= int(lista[max]):
			max = i
	print("The min is " + str(lista[min]) + " and its position is " + str(min) + "\nThe max is " + str(lista[max]) + " and its position is " + str(max))
except:
	print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
