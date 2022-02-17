from bus import Bus


class BusDouble(Bus):


    # Dans notre usage de l'heritage, le nombre de passagers assis,
    # sera represente par le champs "nb_passagers" de la classe mere.

    # Dans notre usage de l'heritage, le nombre de passagers debouts,
    # Sera represente par le champs "nb_passagers_debouts" de la classe mere.
    def __init__(
        self,
        roues,
        portes,
        places,
        places_debout,
        places_compartiment2,
        places_debout_compartiment2
    ):

        Bus.__init__(self, roues, portes, places, places_debout)
        self.nb_places_compartiment2 = places_compartiment2
        self.nb_places_debout_compartiment2 = places_debout_compartiment2
        self.nb_passagers_c2 = 0
        self.nb_passagers_debouts_c2 = 0

    def ajoute_passager_c2(self):
        if self.nb_passagers_c2 +1 > self.nb_places_compartiment2:
            print("Nombre de passagers maximum deja atteind. Cette personne ne peut monter.")
        elif self.nb_passagers_c2 +1 == self.nb_places_compartiment2:
            print("Vehicule plein. Dernier passager a monter a bord.")
            self.nb_passagers_c2 = self.nb_passagers_c2 +1
        else:
            print("Passage ajoute. {} place(s) restante(s).".format(self.nb_places_compartiment2 - self.nb_passagers_c2))
            self.nb_passagers_c2 = self.nb_passagers_c2 +1

    def retire_passager_c2(self):
        self.nb_passagers_c2 = self.nb_passagers_c2 -1

    def compte_passager_c2(self):
        print("Il y a {} passager(s) a bord dans le compartiement 2.".format(self.nb_passagers_c2))

    def ajoute_passager_debout_c2(self):
        if self.nb_passagers_debouts_c2 +1 > self.nb_places_debout_compartiment2:
            print("Nombre de passagers debouts dans le compartiment 2 maximum deja atteind. Cette personne ne peut monter.")
        elif self.nb_passagers_debouts_c2 +1 == self.nb_places_debout_compartiment2:
            print("Places debouts dans le compartiement 2 remplies. Dernier passager debout a monter a bord.")
            self.nb_passagers_debouts_c2 = self.nb_passagers_debouts_c2 +1
        else:
            print("Passage ajoute. {} place(s) restante(s) dans le compartiement 2.".format(self.nb_places_debout_compartiment2 - self.nb_passagers_debouts_c2))
            self.nb_passagers_debouts_c2 = self.nb_passagers_debouts_c2 +1

    def retire_passager_debout_c2(self):
        self.nb_passagers_debouts_c2 = self.nb_passagers_debouts_c2 -1

    def compte_passager_debouts_c2(self):
        print("Il y a {} passager(s) debout(s) a bord dans le 2e compartiment.".format(self.nb_passagers_debouts_c2))
