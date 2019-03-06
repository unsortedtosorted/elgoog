"""
1002. Find Common Characters


"""

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        m = {} 
        
        for x in A:
            
            temp = [0]*26
            for c in x:
        
                
                temp[ord(c)-ord('a')]+=1
            
            for x in range(0,26):
                
                if x in m:
                    m[x].append(temp[x])
                else:
                    m[x] = [temp[x]]
        
        r = []
        for x in m:
            
            temp = min(m[x])
            
            while temp>0:
                
                r.append(chr(ord('a')+x))
                temp-=1
           
        return (r)
