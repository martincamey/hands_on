class Animal:

    def __init__(self, nom, race, cri, nb_pattes, poids):
        self.nom = nom
        self.race = race
        self.cri = cri
        self.nombre_pattes = nb_pattes
        self.poids = poids

    def mise_a_jour_poids(self, nouveau_poids):
        self.poids = nouveau_poids

    def description(self):
        desc = "{} est un(e) {}. ".format(self.nom, self.race)

        if self.cri:
            desc = desc + "Son cri : '{}'. ".format(self.cri)

        if self.nombre_pattes:
            desc = desc + "Avec {} pattes, ".format(self.nombre_pattes)
        else:
            desc = desc + "Sans patte, "

        desc = desc + "son poids est de {} kg !".format(self.poids)

        return desc
