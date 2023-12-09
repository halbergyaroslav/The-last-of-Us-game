#Imports
import pygame, sys, time
from pygame.locals import *
import metadata

#Game Loop
def main(game_name):
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
    
    #Initialzing 
    pygame.init()
    
    #Setting up FPS 
    FPS = 60
    FramePerSec = pygame.time.Clock()
    
    #Set a screen
    screen = pygame.display.set_mode(metadata.SCREEN_SIZE)
    pygame.display.set_caption("The last of Us")
    
    #Load background image
    background_img = pygame.transform.scale(pygame.image.load('assets/gamescore/' + game_name + '_background.jpg'), metadata.SCREEN_SIZE)
    
    #Set score and mark
    if game_name == 'flappybird': 
        score = metadata.CURRENT_SCORE
        mark = flappybird_mark(score)
    elif game_name == 'game_2048': 
        score = metadata.CURRENT_SCORE
        mark = game_2048_mark(score)
    elif game_name == 'minesweeper': 
        score = metadata.CURRENT_SCORE
        mark = minesweeper_mark(score)
    elif game_name == 'pong': 
        score = metadata.CURRENT_SCORE
        mark = pong_mark(score)
    
    #Draw background
    screen.blit(background_img, (0, 0))
    
    #Render text
    my_font = pygame.font.SysFont('monaco', 72)
    score_surf = my_font.render(str(score), True, metadata.WHITE)
    mark_surf = my_font.render(mark, True, metadata.WHITE)
    screen.blit(score_surf, (680, 348)) 
    screen.blit(mark_surf, (680, 460))
    
    pygame.display.update()
    
    time.sleep(5)
    
    import map2
    map2.main()
    
    FramePerSec.tick(FPS)