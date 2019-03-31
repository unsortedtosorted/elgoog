"""
1031. Number of Enclaves

steps:

1. mark starting point of island in a hashmap to be 0 or 1 if on boundry
2. also store number of islands in another hasmap with parent of each island as key
3. if not on boundry (0 for boundry , 1 for not) add the number to result
4. return result


"""

class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        lands = {}
        islands = {}
        seen = set()
        
        def getLand(r,c,parent):
            
            if (r,c) in seen:
                return 
            seen.add((r,c))
            islands[parent]+=1
            if r == 0 or r == len(A)-1:
                lands[parent] = lands[parent]*0
            else:
                lands[parent] = lands[parent]*1
            
            if c == 0 or c == len(A[r])-1:
                lands[parent] = lands[parent]*0
            else:
                lands[parent] = lands[parent]*1
            
            
            #go up
            if r-1 >=0 and A[r-1][c] == 1:
                getLand(r-1,c,parent)

            #go down
            if r+1 < len(A) and A[r+1][c] ==1 :
                getLand(r+1,c,parent)
                
            #go left
            if c-1 >=0 and A[r][c-1] ==1 :
                getLand(r,c-1,parent)
                
            #go right
            if c+1 < len(A[r]) and A[r][c+1] ==1:
                getLand(r,c+1,parent)
        
        
        
        for i,x in enumerate(A):
            for j,y in enumerate(x):
                if (i,j) not in seen and A[i][j] == 1:
                    lands[(i,j)] = 1
                    islands[(i,j)] = 0
                    getLand(i,j,(i,j))
        
        r = 0
        for x in lands:
            if lands[x] != 0:
                r += islands[x]
        
        return r
