from collections import deque

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        
        self.l=deque()
        self.r=[]
        
        def backtrack(num):
            for i,x in enumerate(num):
                self.l.append(x)
                backtrack(num[:i]+num[i+1:])
                if len(self.l)==len(nums):
                    self.r.append(list(self.l))
                self.l.pop()
         
        backtrack(nums)
        return self.r
