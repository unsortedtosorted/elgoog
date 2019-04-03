"""
494. Target Sum

if end of array reached and remain == 0:
    return 1
else:
    return 0
    
    
    dp equation : return ( ways to reach 0 with (remain - curr) + ways to reach 0 with (remain + curr))

"""



class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        memo = {}
        def checksum(ind,remain):
            
            if (ind,remain) in memo:
                return memo[(ind,remain)]
            
            if ind == len(nums): 
                if remain == 0:
                    return 1
                else:
                    return 0
            
            if ind+1 <= len(nums):
                l = checksum(ind+1,remain-nums[ind])
                r = checksum(ind+1,remain+nums[ind])
                memo[(ind,remain)] = l+r
                
                return  memo[(ind,remain)]
                
        return checksum(0,S)
