try:
	expression = input('Insert an expression:')
	print('The result is: ' + str(abs(eval(expression))))
except:
	print("Invalid expression")
