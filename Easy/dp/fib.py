class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        
        self.m = {}
        
        
        
        
        def fibo(n):
            if n in self.m:
                return self.m[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            x=fibo(n-1)+fibo(n-2)
            self.m[n]=x
            return x
        
        return fibo(N)
