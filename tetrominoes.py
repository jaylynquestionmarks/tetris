import pygame

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

    def movement(self, old_grid, show_grid):
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


    #works but having abstract class(ABC) would catch bugs and typos
    #Multiple Inheritance is generally complicated and :(, stick to single inheritance
    def rotate(self):
        pass

    def borders(self, old_grid, show_grid):
        if self.block1_row == 18 or self.block2_row == 18 or self.block3_row == 18 or self.block4_row == 18:
            self.can_move = False
            print(self.can_move)

        # stack
        # 12 13 14 23 24 34
        #list index out of range
        if old_grid[self.block1_row+1][self.block1_column] == 1 or old_grid[self.block2_row+1][self.block2_column] == 1 or old_grid[self.block3_row+1][self.block3_column] == 1 or old_grid[self.block4_row+1][self.block4_column] == 1:
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
        #tetromino_5
        #tetromino_J
        #tetromino_L
        #tetromino_T
        #tetromino_|
        #tetromino_□
        # from tetrominoes choose random(0-6)
        #random.choice(tetrominoes_list)