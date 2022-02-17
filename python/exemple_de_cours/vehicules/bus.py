from vehicule import Vehicule


class Bus(Vehicule):

    # Dans notre usage de l'heritage, le nombre de passagers assis,
    # sera represente par le champs "nb_passagers" de la classe mere.
    def __init__(self, roues, portes, places, places_debout):
        Vehicule.__init__(self, roues, portes, places)
        self.nb_places_debout = places_debout
        self.nb_passagers_debouts = 0

    def ajoute_passager_debout(self):
        if self.nb_passagers_debouts +1 > self.nb_places_debout:
            print("Nombre de passagers debouts maximum deja atteind. Cette personne ne peut monter.")
        elif self.nb_passagers_debouts +1 == self.nb_places_debout:
            print("Places debouts remplies. Dernier passager debout a monter a bord.")
            self.nb_passagers_debouts = self.nb_passagers_debouts +1
        else:
            print("Passage ajoute. {} place(s) restante(s).".format(self.nb_places_debout - self.nb_passagers_debouts))
            self.nb_passagers_debouts = self.nb_passagers_debouts +1

    def retire_passager_debout(self):
        self.nb_passagers_debouts = self.nb_passagers_debouts -1

    def compte_passager_debouts(self):
        print("Il y a {} passager(s) debout(s) a bord.".format(self.nb_passagers_debouts))
