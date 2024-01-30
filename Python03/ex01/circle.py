import sys
class Point:
		def __init__(self,x:float,y:float) -> None:
			self.x = x
			self.y = y

class Circle:
	def __init__(self,center:tuple,radius) -> None:
		self.radius = radius
		self.center = Point(center[0],center[1])
	def __str__(self) -> str:
		return(f"Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}")

if __name__ == "__main__":
	circle = Circle((150,100),75)
	print(circle)
