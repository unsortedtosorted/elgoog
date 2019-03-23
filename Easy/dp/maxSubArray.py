"""

53. Maximum Subarray

Algo:

1. for index i:
    if sum till i-1>0:
        s[i] = s[i-1] + arr[i]
        else:
        s[i] = a[i]
    
    
    return max of s
    
    Runtime : O(N)

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = [-sys.maxsize-1]
        def dp(nums,i):
            
            temp = nums[i]
            temp2 = 0
            if i-1>=0 :
                temp2 = dp(nums,i-1)
            
            if  temp2 > 0:
                temp+=temp2
            
            m[0] = max(m[0],temp)
            return temp
        
        
        dp(nums, len(nums)-1)
        return m[0]
            
