class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1)>len(nums2):
            temp=nums1
            nums1=nums2
            nums2=temp
        
        
        start=0
        stop=len(nums1)
        
        x=len(nums1)
        y=len(nums2)
        
        
        while start<=stop:
            
            n1 = (start+stop)//2
            n2 = (x+y+1)//2 - n1
            
            
            b4n1p = -sys.maxsize-1 if n1==0 else nums1[n1-1]     
            afn1p= sys.maxsize if n1==x else nums1[n1]
            b4n2p = -sys.maxsize-1 if n2==0 else nums2[n2-1] 
            afn2p = sys.maxsize if n2 == y else nums2[n2]
                
            
            if b4n1p<=afn2p and b4n2p<=afn1p:
                if (x+y)%2==0:
                    return ((max(b4n1p,b4n2p)+min(afn1p,afn2p))/2)
                else:
                    return (max(b4n1p,b4n2p))
            elif b4n1p>afn2p:
                stop=n1-1
            elif b4n2p>afn1p:
                start=n1+1
