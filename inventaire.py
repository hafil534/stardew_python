import pygame 

class Inventaire :

    def __init__(self, taille) :
        #création de l'inventaire avec le nom de l'objet et sa quantité pour chaque slot
        self.inventaire = [[None, 0] for i in range (taille)] 


    # fonction pour ajouter un objet dans l'inventaire
    def ajout_objet (self, objet, quantite):

        for slot in self.inventaire :
            # on parcourt tous les slot jusqu'a ce qu'on trouve un slot avec l'objet recherché et on verifie si il n'est pas plein (64 max)
            if slot[0] == objet and slot[1] < 64 :
                ajout = min(quantite, 64 - slot[1])
                slot[1] += ajout
                quantite -= ajout

            # tous les objets ont ete ajoutes   
                if quantite == 0 :
                    return True

        for slot in self.inventaire :

            #si cette fois le slot est vide on rajoute l'objet
            if slot[0] is None : 
                slot[0] = objet
                slot[1] = min(quantite, 64)
                quantite -= slot[1]

            #on verifie si tout a ete ajoute
                if quantite == 0:
                    return True

            # l'inventaire n'a plus de place
            return False

    # fonction pour retirer un objet dans l'inventaire
    def retirer_objet(self, objet, quantite):
        
        for slot in self.inventaire :
            if slot[0] == objet:

                retrait = min(quantite, slot[1])

                slot[1] -= retrait
                quantite -= retrait

                # on vide le slot car il n'y a plus d'objet
                if slot[1] == 0 :
                    slot[0] = None

                #tous les objets on ete retires
                if quantite == 0 :
                    return True

        return False