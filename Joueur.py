""""

Joueur

"""

import random
import time
class Joueur():
    def __init__(self, name):
        """
        __init__ (self : instance , name : str) -> None
        créer une instance de la class {Joueur} puis attribut à l'instance {self} les attributs {deck} et {name} qui correspondent respectivement aux cartes en mains et au nom du joueur/Instance
        """
        self._deck = [] #création d'une liste Vide 
        self._name = name 


    def distribuer(self, pioche):
        """
        distribuer (self : instance , pioche : list ) -> None
        Méthode permettant de distribuer au joueur, {self}, ses cartes de départ  
        """
        # distribuer a chcun des joueurs 7 cartes de la pioche une par une
        assert not len(pioche) <= 7, "Il y a trop de joueur" #On verifie qu'il y a suffisemment de carte pour pouvoir en distribuer 7 a tous les joueurs , sinon un message disant "Il y a trop de joueur apparait"
        while len(self._deck) < 7:
            n = random.randint(0, len(pioche) - 1) #utilisation de la méthode randint appartenant a la bibliothèque random pour tirer un numéro aléatoire et donc tirer une carte aléatoire dans la pioche 
            self._deck.append(pioche.pop(n))


    def affichage2(self):
        """
        affichage2 ( self : instance ) -> None
        methode affichant les cartes d'un joueur, {self}
        """
        print(f"Voici , Vos cartes ({self._name}) :")
        print("\n") #permet de faire un saut de 3/4 lignes .
        for i in range(len(self._deck)):
            time.sleep(0.1) #utilisation de la méthode .sleep() de la bibliothèque time . Permettant de créer un temps d'attente de 0.1 secondes entre chaque affichage
            print(f"{i+1} : {self._deck[i]._numero,self._deck[i]._couleur}")


    def trier(self):
        """
        trier(self : instance)-> None
        {trier} est une méthode qui a pour objectif de trier les cartes du joueur {self} par couleur , pour ce faire elle emploie une sous fonction {_trier}
        """
        temp = self._deck.copy() #temp est une copy temporaire de l'instance self
        self._deck.clear() # On supprime le contenu de l'instance self

        def _trier(couleur): #sous fonction évitant de créer a chaque fois un nouveau temp ou de clear self._deck() a chaque tour 
            """
            _trier(couleur : str)-> None
            {_trier} est une sous fonction de la methode {trier} qui a pour objectif de trier par couleur les cartes du joueur {self} . 
            """
            i = 0 #{i} est une variable 
            while len(temp) > 0 and i < len(temp):
                if temp[i]._couleur == couleur:
                    self._deck.append(temp.pop(i))
                    i -= 1
                i += 1

        _trier("Rouge")
        _trier("Bleu")
        _trier("Vert")
        _trier("Jaune")
        _trier("Noir")
        self.affichage2()