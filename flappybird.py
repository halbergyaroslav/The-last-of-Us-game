import pygame, random, time
import metadata
from math import atan, degrees, pi

# Initialize Seed
random.seed()

def main():
    #Create bird
    class Bird:
        def __init__(self):
            self.x = 50      
            self.y = width / 2    
            self.gravity = 1 
            self.lift = 25 
            self.velocity = 0  
            
        #Present bird
        def show(self):
            angle = degrees(atan(-self.velocity / 15) + pi / 18)  
            pic = pygame.transform.rotate(img, angle)    
            playSurface.blit(pic, (int(self.x - img_width / 2), int(self.y - img_height / 2)))
            
        def update(self):
            self.velocity += self.gravity 
            self.velocity *= 0.9  
            self.y += self.velocity  
            if (self.y > height): 
                self.y = height
                self.velocity = 0
            if (self.y < 0): 
                self.y = 0
                self.velocity = 0
        def up(self):
            self.velocity += -self.lift  

    #Create pipes
    class Pipe:
        def __init__(self, level):
            self.top = random.randrange(int(height /2)) 
            self.gap = 200 - level*10         
            self.x = width        
            self.w = 30                
            self.speed = 3         
            self.color = metadata.WHITE          
            self.collide = False
          
        #Check hit with bird      
        def hit(self, bird):
            if (bird.y < self.top or bird.y > self.top + self.gap): 
                if (bird.x > self.x and bird.x < self.x + self.w):
                    self.collide = True 
                    return True
            self.collide = False 
            return False
        
        #Present pipes
        def show(self):
            upPipe = pygame.Rect((self.x, 0), (self.w, self.top))
            downPipe = pygame.Rect((self.x, self.top + self.gap), (self.w, height - self.top - self.gap))
            if (self.collide):
                self.color = metadata.RED
            else:
                self.color = metadata.WHITE
            pygame.draw.rect(playSurface, self.color, upPipe, 0)   
            pygame.draw.rect(playSurface, self.color, downPipe, 0)  
            #pipe = pygame.transform.scale(pygame.image.load('assets/flappy_bird/pipe.png'), (30, 400))
            #playSurface.blit(pipe, upPipe)
            #playSurface.blit(pipe, downPipe)
            
        def update(self):
            self.x -= self.speed   
          
        #Offscreen case  
        def offscreen(self):
            if (self.x < -self.w):
                return True
            else:
                return False
            
    def KeyPressed():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.up()  
                    sound1.play() 
    #Render score
    def showScore(choice):
        sFont = pygame.font.SysFont('monaco', 22)
        Ssurf = sFont.render('Score : {0}'.format(score), True, metadata.WHITE)
        Srect = Ssurf.get_rect()
        if choice == True:
            Srect.midtop = (200, 200)
        else:
            Srect.midtop = (350, 20)
        playSurface.blit(Ssurf, Srect)

    def gameOver():
        #Update game score
        new_score = max(metadata.FLAPPYBIRD_SCORE, score)
        metadata.update('FLAPPYBIRD_SCORE', new_score)
        metadata.update('CURRENT_SCORE', score)
        
        #Show postgame scene
        myFont = pygame.font.SysFont('monaco', 72)
        Game_Over_Surf = myFont.render('Game Over!', True, metadata.RED)
        Game_Over_Rect = Game_Over_Surf.get_rect()  
        Game_Over_Rect.midtop = (200, 130)  
        playSurface.blit(Game_Over_Surf, Game_Over_Rect) 
        pygame.display.update()
        pygame.mixer.music.pause()    
        sound_end.play()   
        time.sleep(0.01)
        import gamescore
        gamescore.main('flappybird')

    pygame.init()

    # Initialize Mixer
    pygame.mixer.init()

    # Setting Background Music
    pygame.mixer.music.load('assets/flappy_bird/GrasslandsTheme.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    #Load sounds
    sound1 = pygame.mixer.Sound('assets/flappy_bird/jump.wav')
    sound1.set_volume(0.1)

    sound_end = pygame.mixer.Sound('assets/flappy_bird/fail.wav')
    sound_end.set_volume(0.2)

    playSurface = pygame.display.set_mode(metadata.SCREEN_SIZE)
    width, height = metadata.SCREEN_SIZE
    pygame.display.set_caption('The last of Us')

    # Adding background for Discrete math
    background_flappy_bird = pygame.image.load('assets/flappy_bird/background_kbtu.jpg')
    # background_flappy_bird = pygame.image.load(r"C:\Users\User\Desktop\pp2 hackathon\assets\flappy_bird/hall_of_castle.jpg")
    background_flappy_bird = pygame.transform.scale(background_flappy_bird, (1200, 800))

    #Set FPS 
    fpsController = pygame.time.Clock()

    frame_rate = 50

    #Bird images
    img_width = 70
    img_height = 70

    img = pygame.image.load('assets/flappy_bird/bird.png')
    img = pygame.transform.scale(img, (img_width, img_height))

    #Set game objects
    bird = Bird()
    pipeList = []

    score = 0
    gameover = False

    while True:
        #Set background
        playSurface.blit(background_flappy_bird, (0,0))

        for i in range (len(pipeList)-1):
            if (pipeList[i].hit(bird)):
                gameover = True
            if (pipeList[i].offscreen()):
                pipeList.pop(i)  
                score += 1      
            pipeList[i].show()
            pipeList[i].update()

        level = int(score/20)

        #Frames
        frameCount = int(pygame.time.get_ticks() / 1000 * frame_rate)
        
        if (frameCount % 50 == 0 ): pipeList.append(Pipe(level))

        KeyPressed()
        
        bird.show()
        bird.update()

        showScore(gameover)

        #Gameover
        if (gameover == True):
            gameOver()

        pygame.display.update()       
        fpsController.tick(frame_rate)  
        
main()