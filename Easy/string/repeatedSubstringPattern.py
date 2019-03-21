"""
459. Repeated Substring Pattern

Algo:

- for every subtring check if some number x times is equal to the given string
- run time:
  O(N)


"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        temp = ""
        for x in s[:-1]:
            
            temp = temp+x
            
            mult = len(s)/len(temp)
            
            if temp*mult == s:
                
                return True
        
        
        return False
