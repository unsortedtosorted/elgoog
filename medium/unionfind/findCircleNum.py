"""

547. Friend Circles


union and find take o(n) in worst case.


"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """ 
        parent = {}
        
        
        def find(val):
            
            if val not in parent:
                parent[val] = val
                return val
            else:
                
                temp = val
                
                while temp!=parent[temp]:
                    temp = parent[temp]
                
                parent[val] = temp
                return temp
        
        
        def union(val1,val2):
            
            parent[find(val1)] = find(val2)
        

        i = 0
        
        while i < len(M):
            
            j = 0
            
            while j < len(M[i]):
                
                if  M[i][j] == 1:
                    p1 = find(i)
                    p2 = find(j)
                    union(p1,p2) 
                
            
                j+=1
            print parent
            i+=1
        
        
        cir = set()
        
        for x in (parent):
            cir.add(find(parent[x]))
        
        return len(cir)
