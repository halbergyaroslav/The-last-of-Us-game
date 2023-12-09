import pygame, random, time
import metadata

score = 0

def main(): 
    #Create sell   
    class Cell:
        def __init__(self, i, j, w):
            self.i = i       
            self.j = j        
            self.x = i * w     
            self.y = j * w     
            self.w = w      
            self.bombCount = 0 
            self.bomb = False 
            self.revealed = False
            
        #Show cells
        def show(self):
            cell = pygame.Rect(self.x, self.y, self.w, self.w)
            if (self.revealed):
                if (self.bomb):
                    rect = img_bomb.get_rect()
                    rect.center = (int(self.x + self.w / 2), int(self.y + self.w / 2))
                    playSurface.blit(img_bomb, rect)
                else:
                    playSurface.fill(metadata.GRAY, cell)  
                    if (self.bombCount > 0):
                        sFont = pygame.font.SysFont('monaco', 30)
                        Ssurf = sFont.render('{0}'.format(self.bombCount), True, metadata.BLACK)
                        Srect = Ssurf.get_rect()
                        Srect.center = (self.x + self.w / 2, self.y + self.w / 2)
                        playSurface.blit(Ssurf, Srect)
            pygame.draw.rect(playSurface, metadata.BLACK, cell, 1) 
            
        #Check collision
        def contains(self, x, y):
            return (x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.w)
        
        #Print cells
        def reveal(self):
            self.revealed = True  
            self.show()            
            pygame.display.flip() 
            if (self.bombCount == 0):
                self.floodFill() 
           
        #Count bombs     
        def countBombs(self):
            if (self.bomb):
                self.bombCount = -1
                return
            total = 0 
            for xoff in range(-1, 2):
                for yoff in range(-1, 2):
                    i = self.i + xoff
                    j = self.j + yoff
                    if (i > -1 and i < cols and j > -1 and j < rows):
                        neighbor = grid[i][j]
                        if (neighbor.bomb):
                            total += 1     
            self.bombCount = total  
                
        def floodFill(self):
            global score 
            
            for xoff in range(-1, 2):
                for yoff in range(-1, 2):
                    i = self.i + xoff
                    j = self.j + yoff
                    if (i > -1 and i < cols and j > -1 and j < rows):
                        neighbor = grid[i][j]
                        if (not neighbor.bomb and not neighbor.revealed):
                            time.sleep(0.05) 
                            score += 1
                            neighbor.reveal()

    #Make an explosion
    class Explode:
        def __init__(self):
            self.image = [pygame.image.load("assets/minesweeper/explosion" + str(v) + ".png") for v in range(1, 9)]
            self.interval = 0.2  
            
        def show(self, index, x, y, w):
            img = pygame.transform.scale(self.image[index], (w - 2, w - 2))
            rect = img.get_rect()
            rect.center = (int(x + w / 2), int(y + w / 2))                   
            playSurface.blit(img, rect)                            
            pygame.display.flip()               
            
    def make2DArray(cols, rows):
        Array = [[0 for y in range(rows)] for x in range(cols)]
        return Array

    #Check mpve collision
    def MousePressed():
        global score
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for i in range(cols):
            for j in range(rows):
                if (grid[i][j].contains(mouse_x, mouse_y)):
                    sound_click.play()   
                    grid[i][j].reveal()
                    score += 1  
                    if (grid[i][j].bomb):
                        score -= 1
                        gameOver()

    #Quit the game
    def gameOver():
        new_score = max(metadata.MINESWEEPER_SCORE, score)
        metadata.update('MINESWEEPER_SCORE', new_score)
        metadata.update('CURRENT_SCORE', score)
        
        for i in range(cols):
            for j in range(rows):
                grid[i][j].revealed = True
        sound_bomb.play()
        sound_end.play()
        for i in range(cols):
            for j in range(rows):
                grid[i][j].show()
        time.sleep(0.1)
        explosion = Explode()
        for k in range(len(explosion.image)):
            for location in bombList:     
                i = location[0]
                j = location[1]
                bomb = grid[i][j]          
                explosion.show(k, bomb.x, bomb.y, bomb.w) 
            time.sleep(explosion.interval)   
        time.sleep(0.5)
        import gamescore
        gamescore.main('minesweeper')

    #Check winning
    def WinningDetect():
        for i in range(cols):
            for j in range(rows):
                cell = grid[i][j]
                if (cell.bomb and cell.revealed):
                    return False  
                elif (not cell.bomb and not cell.revealed):
                    return False  
        return True  

    def gameWinning():
        new_score = max(metadata.MINESWEEPER_SCORE, score)
        metadata.update('MINESWEEPER_SCORE', new_score)
        metadata.update('CURRENT_SCORE', score)
        
        sound1.play() 
        sound2.play()
        time.sleep(0.5)  
        import gamescore
        gamescore.main('minesweeper')  

    random.seed()

    pygame.init()

    pygame.mixer.init()

    #Set sounds
    sound_click = pygame.mixer.Sound('assets/minesweeper/Mouse.wav')
    sound_click.set_volume(0.5)

    sound_bomb = pygame.mixer.Sound('assets/minesweeper/Bomb.wav')
    sound_bomb.set_volume(0.3)

    sound_end = pygame.mixer.Sound('assets/minesweeper/fail.wav')
    sound_end.set_volume(0.3)

    sound1 = pygame.mixer.Sound('assets/minesweeper/DongDong.wav')
    sound1.set_volume(0.7)
    sound2 = pygame.mixer.Sound('assets/minesweeper/YouWin.wav')
    sound2.set_volume(0.7)

    width = 1200
    height = 800

    playSurface = pygame.display.set_mode(metadata.SCREEN_SIZE)
    pygame.display.set_caption('The last of Us')  

    fpsController = pygame.time.Clock()
    frame_rate = 50

    w = 40              
    cols = int(width / w)          
    rows = int(height / w)    
    grid = make2DArray(cols, rows)  

    #Load bombs
    img_bomb = pygame.image.load('assets/minesweeper/bomb.png')
    img_bomb = pygame.transform.scale(img_bomb, (int(w/2)+20, int(w/2)+20))

    totalBombs = 100

    for i in range(cols):
        for j in range(rows):
            grid[i][j] = Cell(i, j, w)

    optionList = []  
    bombList = []  

    for i in range(cols):
        for j in range(rows):
            optionList.append([i, j])

    for num in range(totalBombs):
        index = int(random.randrange(len(optionList))) 
        choice = optionList[index]     
        i = choice[0]                 
        j = choice[1]                    
        bombList.append(choice)    
        optionList.pop(index)        
        grid[i][j].bomb = True  

    for i in range(cols):
        for j in range(rows):
            grid[i][j].countBombs()

    while True:
        #Set background
        playSurface.fill(metadata.WHITE)

        for i in range(cols):
            for j in range(rows):
                grid[i][j].show()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                MousePressed()
        
        #Check winning
        if (WinningDetect()):
            gameWinning()

        pygame.display.update()          
        fpsController.tick(frame_rate)  
        
main()