import sys
def is_palindrome(str:str) -> bool:
	str_r = str[::-1]
	if(str == str_r):
		return True
	return False

if __name__ == "__main__":
	if(len(sys.argv) == 2):
		if(is_palindrome(sys.argv[1])):
			print("The string "+ sys.argv[1] +" is palindrome")
		else:
			print("The string "+ sys.argv[1] +" is not palindrome")
	else:
		print("Error! Insert just 1 string!")
