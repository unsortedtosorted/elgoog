"""
441. Arranging Coins

"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <=1:
            return n
        
        i = 1
        flag = 0
        
        while n >= i:
            n-=i
            i+=1
            flag+=1
        
        return flag
