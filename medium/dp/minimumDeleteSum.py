"""
712. Minimum ASCII Delete Sum for Two Strings

dp equations:

  if s[i]!=s[j]
      return min(v1+ dp(i+1,j), v2+ dp(i,j+1), v1+v2+dp(i+1,j+1)

  if s[i] == s[j]:
      return dp(i+1,j+1)

"""

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        memo = {}
        def getascii(s,ind):
            
            if ind >= len(s):
                return 0
            temp = 0
            
            for x in s[ind:]:
                temp += ord(x)
            
            return temp

        def dp(i,j):
            
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s1) and j == len(s2):
                memo[(i,j)] = 0
                return memo[(i,j)]
            
            if i >= len(s1):
                memo[(i,j)] = getascii(s2,j)
                return memo[(i,j)]
            
            if j >= len(s2):
                memo[(i,j)] = getascii(s1,i)
                return memo[(i,j)] 
            
            
            if s1[i] == s2[j]:
                memo[(i,j)] = dp(i+1,j+1)
                return memo[(i,j)]
            
            val1 = ord(s1[i])
            val2 = ord(s2[j])
            
            memo[(i,j)] = min (val1+ dp(i+1,j),val2+dp(i,j+1),val1+val2+dp(i+1,j+1) )
            return memo[(i,j)]

        return dp(0,0)
