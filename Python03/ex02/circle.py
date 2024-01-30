import sys

class Point:
	def __init__(self,x:float,y:float) -> None:
		self.x = x
		self.y = y

def dist_point(a:Point, b: Point)-> float:
	return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5

class Circle:
	def __init__(self,center:tuple,radius) -> None:
		self.radius = radius
		self.center = Point(center[0],center[1])
	def __str__(self) -> str:
		return(f"Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}")
	def contains(self,external_point: Point)->bool:
		if dist_point(self.center,external_point) <= self.radius:
			return True
		return False

if __name__ == "__main__":
	circle = Circle((0,0),1)
	point = Point(float(sys.argv[1]),float(sys.argv[2]))
	if circle.contains(point):
		print(f"The Point ({point.x}, {point.y}) lies in the Circle of center ({circle.center.x},{circle.center.y}) and radius {circle.radius}")
	else:
		print(f"The Point ({point.x}, {point.y}) lies out the Circle of center ({circle.center.x},{circle.center.y}) and radius {circle.radius}")
