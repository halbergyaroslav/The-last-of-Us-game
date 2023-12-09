#Imports
import pygame, sys
import metadata
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
    
    #Set background music
    if not metadata.IS_GRADUATED:
        pygame.mixer.music.load('assets/map/background_music.mp3')
        music_duration = 17
    else:
        pygame.mixer.music.load('assets/map/background_music_graduated.mp3')
        music_duration = 10
    pygame.mixer.music.set_volume(metadata.MUSIC_VOLUME / 100)
    pygame.mixer.music.play(loops = -1, start = metadata.MAP_BACKGROUND_MUSIC_TIMESTAMP)
    start_ticks = pygame.time.get_ticks()
    
    #Set background map
    background_map = pygame.transform.scale(pygame.image.load('assets/map/map_v1.2.jpg'), screen.get_size())
    background_map_graduated = pygame.transform.scale(pygame.image.load('assets/map/map_v1.3.jpg'), screen.get_size())
    
    #Load pause button image
    pause_button_img = pygame.transform.scale(pygame.image.load('assets/map/pause_button.png'), (60, 60))
    
    #Load image of player
    player_img = pygame.transform.scale(pygame.image.load('assets/map/player/' + metadata.PLAYER_GENDER + 'up2.png'), (30, 30))
    
    #Load mini-games teleport images
    mini_game_on_img = pygame.transform.scale(pygame.image.load('assets/map/mini_game_on.png'), (40, 40))
    
    #Lict of rects
    list_rects = []
    
    #Set rooms and rects
    #room1 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(60, 20, 160, 160))
    #inside1 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(75, 35, 130, 130)) 
    rect1 = pygame.Rect(75, 35, 131, 131)
    list_rects.append(rect1)
    
    #room2 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(220, 40, 160, 40))
    #inside2 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(205, 55, 190, 10)) 
    rect2 = pygame.Rect(205, 55, 191, 11)
    list_rects.append(rect2)
    
    #room3 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(300, 80, 40, 460))
    #inside3 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(315, 65, 10, 490)) 
    rect3 = pygame.Rect(315, 65, 11, 491)
    list_rects.append(rect3) 
    
    #room4 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(220, 340, 200, 40))
    #inside4 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(205, 355, 230, 10)) 
    rect4 = pygame.Rect(205, 355, 231, 11)
    list_rects.append(rect4) 
    
    #room5 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(60, 240, 160, 240))
    #inside5 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(75, 255, 130, 210)) 
    rect5 = pygame.Rect(75, 255, 131, 211)
    list_rects.append(rect5) 
    
    #room6 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(60, 540, 360, 200))
    #inside6 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(75, 555, 330, 170)) 
    rect6 = pygame.Rect(75, 555, 331, 171)
    list_rects.append(rect6) 
    
    #room7 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(380, 20, 420, 80))
    #inside7 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(395, 35, 390, 50)) 
    rect7 = pygame.Rect(395, 35, 391, 51)
    list_rects.append(rect7) 
    
    #room8 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(800, 40, 140, 40))
    #inside8 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(785, 55, 140, 10)) 
    rect8 = pygame.Rect(785, 65, 141, 11)
    list_rects.append(rect8) 
    
    #room9 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(900, 80, 40, 420))
    #inside9 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(915, 65, 10, 450)) 
    rect9 = pygame.Rect(915, 65, 11, 451)
    list_rects.append(rect9) 
    
    #room10 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(940, 160, 80, 40))
    #inside10 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(925, 175, 110, 10)) 
    rect10 = pygame.Rect(925, 175, 111, 11)
    list_rects.append(rect10) 
    
    #room11 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(940, 320, 80, 40))
    #inside11 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(925, 335, 110, 10)) 
    rect11 = pygame.Rect(925, 335, 111, 11)
    list_rects.append(rect11) 
    
    #room12 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(820, 340, 80, 40))
    #inside12 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(805, 355, 110, 10)) 
    rect12 = pygame.Rect(805, 355, 111, 11)
    list_rects.append(rect12) 
    
    #room13 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(1020, 40, 120, 420))
    #inside13 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(1035, 55, 90, 390)) 
    rect13 = pygame.Rect(1035, 55, 91, 391)
    list_rects.append(rect13)
    
    #room14 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(840, 500, 320, 240))
    #inside14 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(855, 515, 290, 210)) 
    rect14 = pygame.Rect(855, 515, 291, 211)
    list_rects.append(rect14)
    
    #room15 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(420, 600, 160, 40))
    #inside15 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(405, 615, 190, 10)) 
    rect15 = pygame.Rect(405, 615, 191, 11)
    list_rects.append(rect15)
    
    #room16 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(580, 560, 40, 180))
    #inside16 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(595, 545, 10, 210)) 
    rect16 = pygame.Rect(595, 545, 11, 211)
    list_rects.append(rect16)
    
    #room17 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(620, 640, 220, 40))
    #inside17 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(605, 655, 250, 10)) 
    rect17 = pygame.Rect(605, 655, 251, 11)
    list_rects.append(rect17)
    
    #room18 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(500, 740, 200, 60))
    #inside18 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(515, 755, 170, 30)) 
    rect18 = pygame.Rect(515, 755, 171, 31)
    list_rects.append(rect18)
    
    #room19 = pygame.draw.polygon(screen, colors.BLUE, ((420, 260), (480, 160), (760, 160), (820, 260), (820, 460), (760, 560), (480, 560), (420, 460)))
    #inside19 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(490, 175, 260, 370))
    rect19 = pygame.Rect(490, 175, 261, 371)
    list_rects.append(rect19)
    
    #inside20 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(485, 180, 270, 360))
    rect20 = pygame.Rect(485, 180, 271, 361)
    list_rects.append(rect20)
    
    #inside21 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(435, 260, 370, 200))
    rect21 = pygame.Rect(435, 260, 371, 201)
    list_rects.append(rect21)
    
    #inside22 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(480, 190, 280, 340))
    rect22 = pygame.Rect(480, 190, 281, 341)
    list_rects.append(rect22)
    
    #inside23 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(475, 195, 290, 330))
    rect23 = pygame.Rect(475, 195, 291, 331)
    list_rects.append(rect23)
    
    #inside24 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(470, 205, 300, 310))
    rect24 = pygame.Rect(470, 205, 301, 311)
    list_rects.append(rect24)
    
    #inside25 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(465, 210, 310, 300))
    rect25 = pygame.Rect(465, 210, 311, 301)
    list_rects.append(rect25)
    
    #inside26 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(460, 220, 320, 280))
    rect26 = pygame.Rect(460, 220, 321, 281)
    list_rects.append(rect26)
    
    #inside27 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(455, 230, 330, 260))
    rect27 = pygame.Rect(455, 230, 331, 261)
    list_rects.append(rect27)
    
    #inside28 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(450, 240, 340, 240))
    rect28 = pygame.Rect(450, 240, 341, 241)
    list_rects.append(rect28)
    
    #inside29 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(445, 250, 350, 220))
    rect29 = pygame.Rect(445, 250, 351, 221)
    list_rects.append(rect29)
    
    #inside30 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(440, 255, 360, 210))
    rect30 = pygame.Rect(440, 255, 361, 211)
    list_rects.append(rect29)
    
    #Set player
    prev_player_x, prev_player_y = metadata.PLAYER_POSITION
    player_x, player_y = metadata.PLAYER_POSITION
    
    #Set player condition and destination 
    player_condition = 2
    player_destination = 'up'
    
    #Set sound
    step_sound = pygame.mixer.Sound('assets/map/step.mp3')
    step_sound.set_volume(0.2)
    
    is_moved = 0
    
    while True:  
        #Set player image
        player_img = pygame.transform.scale(pygame.image.load('assets/map/player/' + metadata.PLAYER_GENDER + player_destination + str(player_condition) + '.png'), (30, 30))
        
        #Set map
        if metadata.PONG_PLAYED > 0 and metadata.FLAPPYBIRD_PLAYED > 0 and metadata.MINESWEEPER_PLAYED > 0 and metadata.GAME_2048_PLAYED > 0: 
            metadata.update('IS_GRADUATED', True)
            screen.blit(background_map_graduated, (0, 0))
        else: screen.blit(background_map, (0, 0))
        attestation_button_rect = pygame.Rect(487, 223, 263, 60)
        
        #Set pause button
        pause_button = screen.blit(pause_button_img, (1140, 20))
        
        #Load mini-games buttons
        if metadata.PONG_PLAYED < metadata.PONG_PLAY_LIMIT: screen.blit(mini_game_on_img, (223, 623))
        pong_mini_game_button_rect = pygame.Rect(223, 623, 40, 40)
        
        if metadata.FLAPPYBIRD_PLAYED < metadata.FLAPPYBIRD_PLAY_LIMIT: screen.blit(mini_game_on_img, (120, 40))
        flappybird_mini_game_button_rect = pygame.Rect(120, 40, 40, 40)
        
        if metadata.MINESWEEPER_PLAYED < metadata.MINESWEEPER_PLAY_LIMIT: screen.blit(mini_game_on_img, (1080, 60))
        minesweeper_mini_game_button_rect = pygame.Rect(1080, 60, 40, 40)
        
        if metadata.GAME_2048_PLAYED < metadata.GAME_2048_PLAY_LIMIT: screen.blit(mini_game_on_img, (940, 550))
        game_2048_mini_game_button_rect = pygame.Rect(940, 550, 40, 40)
        
        #screen.blit(player_img, (1017, 637))
        #pygame.draw.rect(screen, metadata.BLUE, attestation_button_rect)
        
        #Draw player
        if is_moved: step_sound.play()
        metadata.update('PLAYER_POSITION', (player_x, player_y))
        player = screen.blit(player_img, (player_x - 15, player_y - 15)) 
        is_moved = 0
              
        #Cycles through all events occurring  
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if pause_button.collidepoint(x, y):
                    timestamp = (pygame.time.get_ticks() - start_ticks) / 1000
                    metadata.update('MAP_BACKGROUND_MUSIC_TIMESTAMP', ((metadata.MAP_BACKGROUND_MUSIC_TIMESTAMP + timestamp) % music_duration))
                    pygame.mixer.music.stop()
                    import pause
                    pause.main()
                
            elif event.type == pygame.KEYDOWN:
                
                #room1 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(60, 20, 160, 160))  
                #room2 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(220, 40, 160, 40)) 
                #room3 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(300, 80, 40, 460))
                #room4 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(220, 340, 200, 40))
                #room5 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(60, 240, 160, 240))
                #room6 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(60, 540, 360, 200))
                #room7 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(380, 20, 420, 80))
                #room8 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(800, 40, 140, 40))
                #room9 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(900, 80, 40, 420))
                #room10 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(940, 160, 80, 40))
                #room11 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(940, 320, 80, 40))
                #room12 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(820, 340, 80, 40))
                #room13 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(1020, 40, 120, 420))
                #room14 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(840, 500, 320, 240))
                #room15 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(420, 600, 160, 40))
                #room16 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(580, 560, 40, 180))
                #room17 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(620, 640, 220, 40))
                #room18 = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(500, 740, 200, 60))
                #room19 = pygame.draw.polygon(screen, colors.BLUE, ((420, 260), (480, 160), (760, 160), (820, 260), (820, 460), (760, 560), (480, 560), (420, 460)))
                
                #inside1 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(75, 35, 130, 130)) 
                #inside2 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(205, 55, 190, 10)) 
                #inside3 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(315, 65, 10, 490)) 
                #inside4 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(205, 355, 230, 10))    
                #inside5 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(75, 255, 130, 210))  
                #inside6 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(75, 555, 330, 170))    
                #inside7 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(395, 35, 390, 50)) 
                #inside8 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(785, 55, 140, 10))  
                #inside9 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(915, 65, 10, 450)) 
                #inside10 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(925, 175, 110, 10))   
                #inside11 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(925, 335, 110, 10)) 
                #inside12 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(805, 355, 110, 10)) 
                #inside13 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(1035, 55, 90, 390)) 
                #inside14 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(855, 515, 290, 210)) 
                #inside15 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(405, 615, 190, 10)) 
                #inside16 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(595, 545, 10, 210)) 
                #inside17 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(605, 655, 250, 10)) 
                #inside18 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(515, 755, 170, 30))
                #inside19 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(490, 175, 260, 370))
                #inside20 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(485, 180, 270, 360))
                #inside21 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(435, 260, 370, 200))
                #inside22 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(480, 190, 281, 341))
                #inside23 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(475, 195, 290, 330))
                #inside24 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(470, 205, 300, 310))
                #inside25 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(465, 210, 310, 300))
                #inside26 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(460, 220, 320, 280))
                #inside27 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(455, 230, 330, 260))
                #inside28 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(450, 240, 340, 240))
                #inside29 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(445, 250, 350, 220))
                #inside30 = pygame.draw.rect(screen, colors.BLACK, pygame.Rect(440, 255, 360, 210))
                
                if event.key == pygame.K_UP:
                    player_y -= 5
                    in_room = False
                    
                    for rect in list_rects:
                        if rect.collidepoint((player_x, player_y)): in_room = True
                    
                    if in_room: 
                        prev_player_x, prev_player_y = player_x, player_y
                        player_destination = 'up'
                        player_condition += 1
                        player_condition %= 2
                        is_moved = 1
                    else: 
                        player_x, player_y = prev_player_x, prev_player_y                    
                        
                elif event.key == pygame.K_DOWN:
                    player_y += 5
                    in_room = False
                    
                    for rect in list_rects:
                        if rect.collidepoint((player_x, player_y)): in_room = True
                    
                    if in_room: 
                        prev_player_x, prev_player_y = player_x, player_y
                        player_destination = 'down'
                        player_condition += 1
                        player_condition %= 2
                        is_moved = 1
                    else: 
                        player_x, player_y = prev_player_x, prev_player_y 
                    
                elif event.key == pygame.K_LEFT:
                    player_x -= 5
                    in_room = False
                    
                    for rect in list_rects:
                        if rect.collidepoint((player_x, player_y)): in_room = True
                    
                    if in_room: 
                        prev_player_x, prev_player_y = player_x, player_y
                        player_destination = 'left'
                        player_condition += 1
                        player_condition %= 2
                        is_moved = 1
                    else: 
                        player_x, player_y = prev_player_x, prev_player_y 
                    
                elif event.key == pygame.K_RIGHT:
                    player_x += 5
                    in_room = False
                    
                    for rect in list_rects:
                        if rect.collidepoint((player_x, player_y)): in_room = True
                    
                    if in_room: 
                        prev_player_x, prev_player_y = player_x, player_y
                        player_destination = 'right'
                        player_condition += 1
                        player_condition %= 2
                        is_moved = 1
                    else: 
                        player_x, player_y = prev_player_x, prev_player_y
                
                player_rect = pygame.Rect(player_x - 15, player_y - 15, 30, 30)
                
                if pong_mini_game_button_rect.contains(player_rect) and metadata.PONG_PLAYED < metadata.PONG_PLAY_LIMIT:
                    metadata.update('PONG_PLAYED', metadata.PONG_PLAYED + 1)
                    metadata.update('PLAYER_POSITION', (112, 628))
                    timestamp = (pygame.time.get_ticks() - start_ticks) / 1000
                    metadata.update('MAP_BACKGROUND_MUSIC_TIMESTAMP', ((metadata.MAP_BACKGROUND_MUSIC_TIMESTAMP + timestamp) % music_duration))
                    pygame.mixer.music.stop()
                    import pong
                    pong.main()
                    
                elif flappybird_mini_game_button_rect.contains(player_rect) and metadata.FLAPPYBIRD_PLAYED < metadata.FLAPPYBIRD_PLAY_LIMIT:
                    metadata.update('FLAPPYBIRD_PLAYED', metadata.FLAPPYBIRD_PLAYED + 1)
                    metadata.update('PLAYER_POSITION', (113, 145))
                    timestamp = (pygame.time.get_ticks() - start_ticks) / 1000
                    metadata.update('MAP_BACKGROUND_MUSIC_TIMESTAMP', ((metadata.MAP_BACKGROUND_MUSIC_TIMESTAMP + timestamp) % music_duration))
                    pygame.mixer.music.stop()
                    import flappybird
                    flappybird.main()
                    
                elif minesweeper_mini_game_button_rect.contains(player_rect) and metadata.MINESWEEPER_PLAYED < metadata.MINESWEEPER_PLAY_LIMIT:
                    metadata.update('MINESWEEPER_PLAYED', metadata.MINESWEEPER_PLAYED + 1)
                    metadata.update('PLAYER_POSITION', (1095, 185))
                    timestamp = (pygame.time.get_ticks() - start_ticks) / 1000
                    metadata.update('MAP_BACKGROUND_MUSIC_TIMESTAMP', ((metadata.MAP_BACKGROUND_MUSIC_TIMESTAMP + timestamp) % music_duration))
                    pygame.mixer.music.stop()
                    import minesweeper
                    minesweeper.main()
                    
                elif game_2048_mini_game_button_rect.contains(player_rect) and metadata.GAME_2048_PLAYED < metadata.GAME_2048_PLAY_LIMIT:
                    metadata.update('GAME_2048_PLAYED', metadata.GAME_2048_PLAYED + 1)
                    metadata.update('PLAYER_POSITION', (1017, 637))
                    timestamp = (pygame.time.get_ticks() - start_ticks) / 1000
                    metadata.update('MAP_BACKGROUND_MUSIC_TIMESTAMP', ((metadata.MAP_BACKGROUND_MUSIC_TIMESTAMP + timestamp) % music_duration))
                    pygame.mixer.music.stop()
                    import game_2048
                    game_2048.main()
                    
                elif attestation_button_rect.contains(player_rect) and metadata.IS_GRADUATED:
                    timestamp = (pygame.time.get_ticks() - start_ticks) / 1000
                    metadata.update('MAP_BACKGROUND_MUSIC_TIMESTAMP', ((metadata.MAP_BACKGROUND_MUSIC_TIMESTAMP + timestamp) % music_duration))
                    pygame.mixer.music.stop()
                    import attestation
                    attestation.main()                   
            
        pygame.display.update()
        FramePerSec.tick(FPS)
    
main()