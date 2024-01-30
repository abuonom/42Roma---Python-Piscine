import sys

if(len(sys.argv) >= 2):
	dict = {}
	str = sys.argv[1]
	for c in str:
		if c not in dict:
			dict[c] = 1
		else:
			dict[c] += 1
	dict_sorted = list(dict.items())
	dict_sorted.sort()
	print("Char count:")
	dict = {k: v for k, v in dict_sorted} #si legge come coppia chiave:valore per k,v contenute in dict_sorted
	for i in dict:
		print(f"{i} = {dict[i]}")
else:
	print("Error! No string given")


