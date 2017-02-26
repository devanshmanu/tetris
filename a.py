from random import randint
import sys
import select
import math
import getch

from a1 import *









def rotatecheck():
    cell=100
    if board.checkPiecePos(block, block.BlockTop, block.BlockLeft) is not 0:
            board.fillPiecePos(block, block.BlockTop, block.BlockLeft)
    else:
        if cell == 1:
            return "X"
        elif cell == 2:
            return "X"
        else:
            return " "
    pass

def movedownchk():
    board.remove(block, block.BlockTop, block.BlockLeft)
    if board.checkPiecePos(block, block.BlockTop+1, block.BlockLeft) != 0:
        return 1
    else:
        return 0
    pass

class Block(object):

    def __init__(self, BlockHeight, BlockWidth, BlockTop=None, BlockLeft=None):
        self.BlockTop = BlockTop
        self.BlockLeft = BlockLeft
        self.BlockHeight = BlockHeight
        self.matrix = [[1] * BlockWidth] + [[0] * (BlockWidth / 2) + [1] + [0] * (BlockWidth - BlockWidth / 2 - 1)] * (BlockHeight-1)
        self.BlockWidth = BlockWidth


    def rotate(self,board):
        board.remove(block, block.BlockTop, block.BlockLeft)
        self.matrix = zip(*self.matrix[::-1])
        rotatecheck()
        
       



    def moveRight(self,board,num):
        board.remove(block, block.BlockTop, block.BlockLeft)
        if num == 1:
            if board.checkPiecePos(block, block.BlockTop, block.BlockLeft+1):
                for ri in range(len(self.matrix)):
                    for ci in range(len(self.matrix[ri])):
                        board.matrix[block.BlockTop + ri][block.BlockLeft+1 + ci] += self.matrix[ri][ci]
                self.BlockLeft = block.BlockLeft+1
                self.BlockTop = block.BlockTop
            else:
                for ri in range(len(self.matrix)):
                    for ci in range(len(self.matrix[ri])):
                        board.matrix[block.BlockTop + ri][block.BlockLeft + ci] += self.matrix[ri][ci]
                self.BlockLeft = block.BlockLeft
                self.BlockTop = block.BlockTop

        

    def moveLeft(self,board,num):
        board.remove(block, block.BlockTop, block.BlockLeft)
        if num == 0:
            if board.checkPiecePos(block, block.BlockTop, block.BlockLeft-1):
                for ri in range(len(self.matrix)):
                    for ci in range(len(self.matrix[ri])):
                        board.matrix[block.BlockTop + ri][block.BlockLeft-1 + ci] += self.matrix[ri][ci]
                self.BlockLeft = block.BlockLeft-1
                self.BlockTop = block.BlockTop
            else:
                for ri in range(len(self.matrix)):
                    for ci in range(len(self.matrix[ri])):
                        board.matrix[block.BlockTop + ri][block.BlockLeft + ci] += self.matrix[ri][ci]
                self.BlockLeft = block.BlockLeft
                self.BlockTop = block.BlockTop

    def move_down(self,board):
        
        checker = movedownchk()
        
        if checker == 1:
            for ri in range(len(self.matrix)):
                for ci in range(len(self.matrix[ri])):
                    board.matrix[block.BlockTop+1 + ri][block.BlockLeft + ci] += self.matrix[ri][ci]
            self.BlockLeft = block.BlockLeft
            self.BlockTop = block.BlockTop+1
        else:
            for ri in range(len(self.matrix)):
                for ci in range(len(self.matrix[ri])):
                    board.matrix[block.BlockTop + ri][block.BlockLeft + ci] += self.matrix[ri][ci]
            self.BlockLeft = block.BlockLeft
            self.BlockTop = block.BlockTop
            raise Exception






    def draw(self,cell):
        if cell == 1:
            return "X"
        elif cell == 2:
            return "X"
        else:
            return " "
        #return BRICK if cell == 1 else SPACE


    def placeontop(self,board):
        self.BlockTop = 0
        self.BlockLeft = randomised(1, board.BlockWidth-block.BlockWidth)
        if board.checkPiecePos(block, self.BlockTop, self.BlockLeft):
            board.fillPiecePos(block, self.BlockTop, self.BlockLeft)
        else:
            raise Exception

def var_fill_zero():
    var_fill=0
    return var_fill
    pass  

def total_zero():
    total=0
    return total
    pass

