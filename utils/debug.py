import pygame

pygame.init()
font = pygame.font.Font(None, 20)

def debug(info, y = 10, x = 10):
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, pygame.color.Color("black"))
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(display_surf, pygame.color.Color("black"), debug_rect)
    display_surf.blit(debug_surf, debug_rect)
    