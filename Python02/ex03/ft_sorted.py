import sys

if(len(sys.argv) > 3):
	sys.argv.pop(0)
	sys.argv = [int(i) for i in sys.argv]
	sort = sorted(sys.argv,reverse=True)
	if(sys.argv == sort):
		print("The inserted sequence is sorted!")
	else:
		print("The inserted sequence is not sorted!")
		print("The correct order is " + str(sort))
else:
	print("Error! You must insert at least 2 numbers")
