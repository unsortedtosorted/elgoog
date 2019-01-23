"""
#215. Kth largest Element in an Array.

Quick select : O (N)

"""


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        
        def quickselect(arr,val):

            pi=random.randint(0, len(arr)-1)
            piv= arr[pi]
            
            s =  []
            b =  []
        
         
            for i,x in enumerate(arr):
                if i==pi:
                    continue
                if x >piv:
                    b.append(x)
                elif x<=piv:
                    s.append(x)


            b.append(piv)
            
            if len(b)==val:
                return piv
            elif len(b)>val:
                return quickselect(b,val)
            elif len(b)<val:
                return quickselect(s,val-len(b))
            
        
        return quickselect(nums,k)
