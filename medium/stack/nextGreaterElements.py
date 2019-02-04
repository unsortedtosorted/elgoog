
"""
503. Next Greater Element II

1. Find next greater element in the cyclic array

Algo:
  1. start from the end, if element with index on top of stack is greater than curr number
      -- add it to the result
      -- add the index of element to the stack
      
      if curr number is greater than the element with index on stack, keep poping the stack
      -- if element greater found, add it to result
      -- add elements index to the top of the stack
      
  2. Do step 1 again since the array is cyclic and some values from step one will be wrong.
  
  Run time : O(N)
  space : O(N)


"""





class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack = []
        r = [-1]*len(nums)

        for x in range(0,2):
            i = len(nums)-1
            
            while i>=0:
            
                #if smaller than top then push
                while stack and nums[stack[-1]]<=nums[i]:
                    stack.pop()

                #if greater than top, first pop then push
                if stack:
                    r[i]=nums[stack[-1]]
            
                stack.append(i)
                i-=1

        return (r)
