import time

class Personnage:
    def __init__(self, nom, lieu, argent):
        self.nom = nom
        self.lieu = lieu
        self.argent = argent
        self.main_droite = []
        self.main_gauche = []

    def se_deplacer(self, lieu):
        self.lieu = lieu
        print(f"{self.nom} est actuellement à la {self.lieu}")

    def payer_article(self, article):
        if self.argent >= article.prix:
            self.argent -= article.prix
            print(f"{self.nom} a payé {article.prix} euros pour {article.nom}. Argent restant {self.argent} euros")
            return True
        else:
            print(f"{self.nom} n'a pas assez d'argent pour acheter {article.nom}.")
            return False

    def couper(self, ingredient, outil):
        if 'entier' in ingredient.etats and outil.action == 'coupé':
            ingredient.etats.remove('entier')
            ingredient.etats.append('coupé')
            print(f"{self.nom} a coupé {ingredient.nom} avec un {outil.nom}")

class Lieu:
    def __init__(self, nom):
        self.nom = nom
        self.personnes = []

class Outil:
    def __init__(self, nom, action='entier'):
        self.nom = nom
        self.action = action

class Ingrédient:
    def __init__(self, nom, etats, prix):
        self.nom = nom
        self.etats = etats
        self.prix = prix

class Épicerie(Lieu):
    def __init__(self, nom):
        super().__init__(nom)
        self.paniers = []
        self.ingrédients = [Ingrédient('œufs', ['entier'], 1.0),
                            Ingrédient('lait', ['entier'], 0.5),
                            Ingrédient('sel', ['entier'], 0.2),
                            Ingrédient('poivre', ['entier'], 0.3)]

class Panier:
    def __init__(self, type):
        self.type = type
        self.contenu = []

class Poêle:
    def __init__(self):
        self.contenu = []

    def cuire(self):
        time.sleep(4)
        self.contenu[0].etats = ['cuit']
        print("L'omelette est cuite :)")

class Bol:
    def __init__(self):
        self.contenu = []

    def melanger(self, nom_melange):
        new_melange = Ingrédient(nom_melange, ['pas cuit'], 0)
        self.contenu = [new_melange]
        print(f"{self.contenu[0].nom} ")


personnage = Personnage("Adil", "maison", 10.0)
maison = Lieu("maison")
epicerie = Épicerie("épicerie")
outil_couteau = Outil("couteau", action='coupé')
poêle = Poêle()
bol = Bol()


personnage.se_deplacer(maison.nom)


personnage.se_deplacer(epicerie.nom)
print(f"{personnage.nom} a pris un panier")


for ingredient in epicerie.ingrédients:
    panier = Panier('panier')
    panier.contenu.append(ingredient)
    personnage.main_droite.append(panier)
    print(f"{personnage.nom} a pris {ingredient.nom} dans le panier.")
    if not personnage.payer_article(ingredient):
        break


personnage.se_deplacer(maison.nom)


for panier in personnage.main_droite:
    for ingredient in panier.contenu:
        print(f"{personnage.nom} met {ingredient.nom} dans le bol.")
        bol.contenu.append(ingredient)
    personnage.main_droite.remove(panier)


personnage.se_deplacer(epicerie.nom)
panier = personnage.main_droite[0]
personnage.main_droite.remove(panier)
epicerie.paniers.append(panier)
print(f"{personnage.nom} a rapporté le panier à l'épicerie.")


personnage.se_deplacer(maison.nom)


for ingredient in bol.contenu:
    if 'entier' in ingredient.etats:
        personnage.couper(ingredient, outil_couteau)


bol.melanger('omelette')

poêle.contenu = bol.contenu
bol.contenu = []
print(f"{personnage.nom} a versé le contenu du bol dans la poêle.")

poêle.cuire()

print("Notre omelette est cuite :)")

