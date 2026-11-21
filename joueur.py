import pygame


class Joueur(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/joueur/marioperso.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100
        

    # modifier les coordonnée donc déplacer le joueur
    def move_right(self):
        self.rect.x += 1

    def move_left(self):
        self.rect.x -= 1

    def move_up(self):
        self.rect.y -= 1

    def move_down(self):
        self.rect.y += 1