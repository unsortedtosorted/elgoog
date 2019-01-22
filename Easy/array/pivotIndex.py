class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp =0
        for x in nums:
            temp+=x
        
        temp2=0
        
        for i,x in enumerate(nums):
            temp-=x
            if temp2==temp:
                return i
            temp2+=x

        return -1
