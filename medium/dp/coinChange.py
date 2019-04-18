"""
322. Coin Change

dp eqaution:
    
    if coins are [1,2,5]
    way to reach N : min(1 + ways to reach(N-1),1 + ways to reach(N-2),1 + ways to reach(N-5))

"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        
        memo = {}
        
        def dp(remain):
            
            if remain in memo:
                return memo[remain]
            
            if remain == 0:
                return 0
            
            else:
                
                tr = sys.maxsize
                
                for x in coins:
                    
                    if remain-x >=0:
                        tr = min(tr,1+dp(remain-x))
                
                memo[remain] = tr
                
                return tr
        
        
        result = dp(amount)
        
        if result == sys.maxsize:
            return -1
        return result
