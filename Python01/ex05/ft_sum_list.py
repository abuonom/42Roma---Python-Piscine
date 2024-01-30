import sys
def sum_list(input_list) -> int:
	res = 0

	for i in input_list:
		res += i
	return res

if __name__ == "__main__":
	lista = []

	while True:
		user_input = input("Insert integer: ")
		if user_input != '0':
			lista.append(int(user_input))
		else:
			print("The sum is: " + str(sum_list(lista)))
			break
