import sys
def my_min(x: float = 0,y : float = 0,z :float = 0) -> float:
	if x <= y and x <= z:
		return x
	elif y <= x and y <= z:
		return y
	else :
		return z
if __name__ == "__main__":
	try:
		nome, x, y, z = sys.argv
		x,y,z = float(x),float(y),float(z)
		print(my_min(x,y,z))
	except:
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
