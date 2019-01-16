class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def getpow(i,j):
            

            if j==0:
                return 1.0
            if j==1:
                return float(i)
            
            half = getpow(i,j//2)

            
            if j%2==0:
                return float(half*half)
            else:
                return float(half*half*i)
       
        
        r=1.0
        
        if n<0:
            x=1/x
            n=-n
        
        i=n
        return getpow(x,n)
        
