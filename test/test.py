import pygame
from pygame.locals import *
from PIL import Image
import time
import random
photo=Image.open("chateau.png")
L,H=photo.size
#Ouverture de la fenêtre Pygame
pygame.init()
fenetre = pygame.display.set_mode((L, H))
randx=L
randy=H//2
chute=0
x=0
cercle=1

#Chargement et collage du fond

fond = pygame.image.load("chateau.png").convert()
fenetre.blit(fond, (x,0))

perso = pygame.image.load("sprite mario 1.png")
perso2 = pygame.image.load("sprite mario 2.png")
perso3 = pygame.image.load("sprite mario 3.png")
perso4 = pygame.image.load("sprite mario 4.png")

fenetre.blit(perso, (10,H//2))

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
            x=0
            pygame.quit()

        if event.type == KEYUP and event.key == K_ESCAPE:
            continuer = False  #On arrête la boucle
            pygame.quit()

        if event.type == KEYDOWN:


            if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
                if chute==0:
                    position_perso = position_perso.move(0,5)
                    fenetre.blit(fond, (x,0))
                    #recollage
                    fenetre.blit(perso, position_perso)
                    #Rafraichissement
                    pygame.display.flip()
                    time.sleep(0.1)

                    position_perso = position_perso.move(0,5)
                    fenetre.blit(fond, (x,0))
                    fenetre.blit(perso2, position_perso)
                    pygame.display.flip()
                    time.sleep(0.1)

                    position_perso = position_perso.move(0,5)
                    fenetre.blit(fond, (x,0))
                    fenetre.blit(perso3, position_perso)
                    pygame.display.flip()
                    time.sleep(0.1)

                    position_perso = position_perso.move(0,2)
                    fenetre.blit(fond, (x,0))
                    fenetre.blit(perso4, position_perso)
                    pygame.display.flip()

                    chute=1






                position_perso = position_perso.move(0,5)
                fenetre.blit(fond, (x,0))
                fenetre.blit(perso4, position_perso)
                pygame.display.flip()








            if event.key == K_UP:	#Si "flèche bas"
				#On descend le perso
                position_perso = position_perso.move(0,-5)
                fenetre.blit(fond, (x,0))
                #recollage
                fenetre.blit(perso, position_perso)
                #Rafraichissement
                pygame.display.flip()

        if event.type == KEYUP:
            if event.key == K_DOWN:
                chute=0
                fenetre.blit(fond, (x,0))


                fenetre.blit(perso, position_perso)
                pygame.display.flip()

    #mouvement fenetre

    fenetre.blit(fond, (x,0))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()







    #mouvement cercle aléatoire
    if cercle==0:
        randy=random.randint(1,H)

    fenetre.blit(fond, (x,0))

    pygame.draw.circle(fenetre, (255,0,0), (randx,randy), 30)
    cercle=1
    pygame.display.flip()

    if cercle==1:
        randx=randx-5
    if randx==1:
        randx=L
        cercle=0




























