# Class to calculate the distance and slop of a line
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
# 9.433981132056603
print(li.slope())
# 1.6


# Class to calculate the volume and surface area of a cylinder

class Cylinder:
    # CLASS OBJECT ATTRIBUTES
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        h = self.height
        r = self.radius
        return Cylinder.pi * r * r * h

    def surface_area(self):
        h = self.height
        r = self.radius
        return 2 * Cylinder.pi * r * h + 2 * Cylinder.pi * r * r


# EXAMPLE OUTPUT
c = Cylinder(2, 3)
print(c.volume())
# 56.519999999999996
print(c.surface_area())
# 94.19999999999999
