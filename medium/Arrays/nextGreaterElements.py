"""
503. Next Greater Element II

1. for element at index i:
  1.1 search in i+1 to len of array, return if greater element is found
  1.2 search in 0 to i-1 of array, return if greater element is found
  1.3 return -1
  
  runtime : O(N^2)
  

"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        r = []
        def search(val,i):
           
            j = i+1
            
            while j < len(nums):
                x = nums[j]
                if x>val:
                    return x
                j+=1
            j=0
            
            while j<i:
                x=nums[j]
                if x>val :
                    return x
                j+=1
            return -1
    
        
        for i,x in enumerate(nums):
            left = nums[0:i]
            right = nums[i+1:]            
            r.append(search(x,i))

        return r
