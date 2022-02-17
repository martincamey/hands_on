class Vehicule:

    def __init__(self, roues, portes, places):
        self.nb_roues = roues
        self.nb_portes = portes
        self.nb_places = places
        self.nb_passagers = 0

    def ajoute_passager(self):
        if self.nb_passagers +1 > self.nb_places:
            print("Nombre de passagers maximum deja atteind. Cette personne ne peut monter.")
        elif self.nb_passagers +1 == self.nb_places:
            print("Vehicule plein. Dernier passager a monter a bord.")
            self.nb_passagers = self.nb_passagers +1
        else:
            print("Passage ajoute. {} place(s) restante(s).".format(self.nb_places - self.nb_passagers))
            self.nb_passagers = self.nb_passagers +1

    def retire_passager(self):
        self.nb_passagers = self.nb_passagers -1

    def compte_passager(self):
        print("Il y a {} passager(s) a bord.".format(self.nb_passagers))
