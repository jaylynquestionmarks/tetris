import pygame

class Tetromino():
    #does class mean that the code runs for everything in this class
    def __init__(self):
        self.can_move = False
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
    def update(self, grid):
        grid[self.block1_row][self.block1_column] = 1
        grid[self.block2_row][self.block2_column] = 1
        grid[self.block3_row][self.block3_column] = 1
        grid[self.block4_row][self.block4_column] = 1

    #im going to forget to pass in grid
    def tetromino_z(self):
        #appear in grid[0][3], grid[0][4], grid[1][4], and grid[1][5]?
        self.block1_row = 0
        self.block1_column = 3
        self.block2_row = 0
        self.block2_column = 4
        self.block3_row = 1
        self.block3_column = 4
        self.block4_row = 1
        self.block4_column = 5

    def movement(self, grid):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # left edge
            if self.block1_column != 0 and self.block2_column != 0 and self.block3_column != 0 and self.block4_column != 0:
                #collision
                if min(self.block1_column, self.block2_column, self.block3_column, self.block4_column)-1 != 1:
                    #print columns every time you move left
                    print(self.block1_column, self.block2_column, self.block3_column, self.block4_column)
                    #clear the previous position
                    grid[self.block1_row][self.block1_column] = 0
                    grid[self.block2_row][self.block2_column] = 0
                    grid[self.block3_row][self.block3_column] = 0
                    grid[self.block4_row][self.block4_column] = 0
                    # move
                    self.block1_column -= 1
                    self.block2_column -= 1
                    self.block3_column -= 1
                    self.block4_column -= 1

        if keys[pygame.K_RIGHT]:
            #border: right edge logic (in if)
            if self.block1_column != 9 and self.block2_column != 9 and self.block3_column != 9 and self.block4_column != 9:
                if max(self.block1_column, self.block2_column, self.block3_column, self.block4_column) + 1 != 1:
                    # clear the previous position
                    grid[self.block1_row][self.block1_column] = 0
                    grid[self.block2_row][self.block2_column] = 0
                    grid[self.block3_row][self.block3_column] = 0
                    grid[self.block4_row][self.block4_column] = 0
                    # move
                    self.block1_column += 1
                    self.block2_column += 1
                    self.block3_column += 1
                    self.block4_column += 1

        #for i & j 0-->1
        #rotate
        if keys[pygame.K_r]:
            # clear the previous position
            grid[self.block1_row][self.block1_column] = 0
            grid[self.block2_row][self.block2_column] = 0
            grid[self.block3_row][self.block3_column] = 0
            grid[self.block4_row][self.block4_column] = 0
            #rotate
            if self.rotation_num == 0:
                self.block1_row -= 1
                self.block1_column += 1
                self.block3_row -= 1
                self.block3_column -= 1
                self.block4_column -= 2
                self.rotation_num += 1
            elif self.rotation_num == 1:
                self.block1_row += 1
                self.block1_column -= 1
                self.block3_row += 1
                self.block3_column += 1
                self.block4_column += 2
                self.rotation_num = 0
        #tetromino_5
        #tetromino_J
        #tetromino_L
        #tetromino_T
        #tetromino_|
        #tetromino_□
        # from tetrominoes choose random(0-6)
        #random.choice(tetrominoes_list)

    def borders(self, grid):
        if self.block1_row == 18 or self.block2_row == 18 or self.block3_row == 18 or self.block4_row == 18:
            self.can_move = False
            print(self.can_move)

        # stack
        # 12 13 14 23 24 34
        if self.block1_column == self.block2_column:
            if grid[max(self.block1_row, self.block2_row) + 1][self.block1_column] == 1 or \
                    grid[self.block3_row + 1][self.block3_column] == 1 or grid[self.block4_row + 1][
                self.block4_column] == 1:
                self.can_move = False
        if self.block1_column == self.block3_column:
            if grid[max(self.block1_row, self.block3_row) + 1][self.block1_column] == 1 or \
                    grid[self.block2_row + 1][self.block2_column] == 1 or grid[self.block4_row + 1][
                self.block4_column] == 1:
                self.can_move = False
        if self.block1_column == self.block4_column:
            if grid[max(self.block1_row, self.block4_row) + 1][self.block1_column] == 1 or \
                    grid[self.block2_row + 1][self.block2_column] == 1 or grid[self.block3_row + 1][
                self.block3_column] == 1:
                self.can_move = False
        if self.block2_column == self.block3_column:
            if grid[max(self.block2_row, self.block3_row) + 1][self.block2_column] == 1 or \
                    grid[self.block1_row + 1][self.block1_column] == 1 or grid[self.block4_row + 1][
                self.block4_column] == 1:
                self.can_move = False
                #print("detect", max(self.block2_row, self.block3_row))
        if self.block2_column == self.block4_column:
            if grid[max(self.block2_row, self.block4_row) + 1][self.block2_column] == 1 or \
                    grid[self.block1_row + 1][self.block1_column] == 1 or grid[self.block3_row + 1][
                self.block3_column] == 1:
                self.can_move = False
        if self.block3_column == self.block4_column:
            if grid[max(self.block3_row, self.block4_row) + 1][self.block1_column] == 1 or \
                    grid[self.block1_row + 1][self.block3_column] == 1 or grid[self.block2_row + 1][
                self.block2_column] == 1:
                self.can_move = False

    def timed_mov(self, grid, time):
        if time % 2 == 0 and self.can_move == True:
            #clear the previous position
            grid[self.block1_row][self.block1_column] = 0
            grid[self.block2_row][self.block2_column] = 0
            grid[self.block3_row][self.block3_column] = 0
            grid[self.block4_row][self.block4_column] = 0
            #move down a row
            self.block1_row += 1
            self.block2_row += 1
            self.block3_row += 1
            self.block4_row += 1
            #print("move", max(self.block2_row, self.block3_row))
        #clear
