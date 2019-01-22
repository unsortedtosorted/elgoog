class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        s1=""
        s2=""
        
        
        m1={}
        m2={}
        
        
        for i,x in enumerate(s):
            
            y = t[i]
            
            if x in m1:
                s1=s1+m1[x]
            else:
                s1=s1+str(i)
                m1[x]=str(i)
            
            
            if y in m2:
                s2=s2+m2[y]
            else:
                s2=s2+str(i)
                m2[y]=str(i)
        
        return (s1)==(s2)
