#This program creates a tic tac toe game for two players
#if the game ends in a draw, allow players to move pieces until win
import pygame, sys, math
from pygame.locals import *

FPS = 30 #frames per second, speed of program
WINDOWWIDTH = 320 # size of window's width in pixels
WINDOWHEIGHT = 240 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 3 # number of columns of icons
BOARDHEIGHT = 3 # number of rows of icons
assert math.sqrt(BOARDWIDTH * BOARDHEIGHT) == BOARDWIDTH, 'Board must be a square'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
#XMARGIN = 320 - 75
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
#YMARGIN = 240 - 75

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

BGCOLOR = CYAN
LIGHTBGCOLOR = GRAY
BOXCOLOR = BLACK
HIGHLIGHTCOLOR = GREEN
XCOLOR = RED
OCOLOR = BLUE

X = 'player 1'
O = 'player 2'

class Board:
    def __init__(self):
        self.rows = 3
        self.columns = 3

        #declare board array (idk if this is static or dynamic yet)
        self.board = [[0 for x in range(0, 3)] for y in range(0, 3)]
        for x in range(0, 3):
            for y in range(0, 3):
                self.board[x][y] = '.'

    def getRows(self):
        return self.rows
    def getColumns(self):
        return self.columns
    def getBoardSpace(self, r, col):
        return self.board[r][col]

    def checkWin(self, turns):
        if turns % 2 != 0:
            if self.board[0][0] == 'x' and self.board[0][1] == 'x' and self.board[0][2] == 'x':
                return True
            if self.board[1][0] == 'x' and self.board[1][1] == 'x' and self.board[1][2] == 'x':
                return True
            if self.board[2][0] == 'x' and self.board[2][1] == 'x' and self.board[2][2] == 'x':
                return True
            if self.board[0][0] == 'x' and self.board[1][0] == 'x' and self.board[2][0] == 'x':
                return True
            if self.board[0][1] == 'x' and self.board[1][1] == 'x' and self.board[2][1] == 'x':
                return True
            if self.board[0][2] == 'x' and self.board[1][2] == 'x' and self.board[2][2] == 'x':
                return True
            if self.board[0][0] == 'x' and self.board[1][1] == 'x' and self.board[2][2] == 'x':
                return True
            if self.board[0][2] == 'x' and self.board[1][1] == 'x' and self.board[2][0] == 'x':
                return True
        if turns % 2 == 0:
            if self.board[0][0] == 'o' and self.board[0][1] == 'o' and self.board[0][2] == 'o':
                return True
            if self.board[1][0] == 'o' and self.board[1][1] == 'o' and self.board[1][2] == 'o':
                return True
            if self.board[2][0] == 'o' and self.board[2][1] == 'o' and self.board[2][2] == 'o':
                return True
            if self.board[0][0] == 'o' and self.board[1][0] == 'o' and self.board[2][0] == 'o':
                return True
            if self.board[0][1] == 'o' and self.board[1][1] == 'o' and self.board[2][1] == 'o':
                return True
            if self.board[0][2] == 'o' and self.board[1][2] == 'o' and self.board[2][2] == 'o':
                return True
            if self.board[0][0] == 'o' and self.board[1][1] == 'o' and self.board[2][2] == 'o':
                return True
            if self.board[0][2] == 'o' and self.board[1][1] == 'o' and self.board[2][0] == 'o':
                return True

    def drawBoard(self, DISPLAYSURF):
        #checker board
        pygame.draw.line(DISPLAYSURF, BLACK, (128, 190), (128, 45), 2)
        pygame.draw.line(DISPLAYSURF, BLACK, (178, 190), (178, 45), 2)

        pygame.draw.line(DISPLAYSURF, BLACK, (80, 90), (230, 90), 2)
        pygame.draw.line(DISPLAYSURF, BLACK, (80, 140), (230, 140), 2)


        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                left, top = self.leftTopCoordsOfBox(x, y)
                if self.board[x][y] == 'x':
                    self.drawX(x, y, DISPLAYSURF)
                if self.board[x][y] == 'o':
                    self.drawO(x, y, DISPLAYSURF)
                if self.board[x][y] == '.':
                    pygame.draw.rect(DISPLAYSURF, CYAN, (left, top, (BOXSIZE/2), (BOXSIZE/2)))

    def drawX(self, boxX, boxY, DISPLAYSURF):
        quarter = int(BOXSIZE * 0.25) #makes my life easier, I think
        half = int(BOXSIZE * 0.5)

        left, top = self.leftTopCoordsOfBox(boxX, boxY)
        #draw x
        pygame.draw.line(DISPLAYSURF, XCOLOR, (left, top), (left + BOXSIZE, top + BOXSIZE), 5)
        pygame.draw.line(DISPLAYSURF, XCOLOR, (left, top + BOXSIZE), (left + BOXSIZE, top), 5)
        #place x on array (for keeping track)
        self.board[boxX][boxY] = 'x'

    def drawO(self, boxX, boxY, DISPLAYSURF):
        half = int(BOXSIZE * 0.5)

        left, top = self.leftTopCoordsOfBox(boxX, boxY)
        #draw o
        pygame.draw.circle(DISPLAYSURF, OCOLOR, (left + half, top + half), half - 5, 5)
        #place o on array (for keeping track)
        self.board[boxX][boxY] = 'o'

    def getBoxAtPixel(self, x, y):
        for boxX in range(BOARDWIDTH):
            for boxY in range(BOARDHEIGHT):
                left, top = self.leftTopCoordsOfBox(boxX, boxY)
                boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
                if boxRect.collidepoint(x, y):
                    return (boxX, boxY)
        return (None, None)

    def drawHighlightBox(self, boxX, boxY, DISPLAYSURF):
        left, top = self.leftTopCoordsOfBox(boxX, boxY)
        pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

    # Convert board coordinates to pixel coordinates
    def leftTopCoordsOfBox(self, boxx, boxy):
        left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
        top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
        return (left, top)


