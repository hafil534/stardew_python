import pygame;

class Plante(pygame.sprite.Sprite):
    ETATS = [ "graine","planteetp2", "plantefinal"]
    def __init__(self,nom,tempspousse):
        super().__init__()
        self.nom = nom
        self.date_plante = pygame.time.get_ticks()
        self.tempsPousse = tempspousse
        
        
        self.images = [
        pygame.transform.scale(
        pygame.image.load(f"assets/sprites/plante/{etat}.png"),
        (50, 50)
    )
    for etat in self.ETATS
]
        self.image = self.images[0]
        
        self.rect = self.image.get_rect()
        self.hauteur = self.image.get_height()
    #faire evoluer la plante
    def croissance(self):
        temps = pygame.time.get_ticks() - self.date_plante
        if temps >= self.tempsPousse :
            self.image = self.images[2]
        elif temps >= self.tempsPousse/2:
            self.image = self.images[1]
        elif temps >= 0:
            self.image = self.images[0]
           
    def plantepret (self):
        return pygame.time.get_ticks() - self.date_plante >= self.tempsPousse
           

    
