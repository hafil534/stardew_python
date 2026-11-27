import pygame
from joueur import Joueur
from plante import Plante
#création d'une classe jeu
class Jeu :
    def __init__(self):
        self.largeur = 1280
        self.hauteur = 720
        self.is_playing = False
        # générer le joueur
        self.joueur = Joueur()
        #stocker les touches appuyés
        self.pressed = {}
