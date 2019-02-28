"""
303. Range Sum Query - Immutable

prefix sum

"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.sums = [0]*(len(nums)+1)
        
        prev = 0
        i = 0
        
        for x in nums:
            prev = prev+x
            self.sums[i] = prev
            i+=1
            
        
        self.sums = self.sums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j]-self.sums[i-1]
