"""

198. House Robber

Find max sum if cannot rob two adjacent houses.

1. if 1 house, sum = a[0]
2. if 2 house, sum = max(a[0],a[1])
3. if 3 house, sum = max(rob(1),a[2]+rob(0))

there dp equation for k houses is max(rob(k-1),a[k]+rob(k-2))



"""



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        self.m = {}

        def dp(k):
            
            if k in self.m:
                return self.m[k]
            
            if k == 0:
                self.m[k] = nums[k]
                return nums[k]
            elif k == 1:
                self.m[k] = max(nums[0],nums[1])
                return self.m[k]
            
            else:
                self.m[k] = max(dp(k-1), nums[k]+dp(k-2))
                return self.m[k]

        if len(nums)==0:
            return 0
        
        return dp(len(nums)-1)
