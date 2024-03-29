import pygame
import copy

class Tetromino():
    def __init__(self):
        self.can_move = True
        #hhhhhhhhhhhhhhhhh
        self.rotation_num = 0
        #each tetromino is 4 blocks
        self.block1_row = 0
        self.block1_column = 0
        self.block2_row = 0
        self.block2_column = 0
        self.block3_row = 0
        self.block3_column = 0
        self.block4_row = 0
        self.block4_column = 0

    #i have no idea what im doing
    def update(self, show_grid):
        show_grid[self.block1_row][self.block1_column] = 1
        show_grid[self.block2_row][self.block2_column] = 1
        show_grid[self.block3_row][self.block3_column] = 1
        show_grid[self.block4_row][self.block4_column] = 1
        return show_grid

    def movement(self, old_grid, show_grid, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # left edge
            if self.block1_column != 0 and self.block2_column != 0 and self.block3_column != 0 and self.block4_column != 0:
                #collision
                if old_grid[self.block1_row][self.block1_column-1] != 1 and old_grid[self.block2_row][self.block2_column-1] != 1 and old_grid[self.block3_row][self.block3_column-1] != 1 and old_grid[self.block4_row][self.block4_column-1] != 1:
                    #print columns every time you move left
                    print(self.block1_column, self.block2_column, self.block3_column, self.block4_column)
                    #clear the previous position
                    show_grid[self.block1_row][self.block1_column] = 0
                    show_grid[self.block2_row][self.block2_column] = 0
                    show_grid[self.block3_row][self.block3_column] = 0
                    show_grid[self.block4_row][self.block4_column] = 0
                    #move
                    self.block1_column -= 1
                    self.block2_column -= 1
                    self.block3_column -= 1
                    self.block4_column -= 1


        elif keys[pygame.K_RIGHT]:
            #border: right edge logic (in if)
            if self.block1_column != 9 and self.block2_column != 9 and self.block3_column != 9 and self.block4_column != 9:
                print("right1")
                if old_grid[self.block1_row][self.block1_column+1] != 1 and old_grid[self.block2_row][self.block2_column+1] != 1 and old_grid[self.block3_row][self.block3_column+1] != 1 and old_grid[self.block4_row][self.block4_column+1] != 1:
                    # clear the previous position
                    print("right2")
                    show_grid[self.block1_row][self.block1_column] = 0
                    show_grid[self.block2_row][self.block2_column] = 0
                    show_grid[self.block3_row][self.block3_column] = 0
                    show_grid[self.block4_row][self.block4_column] = 0
                    # move
                    self.block1_column += 1
                    self.block2_column += 1
                    self.block3_column += 1
                    self.block4_column += 1

        if keys[pygame.K_UP]:
            if old_grid[self.block1_row][self.block1_column + 1] != 1 and old_grid[self.block2_row][self.block2_column + 1] != 1 and old_grid[self.block3_row][self.block3_column + 1] != 1 and old_grid[self.block4_row][self.block4_column + 1] != 1:
                # clear the previous position
                show_grid[self.block1_row][self.block1_column] = 0
                show_grid[self.block2_row][self.block2_column] = 0
                show_grid[self.block3_row][self.block3_column] = 0
                show_grid[self.block4_row][self.block4_column] = 0
                #go downn
                self.block1_row += 1
                self.block2_row += 1
                self.block3_row += 1
                self.block4_row += 1

        if keys[pygame.K_SPACE]:
            #change while
            while self.can_move == True:
                speed = 100

    #works but having abstract class(ABC) would catch bugs and typos
    #Multiple Inheritance is generally complicated and :(, stick to single inheritance

    #speed up when hold space (because i dont want to think of the block coordinates rn)
    def speed_up(self, speed):
        keys = pygame.key.get_pressed()

    def rotate(self):
        pass

    def borders(self, old_grid, show_grid):
        #list index out of range
        if self.block1_row == 19 or self.block2_row == 19 or self.block3_row == 19 or self.block4_row == 19:
            self.can_move = False
            print(self.can_move)
        # stack
        # 12 13 14 23 24 34
        elif old_grid[self.block1_row+1][self.block1_column] == 1 or old_grid[self.block2_row+1][self.block2_column] == 1 or old_grid[self.block3_row+1][self.block3_column] == 1 or old_grid[self.block4_row+1][self.block4_column] == 1:
            self.can_move = False

    def timed_mov(self, show_grid, time):
        if time % 2 == 0 and self.can_move == True:
            #clear the previous position
            show_grid[self.block1_row][self.block1_column] = 0
            show_grid[self.block2_row][self.block2_column] = 0
            show_grid[self.block3_row][self.block3_column] = 0
            show_grid[self.block4_row][self.block4_column] = 0
            #move down a row
            self.block1_row += 1
            self.block2_row += 1
            self.block3_row += 1
            self.block4_row += 1
            #print("move", max(self.block2_row, self.block3_row))
        #clear

class Tetromino_z(Tetromino):
    def __init__(self):
        super(Tetromino_z, self).__init__()
        #appear in grid[0][3], grid[0][4], grid[1][4], and grid[1][5]?
        self.block1_row = 0
        self.block1_column = 3
        self.block2_row = 0
        self.block2_column = 4
        self.block3_row = 1
        self.block3_column = 4
        self.block4_row = 1
        self.block4_column = 5
   #im going to forget to pass in grid
    #make the tetrominoes subclasses
    
    #whichever block it is it will call that rotate
    def rotate(self, show_grid):
        keys = pygame.key.get_pressed()
        #rotate
        if keys[pygame.K_r]:
            # clear the previous position
            show_grid[self.block1_row][self.block1_column] = 0
            show_grid[self.block2_row][self.block2_column] = 0
            show_grid[self.block3_row][self.block3_column] = 0
            show_grid[self.block4_row][self.block4_column] = 0
            #rotate
            if self.rotation_num == 0:
                self.block1_row -= 1
                self.block1_column += 1
                self.block3_row -= 1
                self.block3_column -= 1
                self.block4_column -= 2
                self.rotation_num = 1
                #print("rotate1")
            elif self.rotation_num == 1:
                self.block1_row += 1
                self.block1_column -= 1
                self.block3_row += 1
                self.block3_column += 1
                self.block4_column += 2
                self.rotation_num = 0
                #print("rotate2")

# tetromino_S
class Tetromino_s(Tetromino):
    def __init__(self):
        super(Tetromino_s, self).__init__()
        # appear in grid[1][3], grid[1][4], grid[0][4], and grid[0][5]
        self.block1_row = 1
        self.block1_column = 3
        self.block2_row = 1
        self.block2_column = 4
        self.block3_row = 0
        self.block3_column = 4
        self.block4_row = 0
        self.block4_column = 5
        self.rotation_num = 0

    # whichever block it is it will call that rotate
    def rotate(self, show_grid):
        keys = pygame.key.get_pressed()
        # rotate
        if keys[pygame.K_r]:
            # clear the previous position
            show_grid[self.block1_row][self.block1_column] = 0
            show_grid[self.block2_row][self.block2_column] = 0
            show_grid[self.block3_row][self.block3_column] = 0
            show_grid[self.block4_row][self.block4_column] = 0
            # rotate
            if self.rotation_num == 0:
                self.block1_row -= 2
                self.block2_row -= 1
                self.block2_column -= 1
                self.block4_row += 1
                self.block4_column -= 1
                self.rotation_num += 1
                # print("rotate1")
            elif self.rotation_num == 1:
                self.block1_row += 2
                self.block2_row += 1
                self.block2_column += 1
                self.block4_row -= 1
                self.block4_column += 1
                self.rotation_num = 0
                # print("rotate2")

#tetromino_J
#appear in grid[0][3], grid[1][3], grid[1][4], and grid[1][5]
class Tetromino_j(Tetromino):
    def __init__(self):
        super(Tetromino_j, self).__init__()
        #appear in grid[0][3], grid[1][3], grid[1][4], and grid[1][5]
        self.block1_row = 0
        self.block1_column = 3
        self.block2_row = 1
        self.block2_column = 3
        self.block3_row = 1
        self.block3_column = 4
        self.block4_row = 1
        self.block4_column = 5
        self.rotation_num = 0

    # whichever block it is it will call that rotate
    def rotate(self, show_grid):
        keys = pygame.key.get_pressed()
        # rotate
        if keys[pygame.K_r]:
            # clear the previous position
            show_grid[self.block1_row][self.block1_column] = 0
            show_grid[self.block2_row][self.block2_column] = 0
            show_grid[self.block3_row][self.block3_column] = 0
            show_grid[self.block4_row][self.block4_column] = 0
            # rotate
            if self.rotation_num == 0:
                self.block1_column += 1
                self.block2_row -= 1
                self.block3_column -= 1
                self.block4_row += 1
                self.block4_column -= 2
                self.rotation_num = 1
                # print("rotate1")
            elif self.rotation_num == 1:
                self.block1_row += 1
                self.block2_column += 1
                self.block3_row -= 1
                self.block4_row -= 2
                self.block4_column -= 1
                self.rotation_num = 2
                # print("rotate2")
            elif self.rotation_num == 2:
                self.block1_column -= 1
                self.block2_row += 1
                self.block3_column += 1
                self.block4_row -= 1
                self.block4_column += 2
                self.rotation_num = 3
                # print("rotate3")
            elif self.rotation_num == 3:
                self.block1_row -= 1
                self.block2_column -= 1
                self.block3_row += 1
                self.block4_row += 2
                self.block4_column += 1
                self.rotation_num = 0
                # print("rotate4")
#tetromino_L
#appear in grid[0][5], grid[1][3], grid[1][4], and grid[1][5]
class Tetromino_l(Tetromino):
    def __init__(self):
        super(Tetromino_l, self).__init__()
        #appear in grid[0][5], grid[1][5], grid[1][4], and grid[1][3]
        self.block1_row = 0
        self.block1_column = 5
        self.block2_row = 1
        self.block2_column = 5
        self.block3_row = 1
        self.block3_column = 4
        self.block4_row = 1
        self.block4_column = 3
        self.rotation_num = 0

    # whichever block it is it will call that rotate
    def rotate(self, show_grid):
        keys = pygame.key.get_pressed()
        # rotate
        if keys[pygame.K_r]:
            # clear the previous position
            show_grid[self.block1_row][self.block1_column] = 0
            show_grid[self.block2_row][self.block2_column] = 0
            show_grid[self.block3_row][self.block3_column] = 0
            show_grid[self.block4_row][self.block4_column] = 0
            # rotate
            if self.rotation_num == 0:
                self.block1_row += 1
                self.block2_column -= 1
                self.block3_row -= 1
                self.block4_row -= 2
                self.block4_column += 1
                self.rotation_num = 1
                # print("rotate1")
            elif self.rotation_num == 1:
                self.block1_column -= 1
                self.block2_row -= 1
                self.block3_column += 1
                self.block4_row += 1
                self.block4_column += 2
                self.rotation_num = 2
                # print("rotate2")
            elif self.rotation_num == 2:
                self.block1_row -= 1
                self.block2_column += 1
                self.block3_row += 1
                self.block4_row += 2
                self.block4_column -= 1
                self.rotation_num = 3
                # print("rotate3")
            elif self.rotation_num == 3:
                self.block1_column += 1
                self.block2_row += 1
                self.block3_row -= 1
                self.block3_column -= 1
                self.block4_row -= 2
                self.block4_column -= 2
                self.rotation_num = 0
                # print("rotate4")

#tetromino_T
#appear in grid[0][4], grid[1][3], grid[1][4], and grid[1][5]
class Tetromino_t(Tetromino):
    def __init__(self):
        super(Tetromino_t, self).__init__()
        #appear in grid[0][5], grid[1][5], grid[1][4], and grid[1][3]
        self.block1_row = 0
        self.block1_column = 4
        self.block2_row = 1
        self.block2_column = 3
        self.block3_row = 1
        self.block3_column = 4
        self.block4_row = 1
        self.block4_column = 5
        self.rotation_num = 0

    # whichever block it is it will call that rotate
    def rotate(self, show_grid):
        keys = pygame.key.get_pressed()
        # rotate
        if keys[pygame.K_r]:
            # clear the previous position
            show_grid[self.block1_row][self.block1_column] = 0
            show_grid[self.block2_row][self.block2_column] = 0
            show_grid[self.block3_row][self.block3_column] = 0
            show_grid[self.block4_row][self.block4_column] = 0
            # rotate
            if self.rotation_num == 0:
                self.block1_row += 1
                self.block1_column += 1
                self.block2_row -= 1
                self.block2_column += 1
                self.block4_row += 1
                self.block4_column -= 1
                self.rotation_num = 1
                # print("rotate1")
            elif self.rotation_num == 1:
                self.block1_row += 1
                self.block1_column -= 1
                self.block2_row += 1
                self.block2_column += 1
                self.block4_row -= 1
                self.block4_column -= 1
                self.rotation_num = 2
                # print("rotate2")
            elif self.rotation_num == 2:
                self.block1_row -= 1
                self.block1_column -= 1
                self.block2_row += 1
                self.block2_column -= 1
                self.block4_row -= 1
                self.block4_column += 1
                self.rotation_num = 3
                # print("rotate3")
            elif self.rotation_num == 3:
                self.block1_row -= 1
                self.block1_column += 1
                self.block2_row -= 1
                self.block2_column -= 1
                self.block4_row += 1
                self.block4_column += 1
                self.rotation_num = 0
                # print("rotate4")

#tetromino_|
#appear in grid[0][3], grid[0][4], grid[0][5], and grid[0][6]
class Tetromino_line(Tetromino):
    def __init__(self):
        super(Tetromino_line, self).__init__()
        #appear in grid[0][5], grid[1][5], grid[1][4], and grid[1][3]
        self.block1_row = 0
        self.block1_column = 2
        self.block2_row = 0
        self.block2_column = 3
        self.block3_row = 0
        self.block3_column = 4
        self.block4_row = 0
        self.block4_column = 5
        self.rotation_num = 0

    # whichever block it is it will call that rotate
    def rotate(self, show_grid):
        keys = pygame.key.get_pressed()
        # rotate
        if keys[pygame.K_r]:
            # clear the previous position
            show_grid[self.block1_row][self.block1_column] = 0
            show_grid[self.block2_row][self.block2_column] = 0
            show_grid[self.block3_row][self.block3_column] = 0
            show_grid[self.block4_row][self.block4_column] = 0
            # rotate
            if self.rotation_num == 0:
                self.block1_row -= 1
                self.block1_column += 1
                self.block3_row += 1
                self.block3_column -= 1
                self.block4_row += 2
                self.block4_column -= 2
                self.rotation_num = 1
                # print("rotate1")
            elif self.rotation_num == 1:
                self.block1_row += 1
                self.block1_column -= 1
                self.block3_row -= 1
                self.block3_column += 1
                self.block4_row -= 2
                self.block4_column += 2
                self.rotation_num = 2
                # print("rotate2")
            elif self.rotation_num == 2:
                self.block1_row += 2
                self.block1_column += 2
                self.block2_row += 1
                self.block2_column += 1
                self.block4_row -= 1
                self.block4_column -= 1
                self.rotation_num = 3
                # print("rotate3")
            elif self.rotation_num == 3:
                self.block1_row -= 2
                self.block1_column -= 2
                self.block2_row -= 1
                self.block2_column -= 1
                self.block4_row += 1
                self.block4_column += 1
                self.rotation_num = 0
                # print("rotate4")

#tetromino_□
#appear in grid[0][4], grid[0][5], grid[1][4], and grid[1][5]
#no rotate!
class Tetromino_sq(Tetromino):
    def __init__(self):
        super(Tetromino_sq, self).__init__()
        #appear in grid[0][5], grid[1][5], grid[1][4], and grid[1][3]
        self.block1_row = 0
        self.block1_column = 4
        self.block2_row = 1
        self.block2_column = 4
        self.block3_row = 0
        self.block3_column = 5
        self.block4_row = 1
        self.block4_column = 5
    def rotate(self, show_grid):
        pass

#if self.rotation_num == 0:
'''
TEMPLATE:
if self.rotation_num == 0:
    self.block1_row += 1
    self.block1_column -= 3
    self.block2_row -= 1
    self.block2_column -= 1
    self.block3_row -= 1
    self.block3_column -= 1
    self.block4_row -= 2
    self.block4_column -= 1
    self.rotation_num = 1
    #print("rotate1")
elif self.rotation_num == 1:
    self.block1_row += 1
    self.block1_column -= 3
    self.block2_row -= 1
    self.block2_column -= 1
    self.block3_row -= 1
    self.block3_column -= 1
    self.block4_row -= 2
    self.block4_column -= 1
    self.rotation_num = 2
    #print("rotate2")
elif self.rotation_num == 2:
    self.block1_row += 1
    self.block1_column -= 3
    self.block2_row -= 1
    self.block2_column -= 1
    self.block3_row -= 1
    self.block3_column -= 1
    self.block4_row -= 2
    self.block4_column -= 1
    self.rotation_num = 3
    #print("rotate3")
elif self.rotation_num == 3:
    self.block1_row += 1
    self.block1_column -= 3
    self.block2_row -= 1
    self.block2_column -= 1
    self.block3_row -= 1
    self.block3_column -= 1
    self.block4_row -= 2
    self.block4_column -= 1
    self.rotation_num = 0
    #print("rotate4")
'''

