"""
64. Minimum Path Sum

dp equation :

    dp(r,c) = min(grid[r][c]+dp(r+1,c), grid[r][c]+dp(r,c+1))
    

"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        memo = {}
        
        def dp(r,c):
            
            if (r,c) in memo:
                return memo[(r,c)]
            if r == len(grid)-1 and c == len(grid[r])-1:
                memo[(r,c)] = grid[r][c]
                return memo[(r,c)]
            
            cr = sys.maxsize
            cd = sys.maxsize
            
            #get cost by down
            if r+1 < len(grid):
                cd = grid[r][c] + dp(r+1,c)
            
            #get cost by right
            if c+1 < len(grid[r]):
                cr = grid[r][c]+dp(r,c+1)
                
            memo[(r,c)] = min(cr,cd)
            return memo[(r,c)]
        
        
        return dp(0,0)
