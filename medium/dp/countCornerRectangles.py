"""
750. Number Of Corner Rectangles

1. If 1 is found at row,col
  1.1 check for 1's in same row, if 1 found at say row,col2:
    1.1.1 add map[col,col2] to answer
    1.1.2 add [col,col2] +=1 in the dictionary
2. return answer

Run time : O(R*C*C)

 

"""



from collections import Counter
class Solution(object):
  
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = Counter()
        ans = 0
        
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col:
                    for col2 in range(j+1,len(row)):
                        if grid[i][col2]:
                            ans += count[j,col2]
                            count[j,col2]+=1
        
        return ans

    def bruteForce(self,grid):
        self.count = 0
        
        def checkdiagonal(i,j):
            
            opx = i+1
            while opx<len(grid) :
                opy = j+1
                while opy<len(grid[i]):
                
                    if grid[opx][opy] == 1:
                    
                        bl = False
                        ur = False
                    
                        ##check bottom left
                        if grid[opx][j]==1:
                            bl = True
                        else:
                            opy+=1
                            continue
                     
                        #check upper right
                        if grid[i][opy] ==1:
                            ur = True
                        else:
                            opy+=1
                            continue

                        if bl and ur:
                            self.count+=1
                    opy+=1
                opx+=1

        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                if y==1:
                    checkdiagonal(i,j)

        return self.count
