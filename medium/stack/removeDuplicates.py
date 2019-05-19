"""
1047. Remove All Adjacent Duplicates In String

use stacks 

"""

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        l = []
        
        
        for x in S:
            
            if len(l) == 0:
                l.append(x)
                
            else:
                
                if l[-1] == x:
                    l.pop()
                else:
                    l.append(x)
        
        return "".join(l)
