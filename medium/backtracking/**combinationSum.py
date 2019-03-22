"""
39. Combination Sum

1. generate all possible combinations
2. sort and remove duplicates from the list

"""

from collections import Counter 
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        
        def bt(r,remain):
            
            if remain == 0:
                result.append(list(r))
            if 0 > remain:
                return 
            
            for i,x in enumerate(candidates):
                
                temp = x
                r.append(x)
                bt(r,remain-x)
                r.pop()
                
            
        
        
        
        bt([],target)
        
        
        for i,x in enumerate(result):
            
            result[i] = sorted(x)
        
        
        
        def func(x):
            
            return len(x),x

        result = sorted(result,key = func)
        result2 = []
        prev = None
        
        for x in result:
            
            if x!= prev:
                result2.append(x)
                prev = x
                

        return result2
