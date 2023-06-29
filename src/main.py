import pygame
from pygame.locals import *
from PIL import Image


def main():
    image = Image.open("./Images/ciel.png")
    L,H = image.size

    #init pygame
    pygame.init()

    
    icon = pygame.image.load("./Images/missile_mario.png")
    

    fond = pygame.image.load("./Images/ciel.png")
    
    
    fenetre = pygame.display.set_mode((L,H))

    pygame.display.set_icon(icon)
    
    pygame.display.set_caption("Rocket Madness")
    
    fenetre.blit(fond, (0,0))

    pygame.display.flip()


    pygame.key.set_repeat(400, 30)

    #run loop
    run = True
    while run == True:

        for event in pygame.event.get():

            if event.type == QUIT:
                run = False
                pygame.quit()




if __name__ == "__main__":
    main()
