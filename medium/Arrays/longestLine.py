"""

562. Longest Line of Consecutive One in Matrix

1. check for Max consequtive ones in each row
2. check for max consequtive ones in each col
3. check for max consequtive one in all diagonals
4. check for max consequtive one in all anti-diagonals

"""



class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        


        def checkrow():
            
            m = 0
            
            for x in M:
                
                count = 0
                
                for y in x:
                    if y == 1:
                        count +=1
                    else:
                        m = max(m,count)
                        count = 0
                m = max(m,count)
            
            return max(m,count)
        
        def checkCol():
            m = 0
            for c in range(0,len(M[0])):
                count = 0
                
                for r in range(0,len(M)):
                    
                    if M[r][c] == 1:
                        count+=1
                    else:
                        m = max(m,count)
                        count = 0
                
                m = max(m,count)
            
            return max(m,count)
        
        def checkdiag(r,c):
            m = 0
            count = 0
            while r < len(M) and c < len(M[r]):
                
                if M[r][c] == 1:
                    count+=1
                else:
                    m = max(count,m)
                    count = 0
                
                r+=1
                c+=1
            m = max(count,m)
            
            
            return max(m,count)
        
        def checkantidiag(r,c):
            m = 0
            count = 0
            while r < len(M) and c >=0:
                
                if M[r][c] == 1:
                    count+=1
                else:
                    m = max(m,count)
                    count = 0
                
            
                r+=1
                c-=1
            
            return max(m,count)
                  
        m = 0
        
        if len(M) == 0:
            return m
        
        for r in range(0,len(M)):
            
            m = max(m,checkdiag(r,0))
        
        for c in range(0,len(M[0])):
            m = max(m, checkdiag(0,c))
        
        for r in range(0,len(M)):

            m = max(m,checkantidiag(r,len(M[r])-1))
        
        c = len(M[0])-1
        
        while c >= 0:
            
            m = max(m,checkantidiag(0,c))
            c-=1
   
        return max(checkrow(),checkCol(),m)
