"""
1020. Partition Array Into Three Parts With Equal Sum

1. check if entire sum is factor of 3
   if not return False
2. start adding number, if sum == avg, set sum = 0
    
   -- if this happens 2 times: return True
   

"""

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        
        a = sum(A)
        if a % 3 != 0:
            return False
        
        
        avg = a//3
        seen = 3
        temp = 0
        
       
        for x in A:
            
            temp +=x
            
            if temp == avg:
                seen-=1
                temp = 0
        
        if temp == avg:
            seen-=1
        
        return seen==0
            
