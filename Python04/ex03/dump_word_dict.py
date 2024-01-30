import pickle

try:
	dictonary = {}
	with open("words.txt") as file:
		for line in file.readline():
			dictonary[len[line]] = dictonary.get(len[line],0) + 1
	with open('word_count.pickle', 'wb') as filepickle:
		pickle.dump(dictonary,filepickle)
except OSError:
	print("Errore apertura file")




