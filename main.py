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
    
    #Create screen 
    screen = pygame.display.set_mode(metadata.SCREEN_SIZE)
    pygame.display.set_caption("The last of Us")
    
    #Create background
    background = pygame.transform.scale(pygame.image.load('assets/main_menu/main_menu_background.jpg'), screen.get_size()) 
    
    #Load images
    start_game_button_img = pygame.transform.scale(pygame.image.load('assets/main_menu/start_game_button.png'), (350, 50))
    quit_game_button_img = pygame.transform.scale(pygame.image.load('assets/main_menu/quit_game_button.png'), (350, 50))
    settings_button_img = pygame.transform.scale(pygame.image.load('assets/main_menu/settings_button.png'), (350, 50))
    
    while True:
        #Show background
        screen.blit(background, (0, 0))
        
        #Set start game button
        start_game_button = screen.blit(start_game_button_img, (120, 500))
        
        #Set options button
        settings_button = screen.blit(settings_button_img, (120, 570))
        
        #Set quit button
        quit_game_button = screen.blit(quit_game_button_img, (120, 640))
        
        #Cycles through all events occurring  
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_game_button.collidepoint(x, y):
                    import instructions
                    instructions.main()
                elif settings_button.collidepoint(x, y):
                    import settings
                    settings.main()
                elif quit_game_button.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()  
            
        pygame.display.update()
        FramePerSec.tick(FPS)
    
main()