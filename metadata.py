SCREEN_SIZE = (1200, 800)

BLUE  = (0, 0, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (252, 248, 3)
ORANGE = (237, 183, 33)
PURPLE = (196, 33, 237)

PLAYER_GENDER = 'boy'

GAMES_DIFFICULTY = 3

GAME_2048_PLAYED = 0
GAME_2048_PLAY_LIMIT = GAMES_DIFFICULTY
GAME_2048_SCORE = 0

FLAPPYBIRD_PLAYED = 0
FLAPPYBIRD_PLAY_LIMIT = GAMES_DIFFICULTY
FLAPPYBIRD_SCORE = 0

MINESWEEPER_PLAYED = 0
MINESWEEPER_PLAY_LIMIT = GAMES_DIFFICULTY
MINESWEEPER_SCORE = 0

PONG_PLAYED = 0
PONG_PLAY_LIMIT = GAMES_DIFFICULTY
PONG_SCORE = 21

PLAYER_POSITION = (600, 750)

IS_GRADUATED = False

MAP_BACKGROUND_MUSIC_TIMESTAMP = 0

MUSIC_VOLUME = 5

CURRENT_SCORE = 0

def update(variable, value):
    global PLAYER_GENDER
    
    global GAMES_DIFFICULTY
    
    global GAME_2048_PLAYED
    global GAME_2048_PLAY_LIMIT
    global GAME_2048_SCORE
    
    global FLAPPYBIRD_PLAYED
    global FLAPPYBIRD_PLAY_LIMIT
    global FLAPPYBIRD_SCORE
    
    global MINESWEEPER_PLAYED
    global MINESWEEPER_PLAY_LIMIT
    global MINESWEEPER_SCORE
    
    global PONG_PLAYED
    global PONG_PLAY_LIMIT
    global PONG_SCORE
    
    global PLAYER_POSITION
    
    global MAP_BACKGROUND_MUSIC_TIMESTAMP
    
    global IS_GRADUATED
    
    global MUSIC_VOLUME
    
    global CURRENT_SCORE
    
    if (variable == 'PLAYER_GENDER'): PLAYER_GENDER = value
    elif (variable == 'GAME_2048_PLAYED'): GAME_2048_PLAYED = value
    elif (variable == 'GAME_2048_PLAY_LIMIT'): GAME_2048_PLAY_LIMIT = value
    elif (variable == 'GAME_2048_SCORE'): GAME_2048_SCORE = value
    elif (variable == 'FLAPPYBIRD_PLAYED'): FLAPPYBIRD_PLAYED = value
    elif (variable == 'FLAPPYBIRD_PLAY_LIMIT'): FLAPPYBIRD_PLAY_LIMIT = value
    elif (variable == 'FLAPPYBIRD_SCORE'): FLAPPYBIRD_SCORE = value
    elif (variable == 'MINESWEEPER_PLAYED'): MINESWEEPER_PLAYED = value
    elif (variable == 'MINESWEEPER_PLAY_LIMIT'): MINESWEEPER_PLAY_LIMIT = value
    elif (variable == 'MINESWEEPER_SCORE'): MINESWEEPER_SCORE = value
    elif (variable == 'PONG_PLAYED'): PONG_PLAYED = value
    elif (variable == 'PONG_PLAY_LIMIT'): PONG_PLAY_LIMIT = value
    elif (variable == 'PONG_SCORE'): PONG_SCORE = value
    elif (variable == 'PLAYER_POSITION'): PLAYER_POSITION = value
    elif (variable == 'MAP_BACKGROUND_MUSIC_TIMESTAMP'): MAP_BACKGROUND_MUSIC_TIMESTAMP = value
    elif (variable == 'IS_GRADUATED'): IS_GRADUATED = value
    elif (variable == 'MUSIC_VOLUME'): MUSIC_VOLUME = value
    elif (variable == 'GAMES_DIFFICULTY'): 
        GAMES_DIFFICULTY = value
        update('PONG_PLAY_LIMIT', GAMES_DIFFICULTY)
        update('FLAPPYBIRD_PLAY_LIMIT', GAMES_DIFFICULTY)
        update('GAME_2048_PLAY_LIMIT', GAMES_DIFFICULTY)
        update('MINESWEEPER_PLAY_LIMIT', GAMES_DIFFICULTY)
    elif (variable == 'CURRENT_SCORE'): CURRENT_SCORE = value
    
def clear():    
    global PLAYER_GENDER
    
    global GAMES_DIFFICULTY
    
    global GAME_2048_PLAYED
    global GAME_2048_PLAY_LIMIT
    global GAME_2048_SCORE
    
    global FLAPPYBIRD_PLAYED
    global FLAPPYBIRD_PLAY_LIMIT
    global FLAPPYBIRD_SCORE
    
    global MINESWEEPER_PLAYED
    global MINESWEEPER_PLAY_LIMIT
    global MINESWEEPER_SCORE
    
    global PONG_PLAYED
    global PONG_PLAY_LIMIT
    global PONG_SCORE
    
    global PLAYER_POSITION
    
    global IS_GRADUATED
    
    global MAP_BACKGROUND_MUSIC_TIMESTAMP
    
    global MUSIC_VOLUME
    
    global CURRENT_SCORE
    
    #print(f'Flappybird score: {FLAPPYBIRD_SCORE}')
    #print(f'Pong score: {PONG_SCORE}')
    #print(f'Minesweeper score: {MINESWEEPER_SCORE}')
    #print(f'Game 2048 score: {GAME_2048_SCORE}')
    
    PLAYER_GENDER = 'boy'
    
    GAMES_DIFFICULTY = 3
    
    GAME_2048_PLAYED = 0
    GAME_2048_PLAY_LIMIT = GAMES_DIFFICULTY
    GAME_2048_SCORE = 0

    FLAPPYBIRD_PLAYED = 0
    FLAPPYBIRD_PLAY_LIMIT = GAMES_DIFFICULTY
    FLAPPYBIRD_SCORE = 0

    MINESWEEPER_PLAYED = 0
    MINESWEEPER_PLAY_LIMIT = GAMES_DIFFICULTY
    MINESWEEPER_SCORE = 0

    PONG_PLAYED = 0
    PONG_PLAY_LIMIT = GAMES_DIFFICULTY
    PONG_SCORE = 21
    
    PLAYER_POSITION = (600, 750)
    
    IS_GRADUATED = False
    
    MAP_BACKGROUND_MUSIC_TIMESTAMP = 0
    
    MUSIC_VOLUME = 5
    
    CURRENT_SCORE = 0