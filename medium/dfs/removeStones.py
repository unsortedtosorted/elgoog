"""

947. Most Stones Removed with Same Row or Column

1. first create graphs
    -- an edge exists between 2 nodes if they have common row or coloumn

2. Find number of connected components i.e an island of nodes 

3. Moves is connected components - 1 
    
"""

from collections import deque
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        
        if len(stones) <=1 :
            return 0
        
        graph = collections.defaultdict(list)
        
        for i,x in enumerate(stones):
            
            j = i+1
            
            while j < len(stones):
                y = stones[j]
                
                if x[0] == y[0] or x[1] == y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
                    
                j+=1
        
        
        islands = 0
        seen = set()
        
        print (graph)
        
        for x in graph:
            
            if x not in seen:
                
                stack = [x]
                seen.add(x)
                
                while len(stack) > 0 :
                    
                    islands+=1
                    curr = stack.pop()
                    
                    for y in  graph[curr]:
                        if y not in seen:
                            stack.append(y)
                            seen.add(y)
                    
                islands-=1

        return islands
