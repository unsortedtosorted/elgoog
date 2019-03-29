"""
399. Evaluate Division

1. each equation is a bi directional edge
2. for every query get path
3. multiply all the distance in the path and return answer

"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        w = {}
        edges = {}
        
        #build path
        for i,x in enumerate(equations):
            
            n1 = x[0]
            n2 = x[1]
            
            if n1 in edges:
                edges[n1].append(n2)
            else:
                edges[n1] = [n2]
            
            if n2 in edges:
                edges[n2].append(n1)
            else:
                edges[n2] = [n1]
            
            w[(n1,n2)] = values[i]
            w[(n2,n1)] = 1/values[i]
        
        
        #get path weights
        def getPath(src,dest):
            
            parent = {}
            
            seen = set()
            
            toVisit = [src]
            
            while len(toVisit) > 0:
                
                curr = toVisit.pop()
                if curr in seen:
                    return
                if curr == dest:
                    break
                seen.add(curr)
                
                for nei in edges[curr]:
                    if nei not in seen:
                        
                        parent[nei] = curr
                        toVisit.append(nei)
            
            temp = dest
            ans = 1.0
            inv = False
            while temp!= src:
                
                
                if temp not in parent:
                    return -1
                num = parent[temp]
                denum = temp
                
                ans = ans * w[(num,denum)]
                temp = parent[temp]
            
            return ans
        r = []
        
        
        for x in queries:
            if x[0] not in edges or x[1] not in edges:
                r.append(-1)
                continue
            r.append(getPath(x[0],x[1]))
        
        return r
