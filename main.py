import pygame
from jeu import Jeu
from terrain import Terrain
from plante import Plante
from portail import Portail

#ouverture de la fenetre pygame
pygame.init()

marche = Portail(nom_endroit="marche_test",nom_bloc_collision="bloc_collision",portailpos_x=1280//4,portailpos_y=0)



#renommer la fenetre
pygame.display.set_caption("Stardew Valley")
  #instance jeu
jeu = Jeu()
#taille de l'écran
ecran = pygame.display.set_mode((jeu.largeur, jeu.hauteur))
#image de fond
background = pygame.image.load("assets/background.jpg")
# instance terrain
terr = Terrain(847,841,200,0,"champ")
terr.planter(2,2,Plante("carote",10000))
#test 
#bloc_test = pygame.image.load("assets/sprites/terrain/bloc_test_collision.png")
#pos_bloc_test = bloc_test.get_rect()
#pos_bloc_test.x = 0 
#pos_bloc_test.y = 0 


running = True

n = 0 
while running:
    #ajouter l'image de fond dans l'interface pygame
    #ecran.blit(background,(0,0))
    #terr.afficher(ecran)
     #ajouter l'image du joueur dans l'interface pygame
    #ecran.blit(jeu.joueur.image,jeu.joueur.rect)
    
    if n == 0 :      
                                                           # ici on regroupe tout ce qu'il faut afficher dans le monde 0 (monde de depart)
        ecran.blit(background,(0,0))                                    # ecran noir si on l'enleve
        terr.afficher(ecran)                                            # affiche le terrain pour la recolte  , lorsqu'on l'enleve le personnage va tres vite
        marche.afficher_portail(ecran)                                  # affiche le bloc portail                                  
        ecran.blit(jeu.joueur.image,jeu.joueur.rect)                    # affiche le personnage 
        # factoriser,liste 
        if jeu.pressed.get(pygame.K_p):
            terr.planter(caseperso_x,caseperso_y,Plante("carote",10000))   # permet de planter avec la touche p

        if marche.collision(jeu.joueur.rect) : 
            n = 1
            jeu.joueur.rect.x,jeu.joueur.rect.y =  1280//4 ,320

    if n == 1 : 
        marche.afficher_endroit(ecran=ecran)
        ecran.blit(jeu.joueur.image,jeu.joueur.rect)
        if jeu.pressed.get(pygame.K_r):
            n = 0 
            jeu.joueur.rect.x,jeu.joueur.rect.y =  50,320
            # rafraichissement,synchroniser les mondes, ralentir le jeu pour que ce soit plus agreable , rien ne le ralenti . 
        #ecran.blit(marche.bloc_marche, marche.pos_bloc_marche)          # affiche l'endroit referencant le marche
        #marche.afficher_endroit(ecran=ecran)






    #ecran.blit(bloc_test, pos_bloc_test)
    caseperso_x =( jeu.joueur.rect.centerx - terr.posx) // terr.PXCASE
    caseperso_y = (jeu.joueur.rect.centery - terr.posy) // terr.PXCASE
    # faire grandir les plantes 
    for y in range(terr.nbcasesLong):
        for x in range(terr.nbcasesLarg):
            if terr.grid[y][x]["plante"] is not None:
                terr.grid[y][x]["plante"].croissance()

    

    
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
        # planter avec la touche p
    if jeu.pressed.get(pygame.K_p):
        terr.planter(caseperso_x,caseperso_y,Plante("carote",10000))
    if (jeu.pressed.get(pygame.K_r)
    and caseperso_x < terr.nbcasesLarg and caseperso_y < terr.nbcasesLong):
        if (terr.grid[caseperso_y][caseperso_x]["plante"] is not None
            and terr.grid[caseperso_y][caseperso_x]["plante"].plantepret()):
                terr.retireplante(caseperso_x,caseperso_y)

    
    #if jeu.joueur.rect.colliderect(pos_bloc_test) :
     #   pygame.quit()   

  
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

