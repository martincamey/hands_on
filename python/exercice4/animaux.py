from animal import Animal


class Chien(Animal):

    nombre_pattes = 4 
    cri = "aboiement"

   
    def __init__(self, nom, race, poids, longueur_poil, queue):
        self.nom = nom
        self.race = race
        self.poids = poids
        self.longueur_poil = longueur_poil
        self.longueur_queue = queue

    def description(self):

        desc = "{} Sa queue est {} et son poil est {} !".format(
            super().description(),
            self.longueur_queue,
            self.longueur_poil
        )

        return desc


class Poulet(Animal):

    nombre_pattes = 2
    cri = "piaulement"


    def __init__(self, nom, race, poids, commentaire):
        self.nom = nom
        self.race = race
        self.poids = poids
        self.commentaire = commentaire

    def description(self):
        return "{}, poulet '{}' de {} kg. {}".format(
            self.nom,
            self.race,
            self.poids,
            self.commentaire
        )
