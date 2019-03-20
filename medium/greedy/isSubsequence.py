"""
392. Is Subsequence

Algo:

  till j == len(s):
    
    search for s[j] in t[i:]
    if found at k :
      search for s[j] in t[k+1:]
    else:
      return False
  
  return True
    

"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        
        def fun(c,i):
            
            while i<len(t):
                
                if t[i] == c :
                    return i+1
                i+=1
            
            return -1
        
        i = 0
        
        for x in s:
            
            i = fun(x,i) 
            if i == -1:
                return False
        
        return True
