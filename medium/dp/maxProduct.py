"""
152. Maximum Product Subarray

if all number in array are positive, ans = prod of entire array
if number of -ve's are even ans = prod of entire array
if -ve numbers are odd: the solution gets tricky

At each index if we keep track of last-max and last-min, we know the answer is

max = max(curr*last-max,curr*last-min,curr)
min =  min(curr*last-max,curr*last-min,curr)

		dp(i) =  max(dp(i-1)[0]*arr[i],dp(i-1)[1]*arr[i],arr[i])

"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = [-sys.maxsize-1]
        def dp(i):
            
            if i == 0:
                m[0] = max(m[0],nums[i])
                return nums[i],nums[i]
            else:
                
                prev = dp(i-1)
                mi = min(nums[i],nums[i]*prev[0],nums[i]*prev[1])
                ma = max(nums[i],nums[i]*prev[0],nums[i]*prev[1])
                m[0] = max(m[0],ma)
                
                return mi,ma
        
        dp(len(nums)-1)[1]
        
        return m[0]
