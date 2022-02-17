from vehicule import Vehicule


class Voiture(Vehicule):

    nb_roues = 4


    def __init__(self, portes, places):
        Vehicule.__init__(self, self.nb_roues, portes, places)
        self.nb_passagers = 0
