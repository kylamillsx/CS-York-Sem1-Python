class Triangle:
    def __init__(self,corners):
        self.vertices = corners
    def area(self):
        (x1,y1) , (x2,y2),(x3,y3) = self.vertices
        area = 0.5 * abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        return area
t = Triangle([(0,0),(3,0),(0,2)])
print(t.area())
