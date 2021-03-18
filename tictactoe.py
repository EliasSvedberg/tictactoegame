import pygame as pygame, sys

class Game:
    def __init__(self, pygame, sys):
        self.pygame = pygame
        self.sys = sys
        self.pygame.init() #Start Pygame
        self.clock = pygame.time.Clock()
        self.winner = None
        self.draw = False
        self.tttArray = self.create_ttt_array()

    class Square:
        def __init__(self, r, c):
            self.row = r
            self.col = c
            self.clicked = False


    def set_screen(self, w, h):
        self.width = w
        self.height = h
        self.screen = self.pygame.display.set_mode((w,h))
        self.pygame.display.set_caption("Tic Tac Toe")

    def set_board_style(self, boardColor, lineColor):
        self.boardColor = boardColor
        self.lineColor = lineColor

    def set_fps(self, fps):
        self.fps = fps

    def set_imgs(self, xImg, oImg):
        #Loading images
        self.xImg = self.pygame.image.load(xImg)
        self.oImg = self.pygame.image.load(oImg)

        #resizing images
        self.xImg = self.pygame.transform.scale(self.xImg, (80,80))
        self.oImg = self.pygame.transform.scale(self.oImg, (80,80))


    def draw_board(self):
        #Drawing background
        self.screen.fill(self.boardColor)
        #Drawing vertical lines
        self.pygame.draw.line(self.screen,self.lineColor,
                            (self.width/3,0),
                            (self.width/3, self.height),7)
        self.pygame.draw.line(self.screen,self.lineColor,
                            (self.width/3*2,0),(self.width/3*2,
                             self.height),7)
        #Drawing horizontal lines
        self.pygame.draw.line(self.screen,self.lineColor,
                            (0,self.height/3),
                            (self.width, self.height/3),7)
        self.pygame.draw.line(self.screen,self.lineColor,
                            (0,self.height/3*2),
                            (self.width, self.height/3*2),7)

        #Draw X and O

        #Update screen
        self.pygame.display.update()

    def create_ttt_array(self):
        #creates instances of Squares in tttArray
        return [[self.Square(r, c) for c in range(3)] for r in range(3)]

    def user_click(self):
        #Get mouse pos and convert to rows/cols
        mPosX,mPosY = self.pygame.mouse.get_pos()
        r = floor(mPosY/self.height)
        c = floor(mPosY/self.width)

        #Set square to clicked
        for sq in self.tttArray:
            if (sq.row,sq.col) == (r,c):
                sq.clicked = True


    def game_loop(self):
        self.draw_board()
        #Game loop
        while (True):
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: #The user closed the window!
                    self.pygame.quit()
                    self.sys.exit() #Stop running
                elif event.type == self.pygame.MOUSEBUTTONDOWN:
                    dosomething = 1
                    if (self.winner or self.draw):
                        endgame = 1
        #set frames/second
        self.pygame.display.update()
        self.clock.tick(fps)

game = Game(pygame, sys)
game.set_screen(400, 400)
game.set_board_style((255,255,255),(0,0,0))
game.set_fps(30)
game.set_imgs("x.png", "o.png")
game.game_loop()
