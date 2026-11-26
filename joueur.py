import pygame


class Joueur(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/joueur/persodroite.png')
        #self.image = pygame.transform.scale(self.image, (50, 50))
        #self.imagedroit = pygame.transform.scale(pygame.image.load("assets/sprites/joueur/persodroite.png"), (50, 50))
        self.imagedroit = pygame.image.load("assets/sprites/joueur/persodroite.png")
        #self.imagegauche = pygame.transform.scale(pygame.image.load("assets/sprites/joueur/persogauche.png"), (50, 50))
        self.imagegauche = pygame.image.load("assets/sprites/joueur/persogauche.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100
        

    # modifier les coordonnée donc déplacer le joueur
    def move_right(self):
        self.rect.x += 4

    def move_left(self):
        self.rect.x -= 4

    def move_up(self):
        self.rect.y -= 4

    def move_down(self):
        self.rect.y += 4


    
                        
