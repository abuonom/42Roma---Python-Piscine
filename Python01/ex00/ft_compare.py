import sys

try:
		num1 = float(sys.argv[1])
		num2 = float(sys.argv[2])
		if num1 > num2:
			print(str(num1) + ' is greather than ' + str(num2))
		if num1 < num2:
			print(str(num1) + ' is less than ' + str(num2))
		if num1 == num2:
			print(str(num1) + ' is equal to ' + str(num2))
except:
	print("Insert two number")

