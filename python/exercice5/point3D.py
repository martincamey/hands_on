from point import Point


class Point3D(Point):

    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def set_z(self, z):
        self.z = z

    def description(self):
        return "X: {} - Y: {} - Z: {}".format(self.x, self.y, self.z)


meilleur_point = Point3D(29, 21, 2021)

print("Point A -> {}".format(meilleur_point.description()))

meilleur_point.set_x(30)
meilleur_point.set_y(22)
meilleur_point.set_z(2022)

print("Nouvelles coordonnees du Point -> {}".format(meilleur_point.description()))
