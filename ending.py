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
    pause_background = pygame.transform.scale(pygame.image.load('assets/ending/ending_background.jpg'), screen.get_size()) 
    
    win_picture = pygame.transform.scale(pygame.image.load('assets/ending/win_picture.jpg'), (800,550))

    #Load images
    quit_button_img = pygame.transform.scale(pygame.image.load('assets/ending/quit_button.png'), (300, 50)) 
    back_to_main_menu_button_img = pygame.transform.scale(pygame.image.load('assets/ending/back_main_menu_button.png'), (300, 50)) 
    
    while True:
        # First background 
        screen.blit(pause_background, (0,0))

        # Set picture winners
        screen.blit(win_picture, (200,100))

        #Set back main menu button
        back_to_main_menu_button = screen.blit(back_to_main_menu_button_img, (250, 700))
        
        #Set continue button
        quit_button = screen.blit(quit_button_img, (650, 700))

        #Cycles through all events occurring  
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_to_main_menu_button.collidepoint(x, y):
                    import main
                    main.main() 
                if quit_button.collidepoint(x,y):
                    pygame.quit()
                    sys.exit()    
            if event.type == QUIT:
                pygame.quit()
                sys.exit()   
        
        pygame.display.update()
        FramePerSec.tick(FPS)
    
main()