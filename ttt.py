# tic tac toe game
import pygame as pg
import sys

#game init
pg.init()
pg.display.set_caption('Tic Tac Toe')
screen = pg.display.set_mode((950, 700))
clock = pg.time.Clock()
running = True
players = ['1player', '2player']
player_points = {players[0]: 0, players[1]: 0}
draws = 0
current_player = players[1]
scales = [(3,3),(5,5),(8,8)]
current_scale = scales[0]
how_many_needed_to_win = 3
font = pg.font.SysFont('Arial', 50)
index = 0 # for scales list


#images
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')

board = []
def figureOutScale(scale):
    global x_img, o_img, board
    if scale == (3,3):
        
        board = [
                 [0,0,0],
                 [0,0,0],
                 [0,0,0],
                ]
        
        x_img = pg.transform.scale(x_img, (200, 200))
        o_img = pg.transform.scale(o_img, (200, 200))
    if scale == (5,5):
        board = [[0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 ]
        x_img = pg.transform.scale(x_img, (120, 120))
        o_img = pg.transform.scale(o_img, (120, 120))
    if scale == (8,8):
        board = [[0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 ]
        x_img = pg.transform.scale(x_img, (75, 75))
        o_img = pg.transform.scale(o_img, (75, 75))

def drawGrid(scale):
    if scale == (3,3):
        pg.draw.line(screen, "black", (200, 0), (200, 600), 5)
        pg.draw.line(screen, "black", (400, 0), (400, 600), 5)
        pg.draw.line(screen, "black", (0, 200), (600, 200), 5)
        pg.draw.line(screen, "black", (0, 400), (600, 400), 5)
        pg.draw.line(screen, "black", (0, 600), (600, 600), 5)
        pg.draw.line(screen, "black", (600, 0), (600, 600), 5)
    if scale == (5,5):
        pg.draw.line(screen, "black", (120, 0), (120, 600), 5)
        pg.draw.line(screen, "black", (240, 0), (240, 600), 5)
        pg.draw.line(screen, "black", (360, 0), (360, 600), 5)
        pg.draw.line(screen, "black", (480, 0), (480, 600), 5)
        pg.draw.line(screen, "black", (600, 0), (600, 600), 5)
        pg.draw.line(screen, "black", (0, 120), (600, 120), 5)
        pg.draw.line(screen, "black", (0, 240), (600, 240), 5)
        pg.draw.line(screen, "black", (0, 360), (600, 360), 5)
        pg.draw.line(screen, "black", (0, 480), (600, 480), 5)
        pg.draw.line(screen, "black", (0, 600), (600, 600), 5)
    if scale == (8,8):


        pg.draw.line(screen, "black", (75, 0), (75, 600), 5)
        pg.draw.line(screen, "black", (150, 0), (150, 600), 5)
        pg.draw.line(screen, "black", (225, 0), (225, 600), 5)
        pg.draw.line(screen, "black", (300, 0), (300, 600), 5)
        pg.draw.line(screen, "black", (375, 0), (375, 600), 5)
        pg.draw.line(screen, "black", (450, 0), (450, 600), 5)
        pg.draw.line(screen, "black", (525, 0), (525, 600), 5)
        pg.draw.line(screen, "black", (600, 0), (600, 600), 5)
        pg.draw.line(screen, "black", (0, 75), (600, 75), 5)
        pg.draw.line(screen, "black", (0, 150), (600, 150), 5)
        pg.draw.line(screen, "black", (0, 225), (600, 225), 5)
        pg.draw.line(screen, "black", (0, 300), (600, 300), 5)
        pg.draw.line(screen, "black", (0, 375), (600, 375), 5)
        pg.draw.line(screen, "black", (0, 450), (600, 450), 5)
        pg.draw.line(screen, "black", (0, 525), (600, 525), 5)
        pg.draw.line(screen, "black", (0, 600), (600, 600), 5)
        pg.draw.line(screen, "black", (600, 0), (600, 600), 5)

def drawXO(row, col):
    global current_player
    try:
        if board[row][col] != 0:
            return
        
        if current_player == players[0]:
            board[row][col] = current_player
            if current_scale == (3,3):
                screen.blit(x_img, (row * 200, col * 200))
            if current_scale == (5,5):
                screen.blit(x_img, (row * 120, col * 120))
            if current_scale == (8,8):
                screen.blit(x_img, (row * 75, col * 75))
            current_player = players[1] 
            
        elif current_player == players[1]:
            board[row][col] = current_player
            if current_scale == (3,3):
                screen.blit(o_img, (row * 200, col * 200))
            if current_scale == (5,5):
                screen.blit(o_img, (row * 120, col * 120))
            if current_scale == (8,8):
                screen.blit(o_img, (row * 75, col * 75))
            current_player = players[0]
    except:
        pass

def checkWin(board):
    if current_scale == (3,3):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return True
            if board[0][i] == board[1][i] == board[2][i] != 0:
                return True
        if board[0][0] == board[1][1] == board[2][2] != 0:
            return True
        if board[0][2] == board[1][1] == board[2][0] != 0:
            return True
    if current_scale == (5,5):
        for i in range(5):
            for j in range(5 - how_many_needed_to_win + 1):
                if all(board[i][j+k] == board[i][j+k+1] != 0 for k in range(how_many_needed_to_win - 1)):
                    return True
                if all(board[j+k][i] == board[j+k+1][i] != 0 for k in range(how_many_needed_to_win - 1)):
                    return True
        for i in range(5 - how_many_needed_to_win + 1):
            if all(board[i+k][i+k] == board[i+k+1][i+k+1] != 0 for k in range(how_many_needed_to_win - 1)):
                return True
            if all(board[i+k][4-i-k] == board[i+k+1][4-i-k-1] != 0 for k in range(how_many_needed_to_win - 1)):
                return True
    if current_scale == (8,8):
        for i in range(8):
            for j in range(8 - how_many_needed_to_win + 1):
                if all(board[i][j+k] == board[i][j+k+1] != 0 for k in range(how_many_needed_to_win - 1)):
                    return True
                if all(board[j+k][i] == board[j+k+1][i] != 0 for k in range(how_many_needed_to_win - 1)):
                    return True
        for i in range(8 - how_many_needed_to_win + 1):
            if all(board[i+k][i+k] == board[i+k+1][i+k+1] != 0 for k in range(how_many_needed_to_win - 1)):
                return True
            if all(board[i+k][7-i-k] == board[i+k+1][7-i-k-1] != 0 for k in range(how_many_needed_to_win - 1)):
                return True
    
def getUsersClick():
    x, y = pg.mouse.get_pos()
    if current_scale == (3,3):
        row = x // 200
        col = y // 200
    if current_scale == (5,5):
        row = x // 120
        col = y // 120
    if current_scale == (8,8):
        row = x // 75
        col = y // 75
    return row, col

def changeScale(scale):
    global current_scale
    current_scale = scale
    figureOutScale(current_scale)
    drawGrid(current_scale) 

screen.fill("aquamarine3")
figureOutScale(current_scale)
drawGrid(current_scale)

#loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_e):
            running = False
            sys.exit()

    #draw x and o
    if pg.mouse.get_pressed()[0]:
        row, col = getUsersClick()
        drawXO(row, col)
        
    #check for win
    if checkWin(board):
        pg.draw.rect(screen, "aquamarine3", (0, 0, 600, 600))

        textsurface = font.render(current_player + ' wins', True, (0, 0, 0))
        screen.blit(textsurface,(150,250))
        
        pg.display.flip()
        pg.time.wait(2200)
        screen.fill("aquamarine3")
        
        figureOutScale(current_scale)
        drawGrid(current_scale)
        player_points[current_player] += 1
        current_player = players[1]
    
    #check for draw
    if all(i != 0 for row in board for i in row):
        pg.draw.rect(screen, "aquamarine3", (0, 0, 600, 600))
       
        textsurface = font.render('Draw', True, (0, 0, 0))
        screen.blit(textsurface,(250,250))
        
        pg.display.flip()
        pg.time.wait(2200)
        screen.fill("aquamarine3")
        
        figureOutScale(current_scale)
        drawGrid(current_scale)
        current_player = players[1]
        draws += 1

    #buttons
    pg.draw.rect(screen, "darkslategray4", (0, 610, 950, 100))
    textsurface = font.render('[ + ] Change scale [ - ]', True, (0, 0, 0))
    screen.blit(textsurface,(50,620))
    if pg.mouse.get_pressed()[0]:
        x, y = pg.mouse.get_pos()
        if y > 610:
            if 50 < x < 125:
                pg.draw.rect(screen, "aquamarine3", (0, 0, 600, 600))
                if index != 2:
                    index += 1
                changeScale(scales[index])
            
            if 475 < x < 545:
                pg.draw.rect(screen, "aquamarine3", (0, 0, 600, 600))
                if index != 0:
                    index -= 1
                changeScale(scales[index])
                  
    if current_scale == (5,5):
        how_many_needed_to_win = 4
    if current_scale == (8,8):
        how_many_needed_to_win = 5  

    # side panel
    pg.draw.rect(screen, "darkslategray3", (650, 0, 350, 600))
    for i, player in enumerate(players):
        textsurface = font.render(player + ': ' + str(player_points[player]), True, (0, 0, 0))
        screen.blit(textsurface,(700,100 + (i * 100)-70))
        
    drawstext = font.render('Draws: ' + str(draws), True, (0, 0, 0))
    screen.blit(drawstext,(700,620))

    
    
    
    ############################################################################################################
    pg.display.flip()
    clock.tick(12)
