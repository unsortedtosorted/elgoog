"""
#228

Mem : O(N)
Run : O(N)

"""

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        
        if len(nums)==0:
            return nums
        temp = []
        
        
        i = 1
        
        while i<len(nums):
            temp.append(nums[i]-nums[i-1])
            i+=1
        
        
        s = 0
        
        prev=0
        r=[]
        
        for i,x in enumerate(temp):
            if x==1:
                prev=i+1
                continue
            else:
                if prev!=s:
                    r.append(str(nums[s])+"->"+str(nums[prev]))
                else:
                    r.append(str(nums[s]))
                s=i+1
                prev=i+1
        
        if prev!=s:
            r.append(str(nums[s])+"->"+str(nums[prev]))
        else:
            r.append(str(nums[s]))
        
        return r
