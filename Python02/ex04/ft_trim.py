import sys
def trim(list:list):
	list.pop(0)
	list.pop()

if __name__ == "__main__":
	if(len(sys.argv) > 3):
		sys.argv.pop(0)
		trim(sys.argv)
		print(f"The new list is: {sys.argv}")
	else:
		print("Error! You must insert at least 2 values")
