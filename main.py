#left/right to move, up to speed up, down to drop, space to rotate
#"tetrominoes": 2 5 J L T | □
#points: single = 100, double = 300, triple = 500, tetris(4?) = 800
#ghost piece (opt. and later.)


import pygame
from random import *
pygame.init()
from tetrominoes import Tetromino

#Screen
screen = pygame.display.set_mode((1920,1080))

#Clock
clock = pygame.time.Clock()
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
time = 0
speed = 5 #15

#Score
score = 0
font = pygame.font.SysFont('chalkduster.ttf', 100)
score_text = font.render('SCORE: ' + str(score), True, "white")
cleared = 0
add_points = 0

# 10x20 grid
#1 means activated (not just indicating where to draw)
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

piece = Tetromino()

while True:
    screen.fill('black')
    clock.tick(speed)
    screen.blit(score_text, (1550, 50))

    for event in pygame.event.get():
        if event.type == timer_event:
            time += 1

        if event.type == pygame.QUIT:
            exit()

        def draw_grid(screen):
            i = 0
            j = 0
            for row in grid:
                #print(row)
                j = 0
                for block in row:
                        #print(block)
                        if block == 1:
                            rect = pygame.Rect(50*j, 50*i, 48, 48)
                            pygame.draw.rect(screen, 'white', rect)  #i forgot how color works ._.
                        j += 1

                i += 1
                #??

    #show pieces & how they move (from class)
    if piece.can_move == False:
        #grid: old grid that stores what the board looks like before the new piece is added
        #show_grid: new grid that shows the new piece moving on top of the old grid
        piece.tetromino_z()
        piece.can_move = True
    piece.movement(grid)
    piece.timed_mov(grid, time)
    piece.borders(grid)
    piece.update(grid)

    #Scoring
    #clear row
    for row in grid:
        if row == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            cleared +=1
            if cleared > 1:
                add_points = 200
            if cleared > 3:
                add_points = 300
            score += 100 + add_points
    cleared = 0

    if score % 1500:
        speed += 2

    draw_grid(screen)
    pygame.display.update()
#generate random block in center top of screen

#probably make a speed variable
#constantly go down, so row = 0 and then for every speed(??), grid[row][column]=0 and grid[row+1][column]=1
#L or R would be grid[row][column-1] or grid[row][column+1] (except for @ edge)
#do i have to make a thing for each rotation for each block?
#

