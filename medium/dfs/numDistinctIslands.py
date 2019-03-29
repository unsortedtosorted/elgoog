"""
694. Number of Distinct Islands

1. first get r,c list of all islands
2. get absolute shape of each island
3. compare shapes return result

"""





class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = {}
        seen = set()
        
        
        def getshape(r,c,key):
            
            if (r,c) in seen:
                return 
            
            seen.add((r,c))
            
            if grid[r][c] == 1:
                if key in m:
                    m[key].append((r,c))
                else:
                    m[key] =[(r,c)]
                    
            
            #check up
            if r-1>=0 and grid[r-1][c]==1:
                getshape(r-1,c,key)
            #check down
            if r+1 < len(grid) and grid[r+1][c] ==1 :
                getshape(r+1,c,key)
            #check left
            if c-1 >=0 and grid[r][c-1]==1:
                getshape(r,c-1,key)
            
            #check right
            if c+1 < len(grid[r]) and grid[r][c+1] ==1:
                getshape(r,c+1,key)
            
            
            
        
        
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                
                if y == 1 and (i,j) not in seen:
                    
                    getshape(i,j,(i,j))
       
        s = set()
        count = 0
        rs = {}
        
        for x in m:
            
            y = m[x]
            
            y = sorted(y, key = lambda y: y)
            
            r = y[0][0]
            c = y[0][1]
            
            i = 0
            temp = set()
            while i < len(y):
                temp.add((y[i][0]-r,y[i][1]-c))
                i+=1
            
            if tuple(temp) not in s:
                count+=1
                s.add(tuple(temp))
            
            
        return count
