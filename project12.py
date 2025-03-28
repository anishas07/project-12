#class square
class square:
    def __init__(self,side):
        self.side = side

    def area(self):
        print("My area is:", self.side**2)

#class circle
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("My area is:", 3.14*self.radius)

#class rectangle
class rectangle:
    def __init__(self,side):
        self.side = side
    def area(self):
        print("My area is:", self.side**2)

#class triangle 
class triangle:
    def __init__(self,base, height):
        self.base = base
        self.height = height
    def area(self):
        print("My area is:", 1*self.base*self.height)


osquare = square(5)
ocircle = circle(5)
orectangle = rectangle(5)
otriangle = triangle(5,5)

for shape in (osquare, ocircle, orectangle, otriangle):
    shape.area()


