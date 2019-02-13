"""
71. Simplify Path

1. split string with "/"
2. remove from stack if ..
3. do nothing if .
4. add to stack in other cases

Run time : O(N)

"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split("/")
        
        stack = []
        for x in l :
            
            if x == "..":
                if len(stack)>0:
                    stack.pop()
            elif x =="" or x ==".":
                continue
            else:
                stack.append(x)
        
        r = ""
        
        if len(stack)>=1:
            r = "/"+stack[0]
        else:
            return "/"
        
        for x in stack[1:]:
            r = r+"/"+x
        
