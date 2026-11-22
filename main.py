import pygame
from jeu import Jeu
from terrain import Terrain
from plante import Plante

#ouverture de la fenetre pygame
pygame.init()
#renommer la fenetre
pygame.display.set_caption("Stardew Valley")
  #instance jeu
jeu = Jeu()
#taille de l'écran
ecran = pygame.display.set_mode((jeu.largeur, jeu.hauteur))
#image de fond
background = pygame.image.load("assets/background.jpg")
# instance terrain
terr = Terrain(500,500,600,100,"champ")


running = True


while running:
    #ajouter l'image de fond dans l'interface pygame
    ecran.blit(background,(0,0))
    terr.afficher(ecran)
     #ajouter l'image du joueur dans l'interface pygame
    ecran.blit(jeu.joueur.image,jeu.joueur.rect)
    
    


    
     # vérifie ou le jouer veut aller (droite, gauche, haut, bas)
    if jeu.pressed.get(pygame.K_RIGHT) and jeu.joueur.rect.x + jeu.joueur.rect.width <ecran.get_width():
        jeu.joueur.image = jeu.joueur.imagedroit
        jeu.joueur.move_right()
    if jeu.pressed.get(pygame.K_LEFT) and jeu.joueur.rect.x >0:
        jeu.joueur.image = jeu.joueur.imagegauche
        jeu.joueur.move_left()
    if jeu.pressed.get(pygame.K_UP) and jeu.joueur.rect.y > 0 :
        jeu.joueur.move_up()
    if jeu.pressed.get(pygame.K_DOWN) and jeu.joueur.rect.y + jeu.joueur.rect.height < ecran.get_height() :
        jeu.joueur.move_down()

  
    #afficher image de fond
    pygame.display.flip()
    


    for event in pygame.event.get():
           #quitter la fenetre 
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN :
           jeu.pressed[event.key] = True # la touche est active
        elif event.type == pygame.KEYUP : #la touche n'est plus utilisée
            jeu.pressed[event.key] = False

