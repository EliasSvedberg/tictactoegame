import pygame as pygame, sys
import math
import time

class Game:

    def __init__(self, pygame, sys):
        self.pygame = pygame
        self.sys = sys
        self.pygame.init() #Start Pygame
        self.clock = pygame.time.Clock()
        self.winner = None
        self.draw = False
        self.activePlayer = "x"

    class Square:

        def __init__(self, r, c, xPos, yPos):
            self.row = r
            self.col = c
            self.xPos = xPos
            self.yPos = yPos
            self.clicked = False
            self.clickedBy = None

    def set_screen(self, w, h, lw):
        self.width = w
        self.height = h
        self.lineWidth = lw
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
        self.imgWidth = int(self.width/5)
        self.imgHeight = int(self.height/5)
        self.xImg = self.pygame.transform.scale(self.xImg, (self.imgWidth, self.imgHeight))
        self.oImg = self.pygame.transform.scale(self.oImg, (self.imgWidth, self.imgHeight))

    def draw_board(self):
        #Drawing background
        self.screen.fill(self.boardColor)
        #Drawing vertical lines
        self.pygame.draw.line(self.screen,self.lineColor,
                            (self.width/3,0),
                            (self.width/3, self.height),self.lineWidth)
        self.pygame.draw.line(self.screen,self.lineColor,
                            (self.width/3*2,0),(self.width/3*2,
                             self.height),self.lineWidth)
        #Drawing horizontal lines
        self.pygame.draw.line(self.screen,self.lineColor,
                            (0,self.height/3),
                            (self.width, self.height/3),self.lineWidth)
        self.pygame.draw.line(self.screen,self.lineColor,
                            (0,self.height/3*2),
                            (self.width, self.height/3*2),self.lineWidth)
        #Draw X and O
        for r in range(3):
            for c in range(3):
                if self.tttArray[r][c].clicked:
                    if self.tttArray[r][c].clickedBy == "x":
                        self.screen.blit(self.xImg,
                        (self.tttArray[r][c].xPos, self.tttArray[r][c].yPos))
                    else:
                        self.screen.blit(self.oImg,
                        (self.tttArray[r][c].xPos, self.tttArray[r][c].yPos))

        #Update screen
        self.pygame.display.update()

    def create_ttt_array(self):
        #Set x,y cordinates for each img
        xPos = (self.width/3 - self.imgWidth)/2
        yPos = (self.height/3 - self.imgHeight)/2

        #Creates instances of Squares in tttArray
        return [[self.Square(r, c, (xPos+c*(self.width/3)),
        (yPos+r*(self.height/3)) ) for c in range(3)] for r in range(3)]

    def change_player(self):
        if self.activePlayer == "x":
            self.activePlayer = "o"
        else:
            self.activePlayer = "x"

    def user_click(self):
        #Get mouse pos and convert to rows/cols
        mPosX,mPosY = self.pygame.mouse.get_pos()
        mRow = math.floor(mPosY/(self.height/3))
        mCol = math.floor(mPosX/(self.width/3))
        #Set square to clicked
        for r in range(3):
            for c in range(3):
                if (self.tttArray[r][c].row, self.tttArray[r][c].col) == (mRow, mCol):
                    if self.tttArray[r][c].clicked == False:
                        self.tttArray[r][c].clicked = True
                        self.tttArray[r][c].clickedBy = self.activePlayer
                        #change player
                        self.change_player()

    def check_win_or_draw(self):
        #Row wins
        for r in range(3):
            if (self.tttArray[r][0].clickedBy == self.tttArray[r][1].clickedBy
             == self.tttArray[r][2].clickedBy):
                self.winner =  self.tttArray[r][0].clickedBy
                break
        #Column wins
        for c in range(3):
            if (self.tttArray[0][c].clickedBy == self.tttArray[1][c].clickedBy
             == self.tttArray[2][c].clickedBy):
                self.winner =  self.tttArray[0][c].clickedBy
                break
        #Left to right diagonal win
        if (self.tttArray[0][0].clickedBy == self.tttArray[1][1].clickedBy
         == self.tttArray[2][2].clickedBy):
            self.winner =  self.tttArray[0][0].clickedBy
        #Right to left diagonal win
        if (self.tttArray[0][2].clickedBy == self.tttArray[1][1].clickedBy
         == self.tttArray[2][0].clickedBy):
            self.winner =  self.tttArray[0][2].clickedBy

        #Create clicked arr
        clicked = [[c.clicked for c in r] for r in self.tttArray]
        #Check draw
        if(all([all(row) for row in clicked]) and self.winner is None):
            self.draw = True

    def game_finished(self):
        time.sleep(3)
        if self.winner:
            message = f"The winner was: {self.winner}"
        else:
            message = "The game was a Draw"

        font = self.pygame.font.Font(None, 30)
        text = font.render(message,1, (0,0,0))
        # copy the rendered message onto the board
        self.screen.fill (self.boardColor)
        text_rect = text.get_rect(center=(self.width/2, 200))
        self.screen.blit(text, text_rect)
        self.pygame.display.update()

    def game_loop(self):
        self.tttArray = self.create_ttt_array()
        self.draw_board()
        #Game loop
        while (True):
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: #The user closed the window!
                    self.pygame.quit()
                    self.sys.exit() #Stop running
                elif event.type == self.pygame.MOUSEBUTTONDOWN:
                    self.user_click()
                    self.draw_board()
                    self.check_win_or_draw()
                    if (self.winner or self.draw):
                        self.game_finished()
        #set frames/second
        self.pygame.display.update()
        self.clock.tick(fps)

game = Game(pygame, sys)
game.set_screen(400, 400, 12)
game.set_board_style((255,255,255),(0,0,0))
game.set_fps(30)
game.set_imgs("x.png", "o.png")
game.game_loop()
