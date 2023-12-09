#Imports
import metadata
import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

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
    settings_background = pygame.transform.scale(pygame.image.load('assets/settings/settings_background.jpg'), screen.get_size()) 
    
    #Load images
    boy_notpressed_button_img = pygame.transform.scale(pygame.image.load('assets/settings/boy_notpressed.png'), (200, 200)) 
    girl_notpressed_button_img = pygame.transform.scale(pygame.image.load('assets/settings/girl_notpressed.png'), (200, 200)) 
    boy_pressed_button_img = pygame.transform.scale(pygame.image.load('assets/settings/boy_pressed.png'), (200, 200)) 
    girl_pressed_button_img = pygame.transform.scale(pygame.image.load('assets/settings/girl_pressed.png'), (200, 200)) 
    
    main_menu_button_img = pygame.transform.scale(pygame.image.load('assets/settings/back_main_menu_button.png'), (350, 50)) 
    
    #Set sliders and outputs
    music_slider = Slider(screen, 250, 330, 700, 40, min=0, max=100, step=1, initial = metadata.MUSIC_VOLUME)
    music_output = TextBox(screen, 875, 410, 60, 50, fontSize=30)
    music_output.disable()

    difficulty_slider = Slider(screen, 250, 510, 700, 40, min=1, max=5, step=1, initial = (6 - metadata.GAMES_DIFFICULTY))
    difficulty_output = TextBox(screen, 805, 590, 60, 50, fontSize=30)
    difficulty_output.disable()
    
    while True:
        # First background 
        screen.blit(settings_background, (0,0))
        main_menu_button = screen.blit(main_menu_button_img, (425, 700))
        
        #Set buttons
        if metadata.PLAYER_GENDER == 'boy': 
            boy_button = screen.blit(boy_pressed_button_img, (350, 50))
            girl_button = screen.blit(girl_notpressed_button_img, (650, 50))
        else: 
            boy_button = screen.blit(boy_notpressed_button_img, (350, 50))
            girl_button = screen.blit(girl_pressed_button_img, (650, 50))
            
        #Update Textboxes
        music_output.setText(music_slider.getValue())
        metadata.update('MUSIC_VOLUME', music_slider.getValue())
        
        difficulty_output.setText(difficulty_slider.getValue())
        metadata.update('GAMES_DIFFICULTY', 6 - difficulty_slider.getValue())

        #Cycles through all events occurring  
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                if boy_button.collidepoint(x, y):
                    metadata.update('PLAYER_GENDER', 'boy')
                    
                elif girl_button.collidepoint(x,y):
                    metadata.update('PLAYER_GENDER', 'girl')
                    
                elif main_menu_button.collidepoint(x, y):
                    import main
                    main.main()    
            elif event.type == pygame.QUIT:
                pass            
        
        pygame_widgets.update(events)
        pygame.display.update()
        FramePerSec.tick(FPS)
    
main()