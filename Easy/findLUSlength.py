"""
#521

Find longest uncommon subsequence

1. Brute force:
    1.1 Generate all subsequence using recursion, add keep adding them to set
    1.2 pick the longest uncommon subsequence that is present in one and not in other
    1.3 Run time complexity is 2^a+2^b
    
2. Simple Solution:
    1. if A and B are same, return -1 , since there is no subsequence that is uncommon
    2. if A and B are not same, then return the max length of both strings since the bigger length
    string will never be subsequence of the smaller string.
        
"""



class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a==b:
            return -1
        A=len(a)
        B=len(b)
        
        if A==B:
            return A
        else:
            return max(A,B)
        
               
    def BruteForce(self):
        if a==b:
            return -1
        asub=set()        
        bsub=set()
        self.w=""
        
        def generateSub(pre,word,wset,oset):
            wset.add(pre)
            if pre not in oset:
                if len(pre)>len(self.w):
                    self.w=pre
            i=1
            for x in word:
                generateSub(pre+x,word[i:],wset,oset)
                i+=1   
        
        generateSub("",a,asub,bsub)
        generateSub("",b,bsub,asub)

        
        return len(self.w)
