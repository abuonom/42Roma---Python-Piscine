try:
	with open("words.txt") as file:
		words = [word.strip() for word in file.readlines()]
	words.sort()
	num = int(input("Insert an integer: "))
	print(f"The words longer than {num} have been written on \"long_words.txt\"")
	with open("longs_word.txt","w") as file_write:
		for word in words:
			if(len(word) > num):
				file_write.write(word + '\n')
except OSError:
	print("Errore apertura file")
