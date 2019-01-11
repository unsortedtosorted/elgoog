"""
Basic algo:
    1. Create a sorted list withh following rule:
        1.1 if current char is greater than last char in list add it to the list
        1.2 if current char is smaller than the last char in the list, then:
            1.2.1 keep removing last char from the list until (all satisfy below):
                - list size is greater than 0
                - the occurence of last character is more than 0
                - the last character is not smaller than current char
"""

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #For storing characters in ascending order
        stack = []
        
        #for marking that charac is already in sorted list
        seen = set()
        
        #storing number of occurences of each character
        d = {}
        
        
        #store number of occurences of each character
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
    
    
        for x in s:
            
            d[x]-=1
            
            if x in seen:
                continue
            else:
                
                while len(stack)>0 and ord(stack[-1])>ord(x) and d[stack[-1]]!=0:
                    seen.remove(stack.pop())

                stack.append(x)
                seen.add(x)
      
        #return final answer
        return "".join(stack)
