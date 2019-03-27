"""

386. Lexicographical Numbers

Algo:
  
  1. if level is 0 the numbers are in range 1-9
  2. if level is 1 the numbers are in range 0-9
  3. apply back tracking algo:
       1           2    
     10 11      20    21
  100   101 200   210
  
  
  complexity : 10^N

"""


class Solution(object):
    def lexicalOrder(self, N):
        """
        :type n: int
        :rtype: List[int]
        """
        
        r = []
        
        def bt(prev,level):
            
            x = range(0,10)
            if level == 0:
                x = range(1,10)
            
            for i in x:
                
                prev = prev+str(i)
                
                if int(prev) <= N:
                    r.append(int(prev))
                    bt(prev,level+1)
                else:
                    return
                prev = prev[:-1]
            
        bt("",0)
        
        return r
