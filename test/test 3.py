import pygame
from pygame.locals import *
from PIL import Image
import time
import random

#initialisation variables
photo=Image.open("fond.png")
L,H=photo.size
#Ouverture de la fenêtre Pygame
pygame.init()
fenetre = pygame.display.set_mode((L*2, H))
randx=L
randy=H//2
chute=0
x=0
cercle=1

#Chargement et collage du fond
fond = pygame.image.load("fond.png").convert()
fenetre.blit(fond, (x,0))

#Chargement et collage du perso
perso = pygame.image.load("sprite mario 1.png")
posx=10
posy=H//2
fenetre.blit(perso, (posx,posy))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = True
pygame.key.set_repeat(400, 30)

while continuer==True:


    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = False
            x=0
            fenetre.blit(fond, (x,0))
            pygame.quit()

        if event.type == KEYUP and event.key == K_ESCAPE:
            continuer = False  #On arrête la boucle
            pygame.quit()

        if event.type == KEYDOWN:


            if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso

                    posy=posy+5
                    fenetre.blit(fond, (x,0))
                    fenetre.blit(fond, (x+L,0))#recollage
                    fenetre.blit(perso, (posx,posy))
                    pygame.draw.circle(fenetre, (255,0,0), (randx,randy), 30)
                    #Rafraichissement
                    pygame.display.flip()








            if event.key == K_UP:	#Si "flèche haut"
				#On monte le perso
                posy=posy-5
                fenetre.blit(fond, (x,0))
                fenetre.blit(fond, (x+L,0))#recollage
                fenetre.blit(perso, (posx,posy))
                pygame.draw.circle(fenetre, (255,0,0), (randx,randy), 30)
                #Rafraichissement
                pygame.display.flip()





    #mouvement cercle aléatoire

    if cercle==0:
        randy=random.randint(0,H)

    fenetre.blit(fond, (x,0))
    fenetre.blit(fond, (x+L,0))
    fenetre.blit(perso, (posx,posy))
    pygame.draw.circle(fenetre, (255,0,0), (randx,randy), 30)
    cercle=1
    pygame.display.flip()
    pygame.time.wait(10)
    if cercle==1:
        randx=randx-10
    if randx==0:
        randx=L
        cercle=0


    #test colision
    if randx-30==posx and randy-30>=posy and randy+30<=posy:
        fenetre.fill((255,0,0))
        pygame.display.flip()
        time.sleep(0.1)
