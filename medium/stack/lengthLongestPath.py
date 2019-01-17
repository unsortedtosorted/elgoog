from collections import deque

class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        
        q = deque()
        
        input=input.split("\n")
        
        prevCount = 0
        temp=0
        
        for x in input:
            temp1 = x.count('\t')
            x=x.replace('\t','')   
            
            
            if prevCount < temp1 :
                q.append("/"+x)
                if "." in x:
                    l=len("".join(q))-1
                    if l>temp:
                        temp=l
                prevCount = temp1
            
            elif prevCount >= temp1:

                i=prevCount-temp1
                
                while len(q)!=temp1:
                    q.pop()
                    i-=1
                    
                q.append("/"+x)
                if "." in x:
                    l=len("".join(q))-1
                    if l>temp:
                        temp=l
                    
                prevCount=temp1
      
        return (temp)
