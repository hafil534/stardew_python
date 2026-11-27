import pygame


class Lieu():
    def __init__(self, nom_endroit, pos_x, pos_y):
        self.image = pygame.image.load(f"assets/sprites/carte/{nom_endroit}.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def afficher_endroit(self, ecran):
        ecran.blit(self.image, self.rect)
