import pygame
import configs

def main():
    
    #init pygame
    pygame.init()
    
    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    '''
    pygame.display.set_icon(icon)
    pygame.display.set_caption(title)
    '''
    
    #run loop
    running = True
    
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
    
        screen.fill("green")
        
        pygame.display.flip()
        clock.tick(configs.FPS)


if __name__ == "__main__":
    main()
