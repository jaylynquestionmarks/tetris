#left/right to move, up to speed up, down to drop, space to rotate
#"tetrominoes": 2 5 J L T | □
#points: single = 100, double = 300, triple = 500, tetris(4?) = 800
#ghost piece (opt. and later.)

#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

#to-do: clear + make the other pieces
import pygame
from random import *
import copy
pygame.init()
from tetrominoes import Tetromino, Tetromino_z

#Screen
screen = pygame.display.set_mode((1920,1080))

#Clock
clock = pygame.time.Clock()
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
time = 0
speed = 8

#Score
score = 0
font = pygame.font.SysFont('chalkduster.ttf', 100)
cleared = 0
add_points = 0

# 10x20 grid
#1 means activated (not just indicating where to draw)
old_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]

show_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]

#draw_grids
def draw_grid(screen, show_grid):
    i = 0
    j = 0
    for row in show_grid:
        # print(row)
        j = 0
        for block in row:
            # print(block)
            if block == 1:
                rect = pygame.Rect(50 * j, 50 * i, 48, 48)
                pygame.draw.rect(screen, 'white', rect)  # i forgot how color works ._.
            j += 1
        i += 1
        # ??


# what is old grid\
def draw_old_grid(screen, old_grid):
    i = 0
    j = 0
    for row in old_grid:
        # print(row)
        j = 0
        for block in row:
            # print(block)
            if block == 1:
                rect = pygame.Rect(50 * j, 50 * i, 49, 49)
                pygame.draw.rect(screen, 'red', rect)  # i forgot how color works ._.
            j += 1
        i += 1

#set random piece
#generally use clock tick as seed to generate random number(except in security)
def random_piece():
    #pick random
    r = randrange(1,6)
    if r == 1:
        print("generated Z piece")
        return Tetromino_z()
    else:
        return Tetromino_z()

#set piece to random piece
piece = random_piece()

while True:
    screen.fill('black')
    clock.tick(speed)
    #score text
    score_text = font.render('SCORE: ' + str(score), True, "white")
    screen.blit(score_text, (1500, 50))

    if clock.get_time() == 100:
        print("time = 100")

    for event in pygame.event.get():
        if event.type == timer_event:
            time += 1

        if event.type == pygame.QUIT:
            exit()


    #show pieces & how they move (from class)
    if piece.can_move == False: #and clock.get_time() > 100:
        print("piece stop moving")
        #grid: old grid that stores what the board looks like before the new piece is added
        #show_grid: new grid that shows the new piece moving on top of the old grid
        old_grid = copy.deepcopy(show_grid)
        #generate new piece + set stuff
        print("new piece")
        piece = random_piece()
        piece.can_move = True
        piece.rotation_num = 0

        #Scoring
        #clear row
        #score goes up infinitely
        for index, row in enumerate(old_grid):
            print("row: " + str(index) + str(row))
            if row == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                cleared +=1
                print("score:", cleared)
                del old_grid[index]
                for i, row in enumerate(old_grid):
                    print("row", i, index)
                    if i < index and i != 0:
                        print("move down")
                        old_grid[i] = copy.deepcopy(old_grid[i - 1])
                old_grid[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                if cleared > 1:
                    add_points = 200
                if cleared > 3:
                    add_points = 300
                #score += 100 + add_points
        cleared = 0
        show_grid = copy.deepcopy(old_grid)

    piece.movement(old_grid, show_grid)
    piece.rotate(show_grid)
    piece.borders(old_grid, show_grid)
    piece.timed_mov(show_grid, time)
    show_grid = piece.update(show_grid)


    #game over
    for row in old_grid:
        if old_grid.index(row) == 0 and row !=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            # lose text
            game_over_text = font.render("GAME OVER  FINAL SCORE: " + str(score), True, "red")
            screen.blit(game_over_text, (0, 0))

    if score % 1500:
        speed += 2

#draw the grids..
    draw_grid(screen, show_grid)
    draw_old_grid(screen, old_grid)
    pygame.display.update()
#generate random block in center top of screen

#probably make a speed variable
#constantly go down, so row = 0 and then for every speed(??), grid[row][column]=0 and grid[row+1][column]=1
#L or R would be grid[row][column-1] or grid[row][column+1] (except for @ edge)
#do i have to make a thing for each rotation for each block?
#

