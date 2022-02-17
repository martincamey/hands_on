from point import Point


point_a = Point(26, 2)
point_b = Point(15, 5)
point_c = Point(18, 6)

print("Point A -> {}".format(point_a.description()))
print("Point B -> {}".format(point_b.description()))
print("Point C -> {}".format(point_c.description()))

point_c.set_x(20)
point_c.set_y(22)

print("Nouvelles coordonnees Point C -> {}".format(point_c.description()))
