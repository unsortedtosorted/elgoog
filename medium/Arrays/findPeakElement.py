class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        
        for x in range(0,len(nums)):
            
            
            curr = nums[x]
            
            if x == len(nums)-1:
                nex = -sys.maxsize-1
            else:
                nex = nums[x+1]

            if curr>nex:
                return x
