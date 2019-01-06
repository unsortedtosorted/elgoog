"""

1. Get mid, if arr[mid]==target, return mid
2. If mid not equal to target:
   2.1 get start and stop of left half
    2.1.1 if left half is sorted and target in it, l=leftstart, r=right start
    2.1.2 if left half is sorted but target not in left half, then l = mid+1
   
   2.2 get stat and stop of right half
    2.2.1 if right half is sorted and number is in right half, l=right start and r=right stop
    2.2.2 if right half is sorted and number is not in right half, r=mid-1
   
   
"""








class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l=0
        
        r=len(nums)-1
        
        while l<=r:
            
            mid=(l+r)//2
            
            

            if nums[mid]==target:
                return mid
            
            #get start stop of left half
            leftstart=l
            leftstop=l
            if mid-1>l:
                leftstop=mid-1
            
            
            
            #get start and stop of right half
            rightstart=r
            rightstop=r
            
            if mid+1<r:
                rightstart=mid+1

            #left half is sorted
            if nums[leftstart]<=nums[leftstop]:
                #if target is in left sorted half
                if target>=nums[leftstart] and target<=nums[leftstop]:
                    
                    l=leftstart
                    r=leftstop
                else:
                    l=mid+1
                    continue
                
                
            #right half is sorted
            if nums[rightstart]<=nums[rightstop]:

                #if target is in right sorted half
                if target>=nums[rightstart] and target<=nums[rightstop]:
                    
                    l=rightstart
                    r=rightstop
                else:
                   
                    r=mid-1
        return -1
            
            
            
