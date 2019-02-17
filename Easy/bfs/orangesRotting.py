"""

994. Rotting Oranges


"""



class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        
        self.max = 0
        self.marked = set()
        
        def markadj(x,y,curr):
            
            
            if curr == 1 or curr == 0:
                return
            
            self.marked.add((x,y))
            #check top
            if x-1>=0 and grid[x-1][y] == 1 and ((x-1),y) not in self.marked:
                grid[x-1][y] = curr+1
                
            
            #check left
            if y-1>=0 and grid[x][y-1]==1  and ((x,y-1)) not in self.marked:
                grid[x][y-1] = curr+1
                
            
            #check right
            
            if y+1<len(grid[x]) and grid[x][y+1]==1 and ((x,y+1)) not in self.marked:
                grid[x][y+1] = curr+1
                
            
            #check bottom
            if x+1<len(grid) and grid[x+1][y]==1 and ((x+1,y)) not in self.marked:
                 grid[x+1][y] = curr+1
            
   
        curr = 2
    
        while (True):
            seen = 0
            print (grid)
            for i,x in enumerate(grid):
                for j,y in enumerate(x):
                    if y ==curr :
                        seen+=1
                        markadj(i,j,curr)
            if seen>0:
                curr+=1
            else:
                break
        
        temp = 0
        for i,x in enumerate(grid):
                for j,y in enumerate(x):
                    if y == 1 :
                        return -1
                    if y > temp:
                        temp = y
        
        if temp!=0:
            return temp-2
        
        return temp
