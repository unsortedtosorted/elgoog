"""
#890 Find and Replace pattern

1. Runtime : O(P + W*N )

"""


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        
        p=""
        pm={}
        
        
        for i,x in enumerate(pattern):
            if x in pm:
                p=p+pm[x]
            else:
                p=p+str(i)
                pm[x]=str(i)
        
        
        r = []
        
        for word in words:
            w=""
            wm={}
            
            if len(word)!=len(pattern):
                continue
            for i,x in enumerate(word):
                if x in wm:
                    w=w+wm[x]
                else:
                    w=w+str(i)
                    wm[x]=str(i)
            
            if w==p:
                r.append(word)
        
        
        
        return (r)
                   
