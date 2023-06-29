import pygame
from pygame.locals import *
from PIL import Image
import time






'''https://openclassrooms.com/forum/sujet/gerer-les-collisions-avec-pygame
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title('Launcher ')
fenetre.geometry('500x500')
champ_label = Label(fenetre, text="Bienvenue")
bouton_quitter = Button(fenetre, text="Lancer le jeu", command=fenetre.quit)
bouton_quitter.pack()
champ_label.pack()
fenetre.mainloop()
'''
pygame.init()
photo=Image.open("chateau.png")
L,H=photo.size
#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((L, H))
print(L,H)
chute=0

#Chargement et collage du fond
fond = pygame.image.load("chateau.png").convert()
fenetre.blit(fond, (0,0))


perso = pygame.image.load("sprite mario modif 1.png")


perso2 = pygame.image.load("sprite mario modif 2.png")
perso3 = pygame.image.load("sprite mario modif 3.png")
perso4 = pygame.image.load("sprite mario modif 4.png")


position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
pygame.key.set_repeat(400, 30)

while continuer==True:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = False
            pygame.quit()

        if event.type == KEYUP and event.key == K_ESCAPE:
            continuer = False  #On arrête la boucle
            pygame.quit()

        if event.type == KEYDOWN:


            if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
                if chute==0:
                    position_perso = position_perso.move(0,5)
                    fenetre.blit(fond, (0,0))#recollage
                    fenetre.blit(perso, position_perso)
                    #Rafraichissement
                    pygame.display.flip()
                    time.sleep(0.1)





                    position_perso = position_perso.move(0,5)
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso2, position_perso)
                    pygame.display.flip()
                    time.sleep(0.1)

                    position_perso = position_perso.move(0,5)
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso3, position_perso)
                    pygame.display.flip()
                    time.sleep(0.1)

                    position_perso = position_perso.move(0,5)
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso4, position_perso)
                    pygame.display.flip()

                    chute=1

                position_perso = position_perso.move(0,5)
                fenetre.blit(fond, (0,0))
                fenetre.blit(perso4, position_perso)
                pygame.display.flip()

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    chute=0
                    time.sleep(0.1)

                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, position_perso)
                    pygame.display.flip()







                pygame.display.flip()
            if event.key == K_UP:	#Si "flèche bas"
				#On descend le perso
                position_perso = position_perso.move(0,-5)
                fenetre.blit(fond, (0,0))#recollage
                fenetre.blit(perso, position_perso)
                #Rafraichissement
                pygame.display.flip()
            if event.key == K_RIGHT:	#Si "flèche bas"
				#On descend le perso
                position_perso = position_perso.move(5,0)
                fenetre.blit(fond, (0,0))#recollage
                fenetre.blit(perso, position_perso)
                #Rafraichissement
                pygame.display.flip()
            if event.key == K_LEFT:	#Si "flèche bas"
				#On descend le perso
                position_perso = position_perso.move(-5,0)
                fenetre.blit(fond, (0,0))#recollage
                fenetre.blit(perso, position_perso)
                #Rafraichissement
                pygame.display.flip()





















