try:
	path = input("Insert file name: ")
	with open(path) as file:
		words = [word.strip() for word in file.readlines()]
	words.sort()
	num = int(input("Insert an integer: "))
	print(f"The words longer than {num} are the following:")
	for word in words:
		if(len(word) > num):
			print(word)
except OSError:
	print("Error! The specified file does not exist!")
