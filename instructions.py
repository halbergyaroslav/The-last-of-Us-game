#Imports
import pygame, sys
from pygame.locals import *
import metadata

#Game Loop
def main():
    #Initialzing 
    pygame.init()
    
    #Setting up FPS 
    FPS = 60
    FramePerSec = pygame.time.Clock()
    
    #Create a white screen 
    screen = pygame.display.set_mode(metadata.SCREEN_SIZE)
    pygame.display.set_caption("The last of Us")
    
    #Create buttons
    start_game_button_img = pygame.transform.scale(pygame.image.load('assets/instructions/start_game_button.png'), (350, 50))
    back_main_menu_button_img = pygame.transform.scale(pygame.image.load('assets/instructions/back_main_menu_button.png'), (350, 50))
    instructions_background_img = pygame.transform.scale(pygame.image.load('assets/instructions/instructions_background.jpg'), screen.get_size())
    
    while True:
        screen.blit(instructions_background_img, (0, 0))
        #pygame.draw.rect(screen, metadata.WHITE, pygame.Rect(200, 50, 800, 600))
        start_game_button = screen.blit(start_game_button_img, (250, 700))
        back_main_menu_button = screen.blit(back_main_menu_button_img, (700, 700))
        
        #Cycles through all events occurring  
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_game_button.collidepoint(x, y):
                    import map2
                    map2.main()  
                elif back_main_menu_button.collidepoint(x, y):
                    import main
                    main.main() 
            
        pygame.display.flip()
        FramePerSec.tick(FPS)
    
main()