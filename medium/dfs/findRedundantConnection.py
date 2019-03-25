"""
684. Redundant Connection

1. for every pair u,v 
    -- if path already exist between u,v in graph 
        ans = [u,v]
    -- if path does not exit, create edge

"""



class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graph = collections.defaultdict(list)

        def createGraph(i,j):
            
            graph[i].append(j)
            graph[j].append(i)
        
        def checkConn(i,j):
            
            src = i
            dest = j
            toVisit = []
            seen = set()
            
            toVisit.append(i)
            
            while len(toVisit) > 0:
                
                curr = toVisit.pop()
                
                if curr == dest:
                    return True
                
                if curr in seen:
                    continue
                
                seen.add(curr)
                toVisit+=graph[curr]
            
            
            return False

        result = []
        for x in edges:
            if not (checkConn(x[0],x[1])):
                createGraph(x[0],x[1])
            else:
                result = x
        
        
        return result
        
        
        
            
        
        
