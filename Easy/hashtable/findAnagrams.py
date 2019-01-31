"""
438. Find All Anagrams in a String

1. Create a map of character from string1[0:len(string2)] and string2
2. If map equal add 0 to list
3. remove count of curr-len(string2) from the list, add count of curr element to the map
4. if map equal, add [curr-len(string2)+1] to the list

Run time : O(N)

"""

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        r = []
        if len(s)<len(p):
            return r
        
        
        scount = Counter(s[0:len(p)])
        pcount = Counter(p)
        
        if scount == pcount:
            r.append(0)

        for x in range(len(p),len(s)):

            scount[s[x - len(p)]]-=1
            
            if  scount[s[x - len(p)]] == 0:
                del  scount[s[x - len(p)]]
            
            scount[s[x]]+=1
            
            if scount == pcount:
                r.append(x - len(p)+1)
        
        return r
