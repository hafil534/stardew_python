import pygame


class Joueur(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/joueur/persodroite.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.imagedroit = pygame.transform.scale(pygame.image.load("assets/sprites/joueur/persodroite.png"), (50, 50))
        self.imagegauche = pygame.transform.scale(pygame.image.load("assets/sprites/joueur/persogauche.png"), (50, 50))
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


    def procheplante (self,terrain):
        #case du terrain sur lequel le perso se trouve
        caseperso_x =( self.rect.centerx - terrain.posx) // terrain.PXCASE
        caseperso_y = (self.rect.centery - terrain.posy) // terrain.PXCASE
        # le perso peut detecter les plante qui se trouve jusqu'a une case après lui
        for y in range(caseperso_y - 1,caseperso_y + 2):
            for x in range(caseperso_x - 1,caseperso_x + 2):
                if 0 <= x <terrain.nbcasesLarg and 0 <= y < terrain.nbcasesLong:
                    if terrain.grid[y][x]["plante"] is not None:
                             return True
        return False
                        
