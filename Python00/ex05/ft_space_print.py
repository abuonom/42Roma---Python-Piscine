string = input("Insert a string: ")
if(len(string) == 20):
	print(string)
elif(len(string) > 20):
	print(string[len(string) - 20:])
else:
	print(" " * (20 - len(string)) + string)
