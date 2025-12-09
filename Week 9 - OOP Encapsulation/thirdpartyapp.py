from rectangle import Rectangle

r = Rectangle()
p = Rectangle(1, 1, 2, 3)
p.width = 3
p.length = 5
print(f"\n \n R: ({r.x}, {r.y}, {r.width}, {r.length}), area = {r.area()}")
print(f" P: ({p.x}, {p.x}, {p.width}, {p.length}), area = {p.area()}\n\n")