global FPSClOCK, DISPLAYSURF
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

mouseX = 0
mouseY = 0 #these are used to store coordinates of mouse event
pygame.display.set_caption('Tic-Tac-Toe')

gameBoard = Board()
filledSpace = [[0 for x in range(0, 3)] for y in range(0, 3)]
for x in range(0, 3):
    for y in range(0, 3):
        filledSpace[x][y] = False

playerOneTokens = 3 # stores player 1's tokens
playerTwoTokens = 3 # stores player 2's tokens
turns = 0

while True:
    mouseClicked = False

    DISPLAYSURF.fill(BGCOLOR)
    gameBoard.drawBoard(DISPLAYSURF)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouseX, mouseY = event.pos
            mouseClicked = True

    boxX, boxY = gameBoard.getBoxAtPixel(mouseX, mouseY) #location of mouse
    if boxX != None and boxY != None: #mouse is over box
        #if empty box
        if not filledSpace[boxX][boxY]:
            gameBoard.drawHighlightBox(boxX, boxY, DISPLAYSURF)
        if not filledSpace[boxX][boxY] and mouseClicked:
            if playerOneTokens == playerTwoTokens and playerOneTokens > 0: #player ones turn
                gameBoard.drawX(boxX, boxY, DISPLAYSURF)
                playerOneTokens -= 1
                turns += 1
                print(turns)
                print("x drawn. p1 tokens = %i" % playerOneTokens)
                filledSpace[boxX][boxY] = True
            elif playerOneTokens < playerTwoTokens and playerTwoTokens > 0: #player twos turn (i sense issues)
                print("Poop")
                gameBoard.drawO(boxX, boxY, DISPLAYSURF)
                playerTwoTokens -=1
                turns += 1
                print(turns)
                print("y drawn. p2 tokens = %i" % playerTwoTokens)
                filledSpace[boxX][boxY] = True


    if gameBoard.checkWin(turns):
        if turns % 2 != 0:
            print("Player 1 wins")
        if turns % 2 == 0:
            print("Player 2 wins")

        playerOneTokens = 3
        playerTwoTokens = 3
        for x in range(0, 3):
            for y in range(0, 3):
                filledSpace[x][y] = False
        del gameBoard
        gameBoard = Board() #this is faster than resetting the array imo

    if (playerOneTokens + playerTwoTokens == 0) and not gameBoard.checkWin(turns):
        print("Draw")
        #reset game
        playerOneTokens = 3
        playerTwoTokens = 3
        for x in range(0, 3):
            for y in range(0, 3):
                filledSpace[x][y] = False
        del gameBoard
        gameBoard = Board() #this is faster than resetting the array imo

    pygame.display.update()
    FPSCLOCK.tick(FPS)
