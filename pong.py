import pygame, random
import metadata
from math import pi, sin, cos, radians

random.seed()

def main():
    #Set Puck
    class Puck:
        def __init__(self):
            self.x = width/2       
            self.y = height/2      
            self.r = 15           
            self.mag = 5          
            self.reset()
                        
        def update(self):
            self.x += self.x_speed   
            self.y += self.y_speed
            
        #Show pucks on the screen
        def show(self):          
            pygame.draw.circle(playSurface, white, (int(self.x), int(self.y)), self.r)
            
        #Add edges
        def edges(self):
            global leftscore, rightscore  
            if (self.y < 0 or self.y > height): self.y_speed *= -1      
            if (self.x - self.r < 0):    
                rightscore += 1        
                sound_score.play()    
                self.reset()             
            if (self.x + self.r > width):  
                leftscore += 1        
                sound_score.play()    
                self.reset()     
           
        #Set new screen game        
        def reset(self):
            self.x = width / 2   
            self.y = height / 2    
            self.mag = 5       
            angle = random.uniform(-pi / 4, pi / 4) 
            self.x_speed = self.mag * cos(angle)  
            self.y_speed = self.mag * sin(angle) 
            if (random.uniform(0, 1) > 0.5):  
                self.x_speed *= -1
                
        #Check left side
        def checkPaddleLeft(self, p):
            if (self.x - self.r < p.x + p.w / 2 and self.y > p.y - p.h / 2 and self.y < p.y + p.h / 2):
                if (self.x > p.x):
                    self.mag += 0.5                 
                    diff = self.y - (p.y - p.h / 2)   
                    rad = radians(45)         
                    angle = map(diff, 0, p.h, -rad, rad)  
                    self.x_speed = self.mag * cos(angle) 
                    self.y_speed = self.mag * sin(angle)  
                    sound_ping.play() 
                          
        #Check right side      
        def checkPaddleRight(self, p):
            if (self.x + self.r > p.x - p.w / 2 and self.y > p.y - p.h / 2 and self.y < p.y + p.h / 2):
                if (self.x < p.x):
                    self.mag += 0.5
                    diff = self.y - (p.y - p.h / 2)
                    rad = radians(45)
                    angle = map(diff, 0, p.h, rad, -rad) + pi
                    self.x_speed = self.mag * cos(angle)
                    self.y_speed = self.mag * sin(angle)
                    sound_ping.play()

    #Create paddle
    class Paddle:
        def __init__(self, left):
            self.y = height / 2    
            self.y_change = 0    
            self.w = 20     
            self.h = 200     
            if (left):
                self.x = self.w  
            else:
                self.x = width - self.w
                
        def update(self):
            self.y += self.y_change      
            self.y = Constrain(self.y, self.h) 
            
        def show(self):
            rect = pygame.Rect(0, 0, self.w, self.h)
            rect.center = (int(self.x), int(self.y))
            pygame.draw.rect(playSurface, white, rect)
        def move(self, steps):
            self.y_change = steps 

    #Print score
    def showScore():
        sFont = pygame.font.SysFont('monaco', 32)      
        Ssurf = sFont.render('{0}'.format(leftscore), True, white)  
        Srect = Ssurf.get_rect()                              
        Srect.midtop = (50, 25)                                  
        playSurface.blit(Ssurf, Srect)      
        Ssurf = sFont.render('{0}'.format(rightscore), True, white)
        Srect = Ssurf.get_rect()
        Srect.midtop = (width - 50, 25)
        playSurface.blit(Ssurf, Srect)

    def Constrain(y, h):
        down_limit = h/2  
        up_limit = height-h/2 
        if (y < down_limit):
            return down_limit  
        elif (y > up_limit):
            return up_limit 
        else:
            return y       

    step_w = 5 
    
    #Check events
    def KeyPressed():
        for event in pygame.event.get():  
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_UP:
                    right.move(-step_w)       
                if event.key == pygame.K_DOWN:
                    right.move(step_w)          
                if event.key == ord('w'):
                    left.move(-step_w)         
                if event.key == ord('s'):
                    left.move(step_w)      
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.type == pygame.KEYUP: 
                if event.key == pygame.K_UP:
                    right.move(0)         
                if event.key == pygame.K_DOWN:
                    right.move(0)          
                if event.key == ord('w'):
                    left.move(0)         
                if event.key == ord('s'):
                    left.move(0)

    #Set map
    def map(n, start1, stop1, start2, stop2):
        return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2

    pygame.init()

    pygame.mixer.init()

    sound_ping = pygame.mixer.Sound('assets/pong/PongSound.wav')
    sound_ping.set_volume(0.8)

    sound_score = pygame.mixer.Sound('assets/pong/cash.wav')
    sound_score.set_volume(0.6)

    width = 1200
    height = 800

    playSurface = pygame.display.set_mode(metadata.SCREEN_SIZE)
    pygame.display.set_caption('The last of Us')

    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)

    fpsController = pygame.time.Clock()
    frame_rate = 50

    puck = Puck()
    left = Paddle(True)
    right = Paddle(False)
    
    #Set scores
    global leftscore, rightscore

    leftscore = 0
    rightscore = 0

    while True:
        playSurface.fill(black)
        puck.checkPaddleLeft(left)
        puck.checkPaddleRight(right)
        
        puck.update()
        puck.edges()  
        puck.show()

        KeyPressed()

        left.update()
        right.update()
        left.show()
        right.show()

        showScore()
        
        #Check scores
        if leftscore > 10 or rightscore > 10:
            new_score = min(metadata.PONG_SCORE, leftscore + rightscore)
            metadata.update('PONG_SCORE', new_score)
            metadata.update('CURRENT_SCORE', leftscore + rightscore)
            
            import gamescore
            gamescore.main('pong')

        pygame.display.update()  
        fpsController.tick(frame_rate) 

main()