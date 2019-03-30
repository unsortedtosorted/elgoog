"""
348. Design Tic-Tac-Toe

1. create empty 2-D matrix
2. If move:
    update matrix
    check row
    check col
    check diag
    check anti diag

  complexity : O(N^2)
"""


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.grid = [ ([None] * n) for row in range(n) ]
        self.moves = 0
        
      
    def checkRow(self):
        
        count = 0
        
        for x in self.grid:
            
            if x[0]:
                
                temp = x[0]
                count = 0
                for y in x:
                    if y == temp:
                        count+=1
                    else:
                        break
                if count == self.n:
                    return temp
        
        if count == self.n:
            return temp
        return None
    
    def checkCol(self):
        
        for col in range(0,self.n):
            
            if self.grid[0][col]:
                
                temp = self.grid[0][col]
                count = 0
            else:
                continue
            
            for row in range(0,self.n):
                
                if self.grid[row][col] == temp:
                    count+=1
                else:
                    break
            
            if count == self.n:
                return temp
        
        return None
    
    def checkTopleft2right(self):
        
        r = 0
        c = 0
        
        if not self.grid[r][c]:
            return None
        temp = self.grid[r][c]
        count = 0 
        while r < len(self.grid) and c < len(self.grid):
            if self.grid[r][c] == temp:
                count+=1
            
            else:
                break
            
            
            r+=1
            c+=1
        
        if count == self.n:
            return temp
        else:
            return None
        
    def checkToprigh2left(self):
        
        r = 0
        c = len(self.grid)-1
        
        if not self.grid[r][c]:
            return None
        
        temp = self.grid[r][c]
        count = 0
        while r < len(self.grid) and c >= 0:
            
            if self.grid[r][c] == temp:
                count+=1
            else:
                break
            
            r+=1
            c-=1
            
            
        if count == self.n:
            return temp
        
        return None
                    
        
                            

    def move(self, row, col, player):
        
        
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
       
        if player == 1:
            self.grid[row][col] = 1
        else:
            self.grid[row][col] = 2
        
        self.moves +=1
        
        if self.moves >= 0:
            
            r = self.checkRow()
            if r :
                return r
            
            c = self.checkCol()
            if c:
                return c
            lr = self.checkTopleft2right()
            if lr:
                return lr
            rl = self.checkToprigh2left()
            if rl:
                return rl

        return 0
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
