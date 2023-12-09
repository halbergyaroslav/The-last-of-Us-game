#Imports
import metadata
import pygame, sys
from pygame.locals import *

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
    
    #Set background
    pause_background = pygame.transform.scale(pygame.image.load('assets/pause/pause_background.jpg'), screen.get_size()) 
    
    #Load images
    continue_button_img = pygame.transform.scale(pygame.image.load('assets/pause/continue_button.png'), (300, 100)) 
    back_main_menu_button_img = pygame.transform.scale(pygame.image.load('assets/pause/back_main_menu_button.png'), (300, 100)) 
    
    while True:
        # First background 
        screen.blit(pause_background, (0,0))
        
        #Set back main menu button
        back_main_menu_button = screen.blit(back_main_menu_button_img, (200, 350))
        
        #Set continue button
        continue_button = screen.blit(continue_button_img, (700, 350))

        #Cycles through all events occurring  
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_main_menu_button.collidepoint(x, y):
                    metadata.clear()
                    import main
                    main.main() 
                if continue_button.collidepoint(x,y):
                    import map2
                    map2.main()  
        
        pygame.display.update()
        FramePerSec.tick(FPS)
    
main()