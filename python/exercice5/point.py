class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def description(self):
        return "Abscisse : {} - Ordonnee : {}".format(self.x, self.y)
