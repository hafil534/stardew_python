import pygame

class Terrain:
    PXCASE = 50  #taille case en px 

    def __init__(self, largeur, longeur, posx, posy,spritename):
    	#dimentions et norbre de cases dans la grille
        self.posx = posx
        self.posy = posy    
        self.largeur = largeur 
        self.longeur = longeur
        self.nbcasesLarg = largeur // self.PXCASE
        self.nbcasesLong = longeur // self.PXCASE
        self.sprite = pygame.image.load(f'assets/sprites/terrain/{spritename}.png')
        self.grid = [
            [
                {
                    "plante": None,
                }
                for x in range(self.nbcasesLarg)
            ]
            for y in range(self.nbcasesLong)
        ]
    
    def planter(self, x, y, plante):
        if 0 <= x < self.nbcasesLarg and 0 <= y < self.nbcasesLong:
            if self.grid[y][x]["plante"] is None:
                self.grid[y][x]["plante"] = plante
                return True
        return False

    def afficher(self, surface_ecran):
        surface_ecran.blit(self.sprite, (self.posx, self.posy))
        
        for y in range(self.nbcasesLong):
            for x in range(self.nbcasesLarg):
                plante = self.grid[y][x]["plante"]
                if plante is not None:
                    posxP = self.posx + (x * self.PXCASE)
                    posyP = self.posy + (y * self.PXCASE)
                    
                    surface_ecran.blit(plante.image, (posxP, posyP))
