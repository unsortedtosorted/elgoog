"""
3. Longest Substring Without Repeating Characters

1. create a map to maitain index of last seen similar char

2. maintain start pointer, initially set to zero

3. If curr not seen previously:
        len+=1
   else:
        m = max(m,l)
        start = r[curr]+1
        len = currindex-start
        r[curr] = currindex
    
      if r[currindex] < start:
        r[curr] = currindex
        l+=1
            
    
    Runtime = O(N)

"""



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = {}
        start = 0
        l = 0
        m = 0
        for i,x in enumerate(s):
            
            if x not in r:
                l+=1
                r[x] = i
            elif x in r:
                
                ind = r[x]
                
                if ind>=start and ind<i:
                    m = max(m,l)
                    l = i-ind
                    start = ind+1
                    r[x] = i
                    
                else:
                    l+=1
                    r[x] = i
                    
        m = max(m,l)
        return m
