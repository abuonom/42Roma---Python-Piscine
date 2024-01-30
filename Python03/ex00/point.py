class Point:
	def __init__(self,x:float,y:float) -> None:
		self.x = x
		self.y = y

def dist_point(a:Point, b: Point)-> float:
	return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5

if __name__ == "__main__":
	x:float
	y:float

	str = input("Insert the coordinates of the first point: ")
	x = float(str[:str.index(',')])
	y = float(str[str.index(',') + 1:])
	a = Point(x,y)
	str = input("Insert the coordinates of the second point: ")
	x = float(str[:str.index(',')])
	y = float(str[str.index(',') + 1:])
	b = Point(x,y)
	print(f"Their distance is: {dist_point(a,b)}")