class Board(object):

    def __init__(self, BlockHeight=30, BlockWidth=32):
        self.BlockHeight = BlockHeight
        self.BlockWidth = BlockWidth
        self.matrix = [[1] + [0 for _ in range(BlockWidth)] + [2] for __ in range(BlockHeight)] + [[1 for _ in range(BlockWidth + 2)]]

    def __str__(self):
        slfstr = ''.join(list(block.draw(cell) for cell in range(30)))
        for x in self.matrix[1:-1]:
            slfstr += NEWLINE
            slfstr += ''.join(list(block.draw(cell) for cell in x))
        slfstr += NEWLINE
        slfstr += ''.join(list(block.draw(cell) for cell in self.matrix[-1]))
        return slfstr

    def checkPiecePos(self, block, row, col):
        try:
            return all(block.matrix[ri][ci] + self.matrix[row + ri][col + ci] in (0, 1)
                for ri in range(len(block.matrix))
                    for ci in range(len(block.matrix[ri])))
        except IndexError:
            return False

    def fillPiecePos(self, block, y, x):
        for ri in range(len(block.matrix)):
            for ci in range(len(block.matrix[ri])):
                self.matrix[y + ri][x + ci] += block.matrix[ri][ci]
        block.BlockLeft = x
        block.BlockTop = y
        jk1 = block.BlockHeight
        jk2 = block.BlockWidth
        answer1 = brickfunction(jk1)
        answer2 = brickfunction(jk2)


    def remove(self, block, y, x):
        for ri in range(len(block.matrix)):
            for ci in range(len(block.matrix[ri])):
                self.matrix[y + ri][x + ci] -= block.matrix[ri][ci]
        block.BlockLeft = x
        block.BlockTop = y
        ui = block.BlockHeight
        ui2 = block.BlockWidth
        a2 = brickfunction(ui)
        a3 = brickfunction(ui2)


    def printtheboard(self):
        print board
        pass

    @property
    def scorer(self):
        var_fill = var_fill_zero()
        total = total_zero()
        for row in self.matrix[:-1]:
            for cell in row[1:-1]:
                if cell is 0:
                    var_fill += 0
                elif cell < 0:
                    var_fill += 0
                elif cell == -100:
                    var_fill +=100
                else:
                    var_fill += 1
                total += 1
        var1 = float(var_fill)*100
        var2 = float(total)
        var3 = var1/var2
        var4 = math.ceil(var3*100)
        var5 = var4/100
        return var5















def clock(inputf):
    templist, _, __ = select.select([sys.stdin], [], [], inputf)
    if templist:
        x = sys.stdin.readline().strip()
        return x
    else:
        return ''




def init_print():
    #print R
    prompt = """
        a -> Left
        d -> RIGHT
        w -> ROTATE
        s -> DOWN
        """ 
    raw_input(prompt)
    pass


def automate():
    xx = clock(0.3)
    if GV == 0:
        print "You scored 0"
    else:
        print "You scored %s" % int(board.scorer * 100)
    print "Press 'q' to quit!"
    return xx

def randomised(a,b):
    x=a
    y=b
    ans=randint(a,b)
    return ans

def keyscaps(varC):
    if varC == 'A':
        block.moveLeft(board,0)
    elif varC == 'S':
        block.move_down(board)
    elif varC == 'W':
        block.rotate(board)
    elif varC == 'D':
        block.moveright(board,1)


def keys(var):
    if var == 'a':
        block.moveLeft(board,0)
    elif var == 's':
        block.move_down(board)
    elif var == 'w':
        block.rotate(board)
    elif var == 'd':
        block.moveRight(board,1)
    else:
        keyscaps(var)


def printboard():
    board.printtheboard()
    pass

if __name__ == '__main__':
    board = Board()
    syp1=2
    syp2=4
    stp1=randomised(syp1,syp2)
    stp2=randomised(syp1,syp2)
    block = Block(BlockHeight=stp1, BlockWidth=stp2)
    level = 1
    h = 30
    w = 32
    init_print()
    block.placeontop(board)
    printboard()
    x = automate()
    while x != 'q':
        try:
            block.move_down(board)
        except:
            yp1=2
            yp2=4
            tp1=randomised(yp1,yp2)
            tp2=randomised(yp1,yp2)
            block = Block(BlockHeight=tp1, BlockWidth=tp2)
            try:
                block.placeontop(board)
            except:
                print "GAME OVER"
                GV=2
                break
        if x is not None:
            keys(x)
            
        printboard()
        x=automate()
        GV=1