import pygame 
from jeu import Jeu

class Portail() : 



    def __init__(self,nom_endroit,nom_bloc_collision,portailpos_x,portailpos_y):
        #test 
        self.endroit_image = pygame.image.load(f"assets/sprites/carte/{nom_endroit}.jpg")  # photo marche
        self.image_bloc_endroit = pygame.image.load(f"assets/sprites/terrain/{nom_bloc_collision}.png") # photo bloc pour collision futur
        self.image_bloc_endroit = pygame.transform.scale(self.image_bloc_endroit,(50,50))
        self.portailpos = self.image_bloc_endroit.get_rect() # position du bloc de collision
        self.portailpos.x = portailpos_x
        self.portailpos.y = portailpos_y


        #self.pos_bloc_endroit = self.endroit_image.get_rect()
        #self.pos_bloc_endroit.x =  pos_x #1280//4 
        #self.pos_bloc_endroit.y = pos_y

    def afficher_endroit(self, ecran):
            ecran.blit(self.endroit_image, (0,0))    

    def afficher_portail(self,ecran): 
            ecran.blit(self.image_bloc_endroit,self.portailpos )        
        
        #self.pos_bloc_marche.rect.colliderect(other) :
    def collision(self,other) :  
        if self.portailpos.colliderect(other) :
            return True 
        return False   