"""
357. Count Numbers with Unique Digits

1. Do it using Perm and comb problem

n = 0 out 1
n = 1 out is 1+9
n = 2 out is 1+9+81
 ...

run time : O(n)

"""



class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def dp (n):
            
            if n==0:
                return 1
            if n == 1 :
                return 9
            else:
                
                temp = n-1
                mult = 9
                out = mult
                while temp>0:
                    out = out*mult
                    mult-=1
                    temp-=1
            
            return out
        temp = 0
       
        while n>=0:
            temp+=(dp(n))
            n-=1
        
        return temp
