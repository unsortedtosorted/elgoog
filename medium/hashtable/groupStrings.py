"""
249. Group Shifted Strings

Given strings, return their groups

1. keep track of relative distance between consequetive characters, 1 char is always 1

e.g abc bcd both are 123

store the distance as tuple and string as list in hashtable

Run Time : O(N^2)

"""


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        m = {}
        def getgroup(s):
            
            if len(s)<=0:
                return []
            
            prev = s[0]
            r = (0,)
            
            for i,x in enumerate(s[1:]):
                
                curr = ord(x)
                
                if curr>=ord(prev):
                    r =(r) + ((curr-ord(prev)),)
                
                else:
                    #if curr is less than prev
                    #25-prev+
                    r = (r) + ((26-ord(prev)+curr),)
                
                prev = x
            
            return r
        
        for x in strings:
            t = getgroup(x)
            if t in m:
                m[t].append(x)
            else:
                m[t]=[x]
        
        result = []
        for x in m:
            result.append(m[x])
        
        
        return result
