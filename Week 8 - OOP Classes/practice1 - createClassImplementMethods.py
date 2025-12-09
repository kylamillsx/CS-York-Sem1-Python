class Circle:
    def __init__(self, r, c):
        self.radius = r
        self.center = c
def getArea(rad):
    area = pow(rad.radius,2) * 3.14
    return area
def getPerimeter(rad):
    perimeter = 2 * 3.14 * rad.radius
    return perimeter
circle = Circle(6.0,(0,0))
print(getArea(circle))
print(getPerimeter(circle))