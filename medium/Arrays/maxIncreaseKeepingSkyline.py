"""
#807

Runtime : O(n^2)

"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        r = []
        c=[]
        for i,x in enumerate(grid):
            r.append(max(x))

        for col in range(0,len(grid[0])):
            m= -sys.maxsize-1
            for row in range(0,len(grid)):
                if grid[row][col]>m:
                    m = grid[row][col]
            
            c.append(m)

        temp=0
        
        for row in range(0,len(grid)):
            for col in range(0,len(grid[row])):
                temp += min(r[row],c[col])-grid[row][col]

        return temp
