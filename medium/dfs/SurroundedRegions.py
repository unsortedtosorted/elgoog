"""
#130. Surrounded Regions

  1. First find all the zeros on the edges of the rectangle
  2. If zero found, look for all connected zeros, if not seen, up , down , left and right
  3. add all the (row,col) tuple in the set for zeros not to be flipped
  4. Iterate the board again if found O and row,col not in seen set, flip it
  
  Run time : O (R*C)
  Space : O(R*C)

"""


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.seen = set()
        
        
        def dfs(row,col):
            
            if (row,col) in self.seen:
                return
            if board[row][col] =='O':

                self.seen.add((row,col))
                
                #check up
                if row-1>=0:
                    dfs(row-1,col)
                
                #check down
                if row+1<len(board):
                    dfs(row+1,col)
                
                
                #check left
                if col-1>=0:
                    dfs(row,col-1)
                
                
                #check right
                if col+1<len(board[row]):
                    dfs(row,col+1)
            
        
        def getInvalidOs():
            
            for row in range(0,len(board)):
                for col in range(0,len(board[row])):
                    if (row,col) in self.seen:
                        continue
                    else:
                        if row == 0 or col ==0 or row == len(board)-1 or col == len(board[row])-1:
                            dfs(row,col)
        

        getInvalidOs()
        
        for row in range(1,len(board)-1):
                for col in range(1,len(board[row])-1):
                    if (row,col) not in self.seen and board[row][col]=='O':
                        board[row][col] = 'X'
