"""
#280

1. If index i is even, it should be smaller than both next and prev value, if not swap
2. If index i is odd , it should be greater than both next and prev value, if not swap

Run time : O(n)
space : O(1)


"""



class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        for i,x in enumerate(nums):
            
            if i+1>=len(nums):
                continue
                
            if i%2==0:
                
                if nums[i]>nums[i-1]:
                    temp=nums[i-1]
                    nums[i-1]=nums[i]
                    nums[i]=temp
                    
                if nums[i]>nums[i+1]:
                    temp=nums[i+1]
                    nums[i+1]=nums[i]
                    nums[i]=temp
                
            else:
                
                if nums[i]<nums[i-1]:
                    temp=nums[i-1]
                    nums[i-1]=nums[i]
                    nums[i]=temp
                    
                if nums[i]<nums[i+1]:
                    temp=nums[i+1]
                    nums[i+1]=num
