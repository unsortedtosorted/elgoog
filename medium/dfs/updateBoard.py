"""
529. Minesweeper

1. check current position:  
    -- if 'M' , change to X and return
    -- if no mines at any neighbor, change to 'B' and check all neighbor
    -- if mines at adjacent neighbor, change to in(mines) return

"""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        seen = set()
        
        def getadjMines(r,c):
            
            numMines = 0
            #check above
            if r-1 >=0:
                if board[r-1][c] == 'M':
                    numMines+=1
                    
            #check below
            if r+1 <len(board):
                if board[r+1][c] == 'M':
                    numMines+=1

            #left
            if c-1 >=0:
                if board[r][c-1] == 'M':
                    numMines+=1

            #check right
            if c+1 < len(board[r]):
                if board[r][c+1] == 'M':
                    numMines+=1
            

            
            if r-1 >= 0:
                #check top left
                if c - 1 >=0:
                    if board[r-1][c-1] == 'M':
                        numMines+=1
                #check top right
                if c + 1 < len(board[r]) :
                    if board[r-1][c+1] == 'M':
                        numMines+=1
                        

            
            if r+1 < len(board):
                #check bottom left
                if c - 1 >=0:
                    if board[r+1][c-1] == 'M':
                        numMines+=1
                #check bottom right
                if c + 1 < len(board[r]) :
                    if board[r+1][c+1] == 'M':
                        numMines+=1
            
            return numMines

        def check(r,c):
            
            if r < 0 or c < 0:
                return
            if r >= len(board) or c >= len(board[r]):
                return 
            
            if (r,c) in seen:
                return
            seen.add((r,c))
            
            if board[r][c] == 'M':
                board[r][c] = 'X'
            
                return
            else:
                n = getadjMines(r,c)
                
                if n == 0:
                    board[r][c] = 'B'
                    #check all neighbors
                    check(r+1,c)
                    check(r-1,c)
                    check(r,c-1)
                    check(r,c+1)
                    check(r+1,c+1)
                    check(r-1,c-1)
                    check(r+1,c-1)
                    check(r-1,c+1)
                    
                
                else:
                    board[r][c] = str(n)
                
        check(click[0],click[1])

        return board
