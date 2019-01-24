"""
#46 Permutations

Given a list, generate all permutation.

Algorithm for function Permute(list l)

1. create an empty stack s.
2. for every element i in l:
    2.1 push i to stack
    2.2 remove i from l
    2.3 call Permute(l,p)
    2.4 pop i from stack
    2.5 if length of stack equal to l, add it to result

Runtime : O(N!)


"""

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
