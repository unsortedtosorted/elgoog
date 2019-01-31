"""

419. Battleships in a Board

1. If X is found and not already seen:
  -increase count by 1
  - add to seen
  - check up
  - check down
  - check left
  - check right
2. return Count

Run Time : O(N)

"""




class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        self.seen =  set ()
        
        def getship(i,j):
            
            if (i,j) in self.seen:
                return
            self.seen.add((i,j))
            
            #check up
            if i-1>=0:
                if board[i-1][j] == 'X':
                    getship(i-1,j)
                    

            #check down
            if i+1<len(board):
                if board[i+1][j] == 'X':
                    getship(i+1,j)
                    
                
            #check left
            
            if j-1>=0:
                if board[i][j-1]== 'X':
                    getship(i,j-1)
                    
                
            #check right
            if j+1<len(board[i]):
                if board[i][j+1]== 'X':
                    getship(i,j+1)
                    
        count = 0
        
        for i,x in enumerate(board):
            for j,y in enumerate(x):
                if y == 'X' and (i,j) not in self.seen:
                    count+=1
                    getship(i,j)
        
        
        return count
        
