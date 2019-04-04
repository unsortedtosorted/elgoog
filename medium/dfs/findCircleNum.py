"""
547. Friend Circles


if x is not visited, increase count by 1 and
      
      visit all its neighbors/neighbors's neighbors/neighbors's neighbor's neighbors until exhausted


Runtime : O(n2)
"""



class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        visited = set()
        toVisit = []
        count = 0
        
        for i in range(0,len(M)):
            
            if i in visited:
                continue
            else:
                count+=1
                toVisit.append(i)
                
                while len(toVisit) > 0:
                    
                    curr = toVisit.pop()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    
                    for j  in range(0,len(M[curr])):
                        if M[curr][j] == 1 and j not in visited:
                            toVisit.append(j)
        
        return count
