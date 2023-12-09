#Imports
import pygame, sys, time
from pygame.locals import *
import metadata

#Game Loop
def main():
    marks = {'A': 4.00, 'A-': 3.66, 'B': 3.33, 'B-': 3.00, 'C+': 2.66, 'C': 2.33, 'C-': 2.00, 'D': 1.67, 'E': 1.33}
    
    def flappybird_mark(score):
        if score > 50: return 'A'
        elif score > 45: return 'A-'
        elif score > 40: return 'B+'
        elif score > 35: return 'B'
        elif score > 30: return 'B-'
        elif score > 25: return 'C+'
        elif score > 20: return 'C'
        elif score > 15: return 'C-'
        elif score > 10: return 'D'
        elif score > 5: return 'E'
        else: return 'F'
    
    def pong_mark(score):
        if score < 12: return 'A'
        elif score < 13: return 'A-'
        elif score < 14: return 'B+'
        elif score < 15: return 'B'
        elif score < 16: return 'B-'
        elif score < 17: return 'C+'
        elif score < 18: return 'C'
        elif score < 19: return 'C-'
        elif score < 20: return 'D'
        elif score < 21: return 'E'
        else: return 'F'
    
    def minesweeper_mark(score):
        if score > 499: return 'A'
        elif score > 450: return 'A-'
        elif score > 400: return 'B+'
        elif score > 350: return 'B'
        elif score > 300: return 'B-'
        elif score > 250: return 'C+'
        elif score > 200: return 'C'
        elif score > 150: return 'C-'
        elif score > 100: return 'D'
        elif score > 50: return 'E'
        else: return 'F'
    
    def game_2048_mark(score):
        if score > 5000: return 'A'
        elif score > 4500: return 'A-'
        elif score > 4000: return 'B+'
        elif score > 3500: return 'B'
        elif score > 3000: return 'B-'
        elif score > 2500: return 'C+'
        elif score > 2000: return 'C'
        elif score > 1500: return 'C-'
        elif score > 1000: return 'D'
        elif score > 500: return 'E'
        else: return 'F'
    
    flappybird_score = metadata.FLAPPYBIRD_SCORE
    flappybird_mark_text = flappybird_mark(flappybird_score)
    
    game_2048_score = metadata.GAME_2048_SCORE
    game_2048_mark_text = game_2048_mark(game_2048_score)
        
    minesweeper_score = metadata.MINESWEEPER_SCORE
    minesweeper_mark_text = minesweeper_mark(minesweeper_score)
    
    pong_score = metadata.PONG_SCORE
    pong_mark_text = pong_mark(pong_score)   
    
    if flappybird_mark_text != 'F' and game_2048_mark_text != 'F' and minesweeper_mark_text != 'F' and pong_mark_text != 'F':
        gpa = str(round(((marks[flappybird_mark_text] + marks[game_2048_mark_text] + marks[minesweeper_mark_text] + marks[pong_mark_text]) / 4), 2))
    else: gpa = 'F'
    
    #Initialzing 
    pygame.init()
    
    #Setting up FPS 
    FPS = 60
    FramePerSec = pygame.time.Clock()
    
    #Set a screen
    screen = pygame.display.set_mode(metadata.SCREEN_SIZE)
    pygame.display.set_caption("The last of Us")
    
    #Load background image
    background_img = pygame.transform.scale(pygame.image.load('assets/attestation/attestation_background.jpg'), metadata.SCREEN_SIZE)
    
    #Load images
    back_main_menu_button_img = pygame.transform.scale(pygame.image.load('assets/attestation/back_main_menu_button.png'), (350, 50))
    quit_game_button_img = pygame.transform.scale(pygame.image.load('assets/attestation/quit_game_button.png'), (350, 50))
    
    while True:
        screen.blit(background_img, (0, 0))
        
        #Render text
        my_font = pygame.font.SysFont('monaco', 72)
        
        #Flappybird points render
        flappybird_score_surf = my_font.render(str(flappybird_score), True, metadata.WHITE)
        flappybird_mark_surf = my_font.render(flappybird_mark_text, True, metadata.WHITE)
        screen.blit(flappybird_score_surf, (740, 182)) 
        screen.blit(flappybird_mark_surf, (900, 182))
        
        #Game 2048 points render
        game_2048_score_surf = my_font.render(str(game_2048_score), True, metadata.WHITE)
        game_2048_mark_surf = my_font.render(game_2048_mark_text, True, metadata.WHITE)
        screen.blit(game_2048_score_surf, (740, 273)) 
        screen.blit(game_2048_mark_surf, (900, 273))
        
        #Minesweeper points render
        minesweeper_score_surf = my_font.render(str(minesweeper_score), True, metadata.WHITE)
        minesweeper_mark_surf = my_font.render(minesweeper_mark_text, True, metadata.WHITE)
        screen.blit(minesweeper_score_surf, (740, 365)) 
        screen.blit(minesweeper_mark_surf, (900, 365))
        
        #Pong points render
        pong_score_surf = my_font.render(str(pong_score), True, metadata.WHITE)
        pong_mark_surf = my_font.render(pong_mark_text, True, metadata.WHITE)
        screen.blit(pong_score_surf, (740, 456)) 
        screen.blit(pong_mark_surf, (900, 456))
        
        #GPA render
        gpa_surf = my_font.render(gpa, True, metadata.WHITE)
        screen.blit(gpa_surf, (900, 547))
        
        #Set buttons
        back_main_menu_button = screen.blit(back_main_menu_button_img, (200, 700))
        quit_game_button = screen.blit(quit_game_button_img, (650, 700))
        
        #Cycles through all events occurring  
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_main_menu_button.collidepoint(x, y):
                    metadata.clear()
                    import main
                    main.main()
                elif quit_game_button.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()  
           
        pygame.display.update()
        FramePerSec.tick(FPS)
    
main()