class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.v={}
        
        def climb(n):
            
            if n in self.v:
                return self.v[n]
            if n<=0:
                return 0
            
            elif n==1:
                return 1
            
            elif n==2:
                return 2
            
            else:
                x =  climb(n-1)+climb(n-2)  
                self.v[n]=x
                return climb(n-1)+climb(n-2)
        
        return climb(n)
