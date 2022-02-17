from vehicule import Vehicule


class VoitureSansPermis(Vehicule):

    nb_roues = 4
    nb_portes = 2
    nb_places = 2


    def __init__(self):
        self.nb_passagers = 0
