"""

#904

1. Maintain a set with size at most 2
2. If a curr is in set, add it to the window
3. If curr is not in set, get the prev of curr
4. remove all elements from the window untill only prev is present
5. add curr to the window
6. if lenght of the window is larger than last one, update max

return max



"""




from collections import deque

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        q = deque()
        
        prev =tree[0]
        
        i=1
        
        q.append(tree[0])
        
        seen = set()
        
        seen.add(prev)
        
        
        m=0
        
        def remove(q,r):
            
            while r in q:
                q.popleft()
                
        def getOther(seen,prev):
            for x in seen:
                if x != prev:
                    return x
        
        while i<len(tree):
            x = tree[i]
            if len(seen)<2:
                if x not in seen:
                    seen.add(x)
                q.append(x)
                
            else:
                if x in seen:
                    q.append(x)
                else:
                    
                    toremove = getOther(seen,prev)
                    remove(q,toremove)
                    seen.remove(toremove)
                    seen.add(x)
                    q.append(x)
            if len(q)>m:
                    m=len(q)
                    
                    
                    
            
            prev = x
            i+=1
                    
                
        if len(q)>m:
            m=len(q) 
        return m
