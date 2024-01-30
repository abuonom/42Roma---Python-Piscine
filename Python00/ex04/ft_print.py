string = input("Insert a string: ")
integer = int(input("Insert an integer: "))
if(abs(integer) >= len(string)):
	print("Error: index out of range")
else:
	print(string[integer:-integer + 1])
