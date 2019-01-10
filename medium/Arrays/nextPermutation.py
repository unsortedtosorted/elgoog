class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i=len(nums)-2
        
        
        #find first element breaking the decreasing order sequence from right
        while i>-1:
            if nums[i]>=nums[i+1]:
                i-=1
            else:
                break
        
        
        if i==-1:
            nums.sort()
            return
        #swap i with the next largest value
        
        j=len(nums)-1 
        

        while j>-1:
            if nums[j]>nums[i]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                break
            else:
                j-=1
        

        #now reverse the order of all number after i
        start=i+1
        end=len(nums)-1
        
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
