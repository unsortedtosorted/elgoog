class Tree:
    def __init__(self):
        self.zero=None
        self.one=None
        


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        root= Tree()

        for x in nums:
            temp=root
            num=2**31
            i=31
            while num>0:
                if x&num==num:
                    if temp.one==None:
                        temp.one=Tree()
                    temp=temp.one
                        
                elif x&num==0:
                        if temp.zero==None:
                            temp.zero=Tree()
                        temp=temp.zero
                num=num>>1
                i-=1
        
        m=0
        for x in nums:
            temp=root
            num=2**31
            i=31
            k=0
            r=""
            xo=""
            while num>0:
                
                if x&num==num:
                    #r=r+"1"
                    if temp.zero!=None:
                        temp=temp.zero
                        k=k^num
                        #xo=xo+"1"
                        
                    else:
                        #xo=xo+"0"
                        temp=temp.one
                elif x&num==0:
                    #r=r+"0"
                    if temp.one:
                        temp=temp.one
                        k=k^num
                        #xo=xo+"1"
                        
                    else:
                        #xo=xo+"0"
                        temp=temp.zero
                num=num>>1
                i-=1
            
            if (k)>m:
                m=k
            
            
        return m
